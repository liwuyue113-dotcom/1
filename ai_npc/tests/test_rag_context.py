import unittest
from unittest.mock import patch

from rag.answer_service import UNKNOWN_ANSWER

from ai_npc.rag_context import (
    answer_npc_world_question,
    build_npc_rag_query,
    format_npc_rag_context,
)


class NpcRagContextTests(unittest.TestCase):
    def test_builds_query_with_player_message_and_npc_focus(self):
        query = build_npc_rag_query("吕归尘为什么被关在边境城堡？")

        self.assertIn("吕归尘为什么被关在边境城堡？", query)
        self.assertIn("胆小守卫", query)
        self.assertIn("世界观", query)
        self.assertIn("路线", query)

    def test_formats_matches_as_npc_grounding_context(self):
        matches = [
            {
                "source": "docs/rag_setting.md",
                "heading": "真实安全路线",
                "text": "往前第二个口子跳下去有一条暗道，几乎无人镇守。",
                "score": 0.82,
            }
        ]

        context = format_npc_rag_context(matches)

        self.assertIn("NPC RAG 设定依据", context)
        self.assertIn("docs/rag_setting.md", context)
        self.assertIn("真实安全路线", context)
        self.assertIn("往前第二个口子跳下去", context)
        self.assertIn("0.820", context)

    def test_insufficient_evidence_returns_unknown_reply(self):
        matches = [
            {
                "source": "docs/rag_setting.md",
                "heading": "无关设定",
                "text": "这段内容和问题无关。",
                "score": 0.1,
            }
        ]

        result = answer_npc_world_question(
            "吕归尘的武器叫什么？",
            matches,
            min_similarity=0.35,
        )

        self.assertEqual(UNKNOWN_ANSWER, result["reply"])
        self.assertFalse(result["used_rag"])
        self.assertEqual([], result["sources"])
        self.assertEqual("", result["rag_context"])

    def test_sufficient_evidence_returns_grounded_reply_and_sources(self):
        matches = [
            {
                "source": "docs/rag_setting.md",
                "heading": "真实安全路线",
                "text": "往前第二个口子跳下去有一条暗道，几乎无人镇守。",
                "score": 0.82,
            }
        ]

        with patch.dict("os.environ", {}, clear=True):
            result = answer_npc_world_question(
                "真正安全的路线在哪里？",
                matches,
                min_similarity=0.35,
            )

        self.assertTrue(result["used_rag"])
        self.assertIn("往前第二个口子跳下去", result["reply"])
        self.assertEqual(["docs/rag_setting.md"], result["sources"])
        self.assertIn("NPC RAG 设定依据", result["rag_context"])


if __name__ == "__main__":
    unittest.main()
