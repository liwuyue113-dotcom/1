from dataclasses import dataclass


@dataclass
class EvaluationResult:
    passed: bool
    passed_count: int
    total_count: int
    suggestions: list[str]


def evaluate_level_plan(plan_text: str) -> EvaluationResult:
    checks = [
        _has_player_goal(plan_text),
        _has_three_routes(plan_text),
        _has_risk_and_reward(plan_text),
        _has_failure_condition(plan_text),
    ]
    suggestions = []
    if not checks[0]:
        suggestions.append("补充玩家目标，让关卡目的更清楚。")
    if not checks[1]:
        suggestions.append("补全上路、中路、下方暗道三条路线。")
    if not checks[2]:
        suggestions.append("补充每条路线的风险与奖励。")
    if not checks[3]:
        suggestions.append("补充失败条件，例如倒计时结束或路线压力导致任务失败。")

    passed_count = sum(1 for passed in checks if passed)
    total_count = len(checks)
    return EvaluationResult(
        passed=passed_count == total_count,
        passed_count=passed_count,
        total_count=total_count,
        suggestions=suggestions,
    )


def format_evaluation_report(result: EvaluationResult) -> str:
    lines = [
        "## 质量评价",
        f"- 通过：{result.passed_count} / {result.total_count}",
        f"- 结论：{'通过' if result.passed else '未通过'}",
    ]
    if result.suggestions:
        lines.append("- 改进建议：")
        for suggestion in result.suggestions:
            lines.append(f"  - {suggestion}")
    else:
        lines.append("- 改进建议：当前最低质量检查已通过。")
    return "\n".join(lines)


def _has_player_goal(plan_text: str) -> bool:
    return "## 玩家目标" in plan_text and ("目标" in plan_text or "吕归尘" in plan_text)


def _has_three_routes(plan_text: str) -> bool:
    required_routes = ["上路", "中路", "下方暗道"]
    return "## 三条路线设计" in plan_text and all(route in plan_text for route in required_routes)


def _has_risk_and_reward(plan_text: str) -> bool:
    return "## 风险与奖励" in plan_text and "风险" in plan_text and "奖励" in plan_text


def _has_failure_condition(plan_text: str) -> bool:
    return "## 失败条件" in plan_text and ("失败" in plan_text or "倒计时" in plan_text)
