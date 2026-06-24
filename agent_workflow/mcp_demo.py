import sys

from agent_workflow.mcp_server import handle_request


def run_demo() -> dict:
    tools_response = handle_request({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/list",
        "params": {},
    })
    tool_names = [tool["name"] for tool in tools_response["result"]["tools"]]

    route_response = handle_request({
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {
            "name": "get_route_info",
            "arguments": {"route_id": "secret_tunnel"},
        },
    })
    route_text = route_response["result"]["content"][0]["text"]

    game_state_response = handle_request({
        "jsonrpc": "2.0",
        "id": 3,
        "method": "tools/call",
        "params": {
            "name": "check_game_state",
            "arguments": {},
        },
    })
    game_state_text = game_state_response["result"]["content"][0]["text"]

    return {
        "tool_names": tool_names,
        "route_text": route_text,
        "game_state_text": game_state_text,
    }


def build_demo_output(result: dict) -> str:
    lines = [
        "MCP 工具列表：",
    ]
    lines.extend(f"- {tool_name}" for tool_name in result["tool_names"])
    lines.extend([
        "",
        "路线工具结果：",
        result["route_text"],
        "",
        "游戏状态工具结果：",
        result["game_state_text"],
    ])
    return "\n".join(lines)


def main(argv=None) -> int:
    _ = list(sys.argv[1:] if argv is None else argv)
    print(build_demo_output(run_demo()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
