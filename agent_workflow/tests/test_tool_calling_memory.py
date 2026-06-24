import io
import unittest
from contextlib import redirect_stdout

from agent_workflow.prototype import (
    call_tool,
    create_initial_game_state,
    create_initial_memory,
    run_agent_turn,
)
from agent_workflow.cli import main


class ToolCallingMemoryTests(unittest.TestCase):
    def test_route_question_calls_route_tool_and_records_memory(self):
        game_state = create_initial_game_state()
        memory = create_initial_memory()

        result = run_agent_turn("哪条路线最安全？", game_state, memory)

        self.assertEqual("get_route_info", result["tool_calls"][0]["tool"])
        self.assertEqual("secret_tunnel", result["tool_calls"][0]["args"]["route_id"])
        self.assertIn("往前第二个口子跳下去", result["reply"])
        self.assertEqual("player_asked_route", memory["events"][0]["type"])

    def test_task_question_updates_hint_through_tool(self):
        game_state = create_initial_game_state()
        memory = create_initial_memory()

        result = run_agent_turn("我下一步任务是什么？", game_state, memory)

        self.assertEqual("update_quest_hint", result["tool_calls"][0]["tool"])
        self.assertEqual("先确认钥匙和剩余时间，再选择上路、中路或下方暗道。", result["game_state"]["quest_hint"])
        self.assertEqual("quest_hint_updated", memory["events"][0]["type"])

    def test_unknown_tool_is_rejected(self):
        game_state = create_initial_game_state()

        result = call_tool("open_prison_gate", {}, game_state)

        self.assertFalse(result["ok"])
        self.assertIn("not allowed", result["error"])
        self.assertEqual("", game_state["quest_hint"])

    def test_cli_prints_reply_and_tool_calls(self):
        stdout = io.StringIO()

        with redirect_stdout(stdout):
            exit_code = main(["哪条路线最安全？"])

        output = stdout.getvalue()
        self.assertEqual(0, exit_code)
        self.assertIn("回复：", output)
        self.assertIn("工具：get_route_info", output)


if __name__ == "__main__":
    unittest.main()
