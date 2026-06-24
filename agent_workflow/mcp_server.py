import json
import sys

from agent_workflow.prototype import call_tool, create_initial_game_state


MCP_PROTOCOL_VERSION = "2024-11-05"
SERVER_NAME = "coedx-agent-workflow"
SERVER_VERSION = "0.1.0"


GET_ROUTE_INFO_TOOL = {
    "name": "get_route_info",
    "description": "查询《囚城营救》中上路、中路或下方暗道的基础路线设定。",
    "inputSchema": {
        "type": "object",
        "properties": {
            "route_id": {
                "type": "string",
                "enum": ["upper", "middle", "secret_tunnel"],
                "description": "路线 ID：upper、middle 或 secret_tunnel。",
            }
        },
        "required": ["route_id"],
    },
}

CHECK_GAME_STATE_TOOL = {
    "name": "check_game_state",
    "description": "读取当前默认游戏状态，包括剩余时间、钥匙状态和任务提示。",
    "inputSchema": {
        "type": "object",
        "properties": {},
    },
}

MCP_TOOLS = [
    GET_ROUTE_INFO_TOOL,
    CHECK_GAME_STATE_TOOL,
]


def handle_request(request: dict) -> dict | None:
    method = request.get("method")
    request_id = request.get("id")

    if method == "initialize":
        return _success(request_id, {
            "protocolVersion": MCP_PROTOCOL_VERSION,
            "capabilities": {
                "tools": {},
            },
            "serverInfo": {
                "name": SERVER_NAME,
                "version": SERVER_VERSION,
            },
        })

    if method == "notifications/initialized":
        return None

    if method == "tools/list":
        return _success(request_id, {
            "tools": MCP_TOOLS,
        })

    if method == "tools/call":
        params = request.get("params", {})
        return _success(request_id, _call_mcp_tool(
            params.get("name", ""),
            params.get("arguments", {}),
        ))

    return _error(request_id, -32601, f"Method not found: {method}")


def handle_line(line: str) -> str | None:
    line = _clean_json_line(line)
    request = json.loads(line)
    response = handle_request(request)

    if response is None:
        return None

    return json.dumps(response, ensure_ascii=False)


def run_stdio_server(input_stream=None, output_stream=None) -> None:
    input_stream = sys.stdin if input_stream is None else input_stream
    output_stream = sys.stdout if output_stream is None else output_stream

    for line in input_stream:
        line = line.strip()
        if not line:
            continue

        response_line = handle_line(line)
        if response_line is None:
            continue

        print(response_line, file=output_stream, flush=True)


def _clean_json_line(line: str) -> str:
    line = line.strip().lstrip("\ufeff")
    object_start = line.find("{")
    array_start = line.find("[")
    starts = [index for index in [object_start, array_start] if index >= 0]

    if not starts:
        return line

    return line[min(starts):]


def _call_mcp_tool(tool_name: str, arguments: dict) -> dict:
    result = call_tool(tool_name, arguments, create_initial_game_state())

    if not result.get("ok"):
        return {
            "content": [
                {
                    "type": "text",
                    "text": result.get("error", "Tool call failed."),
                }
            ],
            "isError": True,
        }

    if tool_name == "get_route_info":
        route = result["route"]
        text = f"{route['name']}：{route['summary']}"
    else:
        text = json.dumps(result, ensure_ascii=False)

    return {
        "content": [
            {
                "type": "text",
                "text": text,
            }
        ],
        "isError": False,
    }


def _success(request_id, result: dict) -> dict:
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "result": result,
    }


def _error(request_id, code: int, message: str) -> dict:
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "error": {
            "code": code,
            "message": message,
        },
    }


if __name__ == "__main__":
    run_stdio_server()
