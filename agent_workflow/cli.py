import sys

from agent_workflow.prototype import (
    create_initial_game_state,
    create_initial_memory,
    run_agent_turn,
)


DEFAULT_MESSAGE = "哪条路线最安全？"


def format_turn_result(result: dict) -> str:
    lines = [f"回复：{result['reply']}"]

    if result["tool_calls"]:
        for call in result["tool_calls"]:
            lines.append(f"工具：{call['tool']}")
    else:
        lines.append("工具：无")

    lines.append(f"记忆数量：{len(result['memory']['events'])}")
    return "\n".join(lines)


def main(argv=None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    message = args[0] if args else DEFAULT_MESSAGE
    result = run_agent_turn(message, create_initial_game_state(), create_initial_memory())
    print(format_turn_result(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
