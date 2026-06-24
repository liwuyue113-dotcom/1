import unittest

from rag.answer_service import (
    UNKNOWN_ANSWER,
    answer_question,
    build_grounded_prompt,
    deduplicate_sources,
    has_sufficient_evidence,
)


class AnswerServiceTests(unittest.TestCase):
    def test_insufficient_evidence_returns_false(self):
        matches = [{"text": "无关内容", "source": "docs/game.md", "score": 0.2}]

        self.assertFalse(has_sufficient_evidence(matches, min_similarity=0.35))
        self.assertEqual(UNKNOWN_ANSWER, "当前知识库没有足够信息。")

    def test_sources_are_deduplicated_in_original_order(self):
        matches = [
            {"source": "docs/game.md"},
            {"source": "docs/npc.md"},
            {"source": "docs/game.md"},
        ]

        self.assertEqual(
            deduplicate_sources(matches),
            ["docs/game.md", "docs/npc.md"],
        )

    def test_prompt_forbids_unsupported_facts(self):
        matches = [
            {
                "text": "暗道几乎无人镇守。",
                "source": "docs/game.md",
                "heading": "路线",
                "score": 0.8,
            }
        ]

        prompt = build_grounded_prompt("暗道安全吗？", matches)

        self.assertIn("只能根据提供的设定片段回答", prompt)
        self.assertIn("不要补充片段中没有的信息", prompt)
        self.assertIn("暗道几乎无人镇守", prompt)
        self.assertIn("docs/game.md", prompt)

    def test_unconfirmed_setting_is_not_presented_as_an_answer(self):
        matches = [
            {
                "text": "姬野营救目标的原因：待补充。",
                "source": "docs/game_design.md",
                "heading": "故事背景",
                "score": 0.9,
            }
        ]

        result = answer_question(
            "玩家为什么要营救人质？",
            matches,
            min_similarity=0.35,
        )

        self.assertEqual(result["answer"], UNKNOWN_ANSWER)


if __name__ == "__main__":
    unittest.main()
