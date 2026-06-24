import io
import unittest
from contextlib import redirect_stdout

from agent_workflow.mcp_demo import build_demo_output, main, run_demo


class McpDemoTests(unittest.TestCase):
    def test_run_demo_collects_tools_route_and_game_state(self):
        result = run_demo()

        self.assertEqual(["get_route_info", "check_game_state"], result["tool_names"])
        self.assertIn("往前第二个口子跳下去", result["route_text"])
        self.assertIn("remaining_time", result["game_state_text"])
        self.assertIn("has_key", result["game_state_text"])
        self.assertIn("quest_hint", result["game_state_text"])

    def test_build_demo_output_is_human_readable(self):
        output = build_demo_output({
            "tool_names": ["get_route_info", "check_game_state"],
            "route_text": "下方暗道：往前第二个口子跳下去。",
            "game_state_text": '{"remaining_time": 180, "has_key": false, "quest_hint": ""}',
        })

        self.assertIn("MCP 工具列表", output)
        self.assertIn("get_route_info", output)
        self.assertIn("check_game_state", output)
        self.assertIn("路线工具结果", output)
        self.assertIn("游戏状态工具结果", output)

    def test_main_prints_demo_output(self):
        stdout = io.StringIO()

        with redirect_stdout(stdout):
            exit_code = main([])

        output = stdout.getvalue()
        self.assertEqual(0, exit_code)
        self.assertIn("MCP 工具列表", output)
        self.assertIn("路线工具结果", output)
        self.assertIn("游戏状态工具结果", output)


if __name__ == "__main__":
    unittest.main()
