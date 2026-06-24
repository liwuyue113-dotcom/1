import json
from io import StringIO
import unittest

from agent_workflow.mcp_server import handle_request


class McpServerTests(unittest.TestCase):
    def test_initialize_returns_mcp_server_info(self):
        response = handle_request({
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {},
        })

        self.assertEqual("2.0", response["jsonrpc"])
        self.assertEqual(1, response["id"])
        self.assertEqual("coedx-agent-workflow", response["result"]["serverInfo"]["name"])
        self.assertIn("tools", response["result"]["capabilities"])

    def test_tools_list_exposes_allowed_read_tools(self):
        response = handle_request({
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/list",
            "params": {},
        })

        tools = response["result"]["tools"]
        tool_names = [tool["name"] for tool in tools]
        self.assertEqual(["get_route_info", "check_game_state"], tool_names)
        self.assertIn("route_id", tools[0]["inputSchema"]["properties"])
        self.assertEqual({}, tools[1]["inputSchema"]["properties"])

    def test_tools_call_returns_route_info_content(self):
        response = handle_request({
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "get_route_info",
                "arguments": {"route_id": "secret_tunnel"},
            },
        })

        self.assertFalse(response["result"]["isError"])
        self.assertIn("往前第二个口子跳下去", response["result"]["content"][0]["text"])

    def test_tools_call_returns_game_state_content(self):
        response = handle_request({
            "jsonrpc": "2.0",
            "id": 30,
            "method": "tools/call",
            "params": {
                "name": "check_game_state",
                "arguments": {},
            },
        })

        text = response["result"]["content"][0]["text"]
        self.assertFalse(response["result"]["isError"])
        self.assertIn("remaining_time", text)
        self.assertIn("180", text)
        self.assertIn("has_key", text)
        self.assertIn("quest_hint", text)

    def test_tools_call_rejects_unknown_tool(self):
        response = handle_request({
            "jsonrpc": "2.0",
            "id": 4,
            "method": "tools/call",
            "params": {
                "name": "open_prison_gate",
                "arguments": {},
            },
        })

        self.assertTrue(response["result"]["isError"])
        self.assertIn("not allowed", response["result"]["content"][0]["text"])

    def test_main_loop_handles_one_json_rpc_line(self):
        from agent_workflow.mcp_server import handle_line

        output = handle_line(json.dumps({
            "jsonrpc": "2.0",
            "id": 5,
            "method": "tools/list",
            "params": {},
        }, ensure_ascii=False))

        response = json.loads(output)
        self.assertEqual(5, response["id"])
        self.assertEqual("get_route_info", response["result"]["tools"][0]["name"])
        self.assertEqual("check_game_state", response["result"]["tools"][1]["name"])

    def test_handle_line_accepts_utf8_bom_from_powershell_pipe(self):
        from agent_workflow.mcp_server import handle_line

        output = handle_line("\ufeff" + json.dumps({
            "jsonrpc": "2.0",
            "id": 6,
            "method": "tools/list",
            "params": {},
        }, ensure_ascii=False))

        response = json.loads(output)
        self.assertEqual(6, response["id"])
        self.assertEqual("get_route_info", response["result"]["tools"][0]["name"])
        self.assertEqual("check_game_state", response["result"]["tools"][1]["name"])

    def test_handle_line_accepts_mojibake_prefix_from_windows_pipe(self):
        from agent_workflow.mcp_server import handle_line

        output = handle_line(chr(38168) + chr(32310) + json.dumps({
            "jsonrpc": "2.0",
            "id": 7,
            "method": "tools/list",
            "params": {},
        }, ensure_ascii=False))

        response = json.loads(output)
        self.assertEqual(7, response["id"])
        self.assertEqual("get_route_info", response["result"]["tools"][0]["name"])
        self.assertEqual("check_game_state", response["result"]["tools"][1]["name"])

    def test_stdio_server_writes_one_response_per_request(self):
        from agent_workflow.mcp_server import run_stdio_server

        input_stream = StringIO(
            json.dumps({"jsonrpc": "2.0", "id": 8, "method": "tools/list", "params": {}})
            + "\n"
            + json.dumps({"jsonrpc": "2.0", "id": 9, "method": "tools/list", "params": {}})
            + "\n"
        )
        output_stream = StringIO()

        run_stdio_server(input_stream, output_stream)

        responses = [json.loads(line) for line in output_stream.getvalue().splitlines()]
        self.assertEqual([8, 9], [response["id"] for response in responses])


if __name__ == "__main__":
    unittest.main()
