import unittest

from rag.conflict_checker import (
    check_setting_conflict,
    format_conflict_result,
)


class ConflictCheckerTests(unittest.TestCase):
    def test_detects_obvious_enemy_count_conflict(self):
        matches = [
            {
                "text": "下方暗道路线：只有暗道内部有一个站岗的守卫。",
                "source": "docs/rag_setting.md",
                "heading": "三条路线敌人站位",
                "score": 0.88,
            }
        ]

        result = check_setting_conflict(
            "新增设定：下方暗道内部有多个守卫来回巡逻。",
            matches,
            min_similarity=0.35,
        )

        self.assertEqual(result["status"], "possible_conflict")
        self.assertEqual(result["sources"], ["docs/rag_setting.md"])
        self.assertIn("守卫数量", result["conflict_reasons"][0])

    def test_reports_no_obvious_conflict_when_setting_matches_evidence(self):
        matches = [
            {
                "text": "下方暗道路线：只有暗道内部有一个站岗的守卫。",
                "source": "docs/rag_setting.md",
                "heading": "三条路线敌人站位",
                "score": 0.88,
            }
        ]

        result = check_setting_conflict(
            "新增设定：下方暗道内部只有一个站岗守卫。",
            matches,
            min_similarity=0.35,
        )

        self.assertEqual(result["status"], "no_obvious_conflict")
        self.assertEqual(result["conflict_reasons"], [])

    def test_insufficient_evidence_does_not_guess_conflict(self):
        matches = [
            {
                "text": "胆小守卫躲在 Level1 深处。",
                "source": "docs/rag_setting.md",
                "heading": "胆小守卫位置",
                "score": 0.2,
            }
        ]

        result = check_setting_conflict(
            "新增设定：牢房门口有一名商人。",
            matches,
            min_similarity=0.35,
        )

        self.assertEqual(result["status"], "insufficient_evidence")
        self.assertEqual(result["conflict_reasons"], [])

    def test_formats_result_for_command_line_demo(self):
        result = {
            "status": "possible_conflict",
            "summary": "可能冲突：守卫数量与已确认设定不一致。",
            "sources": ["docs/rag_setting.md"],
            "conflict_reasons": ["守卫数量与已确认设定不一致"],
            "matches": [
                {
                    "text": "下方暗道路线：只有暗道内部有一个站岗的守卫。",
                    "source": "docs/rag_setting.md",
                    "heading": "三条路线敌人站位",
                    "score": 0.88,
                }
            ],
        }

        output = format_conflict_result(result)

        self.assertIn("可能冲突", output)
        self.assertIn("守卫数量", output)
        self.assertIn("docs/rag_setting.md", output)
        self.assertIn("三条路线敌人站位", output)


if __name__ == "__main__":
    unittest.main()
