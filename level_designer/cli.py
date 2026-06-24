import argparse
import os

from level_designer.deepseek_client import DeepSeekClient, DeepSeekError, generate_plan_with_deepseek
from level_designer.evaluator import evaluate_level_plan, format_evaluation_report
from level_designer.generator import LevelDesignInput, generate_level_plan
from level_designer.json_output import build_json_output, format_json_output
from level_designer.rag_context import retrieve_rag_context


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Generate a fixed level design plan.")
    parser.add_argument(
        "--provider",
        choices=["template", "deepseek"],
        default="template",
        help="生成方式：template 使用本地模板，deepseek 调用 DeepSeek",
    )
    parser.add_argument("--theme", required=True, help="关卡主题")
    parser.add_argument("--goal", required=True, help="玩家目标")
    parser.add_argument("--difficulty", required=True, help="关卡难度")
    parser.add_argument("--routes", required=True, help="三条路线资料")
    parser.add_argument("--model", default="deepseek-chat", help="DeepSeek 模型名")
    parser.add_argument("--use-rag", action="store_true", help="从 RAG 检索已确认设定并加入生成上下文")
    parser.add_argument("--evaluate", action="store_true", help="生成后追加最低质量评价")
    parser.add_argument(
        "--format",
        choices=["markdown", "json"],
        default="markdown",
        help="输出格式：markdown 适合人读，json 适合网页或 Unity 工具读取",
    )
    args = parser.parse_args(argv)

    design_input = LevelDesignInput(
        theme=args.theme,
        player_goal=args.goal,
        difficulty=args.difficulty,
        route_notes=args.routes,
    )
    if args.use_rag:
        design_input.rag_context = retrieve_rag_context(design_input)

    warnings = []
    used_provider = args.provider
    plan_text = None
    if args.provider == "deepseek":
        api_key = os.environ.get("DEEPSEEK_API_KEY", "")
        if api_key:
            try:
                client = DeepSeekClient(api_key=api_key, model=args.model)
                plan_text = generate_plan_with_deepseek(design_input, client)
            except DeepSeekError as exc:
                warnings.append(f"DeepSeek 调用失败，已回退到本地模板：{exc}")
                used_provider = "template"
        else:
            warnings.append("DeepSeek 未启用：缺少环境变量 DEEPSEEK_API_KEY，已回退到本地模板。")
            used_provider = "template"

    if plan_text is None:
        plan_text = generate_level_plan(design_input)

    _print_plan(
        plan_text=plan_text,
        should_evaluate=args.evaluate,
        output_format=args.format,
        design_input=design_input,
        provider=used_provider,
        warnings=warnings,
    )
    return 0


def _print_plan(
    plan_text: str,
    should_evaluate: bool,
    output_format: str,
    design_input: LevelDesignInput,
    provider: str,
    warnings: list[str],
) -> None:
    evaluation = evaluate_level_plan(plan_text) if should_evaluate else None

    if output_format == "json":
        print(
            format_json_output(
                build_json_output(
                    design_input=design_input,
                    plan_markdown=plan_text,
                    evaluation=evaluation,
                    provider=provider,
                    warnings=warnings,
                )
            )
        )
        return

    for warning in warnings:
        print(warning)
    print(plan_text)
    if evaluation:
        print()
        print(format_evaluation_report(evaluation))


if __name__ == "__main__":
    raise SystemExit(main())
