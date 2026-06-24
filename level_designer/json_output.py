import json
from dataclasses import asdict

from level_designer.evaluator import EvaluationResult
from level_designer.generator import LevelDesignInput


def build_json_output(
    design_input: LevelDesignInput,
    plan_markdown: str,
    evaluation: EvaluationResult | None,
    provider: str,
    warnings: list[str],
) -> dict:
    return {
        "provider": provider,
        "input": {
            "theme": design_input.theme,
            "player_goal": design_input.player_goal,
            "difficulty": design_input.difficulty,
            "route_notes": design_input.route_notes,
            "has_rag_context": bool(design_input.rag_context.strip()),
        },
        "plan_markdown": plan_markdown,
        "evaluation": asdict(evaluation) if evaluation else None,
        "warnings": warnings,
    }


def format_json_output(data: dict) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)
