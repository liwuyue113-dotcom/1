import unittest
import json
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from level_designer.cli import main
from level_designer.deepseek_client import build_level_design_prompt, generate_plan_with_deepseek
from level_designer.evaluator import evaluate_level_plan, format_evaluation_report
from level_designer.generator import LevelDesignInput, generate_level_plan
from level_designer.json_output import build_json_output, format_json_output
from level_designer.rag_context import build_rag_query, format_rag_matches


class LevelDesignerGeneratorTests(unittest.TestCase):
    def test_generates_fixed_markdown_sections_for_three_routes(self):
        design_input = LevelDesignInput(
            theme="离国边境城堡潜入",
            player_goal="在黎明前找到吕归尘",
            difficulty="普通",
            route_notes=(
                "上路较长，敌人数量一般；中路长度一般，敌人略多；"
                "下方暗道长度正常，敌人最少，需要胆小守卫真实情报。"
            ),
        )

        plan = generate_level_plan(design_input)

        expected_sections = [
            "# 离国边境城堡潜入关卡策划案",
            "## 玩家目标",
            "## 三条路线设计",
            "### 上路",
            "### 中路",
            "### 下方暗道",
            "## 敌人配置",
            "## 风险与奖励",
            "## 失败条件",
            "## 设计意图",
            "## 优化建议",
        ]
        for section in expected_sections:
            self.assertIn(section, plan)

        self.assertIn("在黎明前找到吕归尘", plan)
        self.assertIn("路线较长", plan)
        self.assertIn("敌人略多", plan)
        self.assertIn("胆小守卫真实情报", plan)

    def test_rejects_missing_required_fields(self):
        design_input = LevelDesignInput(
            theme="",
            player_goal="在黎明前找到吕归尘",
            difficulty="普通",
            route_notes="三条路线已经确认。",
        )

        with self.assertRaisesRegex(ValueError, "theme"):
            generate_level_plan(design_input)

    def test_cli_prints_generated_plan(self):
        output = StringIO()

        with redirect_stdout(output):
            exit_code = main(
                [
                    "--theme",
                    "离国边境城堡潜入",
                    "--goal",
                    "在黎明前找到吕归尘",
                    "--difficulty",
                    "普通",
                    "--routes",
                    "三条路线分别是上路、中路和下方暗道。",
                ]
            )

        self.assertEqual(0, exit_code)
        self.assertIn("# 离国边境城堡潜入关卡策划案", output.getvalue())
        self.assertIn("## 三条路线设计", output.getvalue())

    def test_builds_deepseek_prompt_with_fixed_sections_and_route_notes(self):
        design_input = LevelDesignInput(
            theme="离国边境城堡潜入",
            player_goal="在黎明前找到吕归尘",
            difficulty="普通",
            route_notes="上路长；中路敌人多；下方暗道敌人最少。",
        )

        prompt = build_level_design_prompt(design_input)

        self.assertIn("离国边境城堡潜入", prompt)
        self.assertIn("在黎明前找到吕归尘", prompt)
        self.assertIn("上路长；中路敌人多；下方暗道敌人最少。", prompt)
        self.assertIn("## 三条路线设计", prompt)
        self.assertIn("## 优化建议", prompt)

    def test_generates_plan_with_deepseek_client(self):
        class FakeClient:
            def generate(self, prompt):
                self.prompt = prompt
                return "# AI 生成的关卡策划案\n\n## 三条路线设计\nAI 输出"

        design_input = LevelDesignInput(
            theme="离国边境城堡潜入",
            player_goal="在黎明前找到吕归尘",
            difficulty="普通",
            route_notes="三条路线分别是上路、中路和下方暗道。",
        )
        client = FakeClient()

        plan = generate_plan_with_deepseek(design_input, client)

        self.assertIn("# AI 生成的关卡策划案", plan)
        self.assertIn("离国边境城堡潜入", client.prompt)

    def test_cli_deepseek_provider_falls_back_without_api_key(self):
        output = StringIO()

        with patch.dict("os.environ", {}, clear=True), redirect_stdout(output):
            exit_code = main(
                [
                    "--provider",
                    "deepseek",
                    "--theme",
                    "离国边境城堡潜入",
                    "--goal",
                    "在黎明前找到吕归尘",
                    "--difficulty",
                    "普通",
                    "--routes",
                    "三条路线分别是上路、中路和下方暗道。",
                ]
            )

        self.assertEqual(0, exit_code)
        self.assertIn("DeepSeek 未启用", output.getvalue())
        self.assertIn("# 离国边境城堡潜入关卡策划案", output.getvalue())

    def test_builds_rag_query_from_level_design_input(self):
        design_input = LevelDesignInput(
            theme="离国边境城堡潜入",
            player_goal="在黎明前找到吕归尘",
            difficulty="普通",
            route_notes="三条路线分别是上路、中路和下方暗道。",
        )

        query = build_rag_query(design_input)

        self.assertIn("三条路线", query)
        self.assertIn("上路", query)
        self.assertIn("下方暗道", query)
        self.assertIn("敌人站位", query)
        self.assertNotIn("吕归尘", query)

    def test_formats_rag_matches_as_grounded_context(self):
        matches = [
            {
                "source": "docs/rag_setting.md",
                "heading": "三条路线基础设定",
                "text": "上路较长，中路敌人略多，下方暗道敌人最少。",
                "score": 0.78,
            }
        ]

        context = format_rag_matches(matches)

        self.assertIn("RAG 设定依据", context)
        self.assertIn("docs/rag_setting.md", context)
        self.assertIn("三条路线基础设定", context)
        self.assertIn("下方暗道敌人最少", context)

    def test_deepseek_prompt_includes_rag_context_when_available(self):
        design_input = LevelDesignInput(
            theme="离国边境城堡潜入",
            player_goal="在黎明前找到吕归尘",
            difficulty="普通",
            route_notes="三条路线分别是上路、中路和下方暗道。",
            rag_context="RAG 设定依据：下方暗道只有一个站岗守卫。",
        )

        prompt = build_level_design_prompt(design_input)

        self.assertIn("RAG 设定依据", prompt)
        self.assertIn("下方暗道只有一个站岗守卫", prompt)

    def test_cli_use_rag_adds_retrieved_context_to_template_output(self):
        output = StringIO()

        with patch(
            "level_designer.cli.retrieve_rag_context",
            return_value="RAG 设定依据：下方暗道只有一个站岗守卫。",
        ), redirect_stdout(output):
            exit_code = main(
                [
                    "--use-rag",
                    "--theme",
                    "离国边境城堡潜入",
                    "--goal",
                    "在黎明前找到吕归尘",
                    "--difficulty",
                    "普通",
                    "--routes",
                    "三条路线分别是上路、中路和下方暗道。",
                ]
            )

        self.assertEqual(0, exit_code)
        self.assertIn("## RAG 设定依据", output.getvalue())
        self.assertIn("下方暗道只有一个站岗守卫", output.getvalue())

    def test_evaluates_complete_level_plan_as_passed(self):
        plan = generate_level_plan(
            LevelDesignInput(
                theme="离国边境城堡潜入",
                player_goal="在黎明前找到吕归尘",
                difficulty="普通",
                route_notes="三条路线分别是上路、中路和下方暗道。",
            )
        )

        result = evaluate_level_plan(plan)

        self.assertTrue(result.passed)
        self.assertEqual(4, result.passed_count)
        self.assertEqual(4, result.total_count)
        self.assertEqual([], result.suggestions)

    def test_evaluates_missing_route_design_as_failed(self):
        plan = "\n".join(
            [
                "# 离国边境城堡潜入关卡策划案",
                "## 玩家目标",
                "- 目标：在黎明前找到吕归尘",
                "## 三条路线设计",
                "### 上路",
                "- 定位：路线较长。",
                "## 风险与奖励",
                "- 上路风险来自时间消耗。",
                "## 失败条件",
                "- 倒计时结束前没有找到吕归尘。",
            ]
        )

        result = evaluate_level_plan(plan)

        self.assertFalse(result.passed)
        self.assertIn("补全上路、中路、下方暗道三条路线。", result.suggestions)

    def test_formats_evaluation_report(self):
        result = evaluate_level_plan(
            "# 策划案\n## 玩家目标\n目标\n## 三条路线设计\n### 上路\n### 中路\n### 下方暗道\n"
            "## 风险与奖励\n风险\n奖励\n## 失败条件\n失败"
        )

        report = format_evaluation_report(result)

        self.assertIn("## 质量评价", report)
        self.assertIn("通过：4 / 4", report)
        self.assertIn("结论：通过", report)

    def test_cli_evaluate_appends_quality_report(self):
        output = StringIO()

        with redirect_stdout(output):
            exit_code = main(
                [
                    "--evaluate",
                    "--theme",
                    "离国边境城堡潜入",
                    "--goal",
                    "在黎明前找到吕归尘",
                    "--difficulty",
                    "普通",
                    "--routes",
                    "三条路线分别是上路、中路和下方暗道。",
                ]
            )

        self.assertEqual(0, exit_code)
        self.assertIn("## 质量评价", output.getvalue())
        self.assertIn("结论：通过", output.getvalue())

    def test_builds_json_output_with_plan_input_and_evaluation(self):
        design_input = LevelDesignInput(
            theme="离国边境城堡潜入",
            player_goal="在黎明前找到吕归尘",
            difficulty="普通",
            route_notes="三条路线分别是上路、中路和下方暗道。",
        )
        plan = generate_level_plan(design_input)
        evaluation = evaluate_level_plan(plan)

        payload = build_json_output(
            design_input=design_input,
            plan_markdown=plan,
            evaluation=evaluation,
            provider="template",
            warnings=[],
        )

        self.assertEqual("离国边境城堡潜入", payload["input"]["theme"])
        self.assertIn("# 离国边境城堡潜入关卡策划案", payload["plan_markdown"])
        self.assertTrue(payload["evaluation"]["passed"])
        self.assertEqual("template", payload["provider"])

    def test_formats_json_output_as_valid_utf8_json(self):
        data = {"title": "离国边境城堡潜入", "warnings": []}

        text = format_json_output(data)

        self.assertEqual("离国边境城堡潜入", json.loads(text)["title"])

    def test_cli_json_format_outputs_valid_json(self):
        output = StringIO()

        with redirect_stdout(output):
            exit_code = main(
                [
                    "--format",
                    "json",
                    "--evaluate",
                    "--theme",
                    "离国边境城堡潜入",
                    "--goal",
                    "在黎明前找到吕归尘",
                    "--difficulty",
                    "普通",
                    "--routes",
                    "三条路线分别是上路、中路和下方暗道。",
                ]
            )

        payload = json.loads(output.getvalue())
        self.assertEqual(0, exit_code)
        self.assertIn("plan_markdown", payload)
        self.assertTrue(payload["evaluation"]["passed"])
        self.assertEqual([], payload["warnings"])

    def test_cli_json_format_keeps_deepseek_fallback_warning_inside_json(self):
        output = StringIO()

        with patch.dict("os.environ", {}, clear=True), redirect_stdout(output):
            exit_code = main(
                [
                    "--format",
                    "json",
                    "--provider",
                    "deepseek",
                    "--theme",
                    "离国边境城堡潜入",
                    "--goal",
                    "在黎明前找到吕归尘",
                    "--difficulty",
                    "普通",
                    "--routes",
                    "三条路线分别是上路、中路和下方暗道。",
                ]
            )

        payload = json.loads(output.getvalue())
        self.assertEqual(0, exit_code)
        self.assertIn("DeepSeek 未启用", payload["warnings"][0])
        self.assertIn("plan_markdown", payload)


if __name__ == "__main__":
    unittest.main()
