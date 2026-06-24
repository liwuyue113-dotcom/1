from rag.answer_service import deduplicate_sources, has_sufficient_evidence

POSSIBLE_CONFLICT = "possible_conflict"
NO_OBVIOUS_CONFLICT = "no_obvious_conflict"
INSUFFICIENT_EVIDENCE = "insufficient_evidence"

SINGLE_GUARD_TERMS = [
    "只有一个",
    "一个站岗",
    "一名守卫",
    "一个守卫",
]

MULTIPLE_GUARD_TERMS = [
    "多个守卫",
    "多名守卫",
    "好几个守卫",
    "很多守卫",
    "不止一个守卫",
]


def check_setting_conflict(
    candidate_setting: str,
    matches: list[dict],
    min_similarity: float,
) -> dict:
    sources = deduplicate_sources(matches)

    if not has_sufficient_evidence(matches, min_similarity):
        return {
            "status": INSUFFICIENT_EVIDENCE,
            "summary": "证据不足：暂时无法判断这条新增设定是否冲突。",
            "sources": [],
            "conflict_reasons": [],
            "matches": matches,
        }

    conflict_reasons = _find_conflict_reasons(candidate_setting, matches)

    if conflict_reasons:
        return {
            "status": POSSIBLE_CONFLICT,
            "summary": "可能冲突：新增设定与已确认设定存在明显不一致。",
            "sources": sources,
            "conflict_reasons": conflict_reasons,
            "matches": matches,
        }

    return {
        "status": NO_OBVIOUS_CONFLICT,
        "summary": "暂未发现明显冲突：仍建议人工复核设定是否符合关卡设计。",
        "sources": sources,
        "conflict_reasons": [],
        "matches": matches,
    }


def format_conflict_result(result: dict) -> str:
    lines = [
        f"结论：{result['summary']}",
    ]

    if result["conflict_reasons"]:
        lines.append("")
        lines.append("冲突原因：")
        for reason in result["conflict_reasons"]:
            lines.append(f"- {reason}")

    if result["sources"]:
        lines.append("")
        lines.append("来源：")
        for source in result["sources"]:
            lines.append(f"- {source}")

    if result["matches"]:
        lines.append("")
        lines.append("相关设定片段：")
        for match in result["matches"]:
            lines.append(
                f"- [{match['score']:.3f}] "
                f"{match['source']} / {match.get('heading', '')}"
            )
            lines.append(f"  {match['text']}")

    return "\n".join(lines)


def _find_conflict_reasons(candidate_setting: str, matches: list[dict]) -> list[str]:
    reasons = []
    candidate_has_single_guard = _contains_any(candidate_setting, SINGLE_GUARD_TERMS)
    candidate_has_multiple_guards = _contains_any(candidate_setting, MULTIPLE_GUARD_TERMS)

    for match in matches:
        evidence = match["text"]
        evidence_has_single_guard = _contains_any(evidence, SINGLE_GUARD_TERMS)
        evidence_has_multiple_guards = _contains_any(evidence, MULTIPLE_GUARD_TERMS)

        if candidate_has_multiple_guards and evidence_has_single_guard:
            reasons.append("守卫数量与已确认设定不一致：新增设定写成多个守卫，旧设定强调只有一个守卫。")
        elif candidate_has_single_guard and evidence_has_multiple_guards:
            reasons.append("守卫数量与已确认设定不一致：新增设定写成一个守卫，旧设定强调有多个守卫。")

    return _deduplicate(reasons)


def _contains_any(text: str, terms: list[str]) -> bool:
    return any(term in text for term in terms)


def _deduplicate(items: list[str]) -> list[str]:
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result
