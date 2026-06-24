ALLOWED_TOOLS = {
    "get_route_info",
    "check_game_state",
    "update_quest_hint",
}

ROUTE_INFO = {
    "upper": {
        "name": "上路",
        "summary": "上路更长，前段守卫分散，后段有连续几个守卫站岗。",
    },
    "middle": {
        "name": "中路",
        "summary": "中路长度一般，敌人更多，有些位置有好几个守卫站岗。",
    },
    "secret_tunnel": {
        "name": "下方暗道",
        "summary": "往前第二个口子跳下去有一条暗道，暗道内部只有一个站岗守卫。",
    },
}

DEFAULT_QUEST_HINT = "先确认钥匙和剩余时间，再选择上路、中路或下方暗道。"


def create_initial_game_state() -> dict:
    return {
        "remaining_time": 180,
        "has_key": False,
        "quest_hint": "",
    }


def create_initial_memory() -> dict:
    return {
        "events": [],
    }


def record_memory(memory: dict, event_type: str, content: str) -> dict:
    event = {
        "type": event_type,
        "content": content,
    }
    memory.setdefault("events", []).append(event)
    return event


def call_tool(tool_name: str, args: dict, game_state: dict) -> dict:
    if tool_name not in ALLOWED_TOOLS:
        return {
            "ok": False,
            "error": f"Tool '{tool_name}' is not allowed.",
        }

    if tool_name == "get_route_info":
        route_id = args.get("route_id", "")
        route = ROUTE_INFO.get(route_id)
        if route is None:
            return {
                "ok": False,
                "error": f"Unknown route: {route_id}",
            }
        return {
            "ok": True,
            "route_id": route_id,
            "route": route,
        }

    if tool_name == "check_game_state":
        return {
            "ok": True,
            "remaining_time": game_state.get("remaining_time"),
            "has_key": game_state.get("has_key"),
            "quest_hint": game_state.get("quest_hint", ""),
        }

    hint = args.get("hint", DEFAULT_QUEST_HINT)
    game_state["quest_hint"] = hint
    return {
        "ok": True,
        "quest_hint": hint,
    }


def run_agent_turn(player_message: str, game_state: dict | None = None, memory: dict | None = None) -> dict:
    state = game_state if game_state is not None else create_initial_game_state()
    memory_store = memory if memory is not None else create_initial_memory()
    message = player_message.strip()
    tool_calls = []

    if _is_route_question(message):
        tool_name = "get_route_info"
        args = {"route_id": "secret_tunnel"}
        tool_result = call_tool(tool_name, args, state)
        tool_calls.append({"tool": tool_name, "args": args, "result": tool_result})
        record_memory(memory_store, "player_asked_route", message)
        reply = tool_result["route"]["summary"] if tool_result["ok"] else "当前无法确认路线信息。"
    elif _is_task_question(message):
        tool_name = "update_quest_hint"
        args = {"hint": DEFAULT_QUEST_HINT}
        tool_result = call_tool(tool_name, args, state)
        tool_calls.append({"tool": tool_name, "args": args, "result": tool_result})
        record_memory(memory_store, "quest_hint_updated", message)
        reply = tool_result["quest_hint"]
    else:
        record_memory(memory_store, "player_message", message)
        reply = "我先记下这句话；当前原型只会调用路线和任务提示工具。"

    return {
        "reply": reply,
        "tool_calls": tool_calls,
        "memory": memory_store,
        "game_state": state,
    }


def _is_route_question(message: str) -> bool:
    return any(keyword in message for keyword in ["路线", "安全", "暗道", "守卫"])


def _is_task_question(message: str) -> bool:
    return any(keyword in message for keyword in ["任务", "下一步", "目标"])
