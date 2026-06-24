# Agent Workflow 最小原型

## 文档用途

本文记录《囚城营救》作品集项目中 Tool Calling / Memory / Agent Workflow 阶段的最小可用原型。

各阶段在作品集中的作用说明见 `docs/agent_workflow_stage_roles.md`。

当前版本不是正式 MCP 服务，也不是多 Agent 系统；它先作为本地 Python 原型证明工具调用和记忆边界，并已接入外部 FastAPI 的最小 HTTP 接口用于演示：

- Agent 不能随便改游戏状态，只能调用白名单工具。
- 工具调用结果可以影响受控的游戏状态字段。
- 玩家关键互动可以写入本局记忆。
- 原型可以通过命令行演示，方便讲解 Agent Workflow 的基本概念。
- 外部 FastAPI 可以通过 `POST /agent/turn` 调用这一轮 Agent 流程。
- 真实 MCP 最小服务可以通过 stdio JSON-RPC 暴露 `get_route_info` 和 `check_game_state` 工具。

## 当前阶段目标

当前阶段：Tool Calling / Memory 最小原型。

本阶段最低目标：

1. 定义一个白名单工具调用入口。
2. 支持查询路线信息。
3. 支持更新任务提示。
4. 拒绝未授权工具。
5. 记录玩家关键行为到本局记忆。
6. 提供命令行演示。

## 已实现文件

- `agent_workflow/prototype.py`
- `agent_workflow/cli.py`
- `agent_workflow/mcp_server.py`
- `agent_workflow/mcp_demo.py`
- `agent_workflow/mcp_client_config.example.json`
- `agent_workflow/tests/test_tool_calling_memory.py`
- `agent_workflow/tests/test_mcp_server.py`
- `agent_workflow/tests/test_mcp_demo.py`
- `D:\develop\pythons\api.py`
- `D:\develop\pythons\test_api_rag.py`

## 当前工具

| 工具 | 用途 |
| --- | --- |
| `get_route_info` | 查询上路、中路或下方暗道的基础路线设定 |
| `check_game_state` | 读取剩余时间、钥匙状态和当前任务提示 |
| `update_quest_hint` | 更新任务提示文本 |

未在白名单里的工具会被拒绝。例如 `open_prison_gate` 不允许被当前原型调用。

## 当前记忆

当前只做本局内存记忆，不写文件，也不做长期总结。

记忆事件示例：

```json
{
  "type": "player_asked_route",
  "content": "哪条路线最安全？"
}
```

## 演示命令

```powershell
D:\develop\pythons\.venv\Scripts\python.exe -m agent_workflow.cli
```

默认会询问：

```text
哪条路线最安全？
```

预期输出包含：

```text
回复：往前第二个口子跳下去有一条暗道，暗道内部只有一个站岗守卫。
工具：get_route_info
记忆数量：1
```

## FastAPI 最小接口

外部 FastAPI 项目位于 `D:\develop\pythons`。当前只新增一个最小接口：

```text
POST /agent/turn
```

请求示例：

```json
{
  "player_message": "哪条路线最安全？"
}
```

返回包含：

```json
{
  "reply": "...",
  "tool_calls": [],
  "memory": {},
  "game_state": {}
}
```

接口内部通过 lazy import 调用当前仓库的 `agent_workflow.prototype.run_agent_turn()`。这一版每次请求使用原型默认的本轮 `game_state` 和 `memory`，不做跨请求长期记忆。

## MCP 最小服务

当前 MCP 第一版不依赖外部 SDK，使用 stdio 上的 JSON-RPC 请求/响应实现最小可运行服务。

启动命令：

```powershell
D:\develop\pythons\.venv\Scripts\python.exe -m agent_workflow.mcp_server
```

当前支持的 MCP 方法：

| 方法 | 用途 |
| --- | --- |
| `initialize` | 返回服务信息和工具能力 |
| `tools/list` | 返回当前暴露的工具清单 |
| `tools/call` | 调用已允许的工具 |

当前暴露两个工具：

```text
get_route_info
check_game_state
```

MCP 客户端配置示例：

```text
agent_workflow/mcp_client_config.example.json
```

示例内容的核心是：

```json
{
  "command": "D:\\develop\\pythons\\.venv\\Scripts\\python.exe",
  "args": ["-m", "agent_workflow.mcp_server"],
  "cwd": "C:\\Users\\eurp\\Documents\\coedx_learning"
}
```

其中 `cwd` 表示从当前仓库根目录启动服务。这样 Python 才能找到 `agent_workflow.mcp_server` 这个模块。

工具参数示例：

```json
{
  "route_id": "secret_tunnel"
}
```

`check_game_state` 暂时不需要参数，会读取默认游戏状态，返回剩余时间、钥匙状态和任务提示。

如果请求 `open_prison_gate` 这类未授权工具，MCP 服务会返回 `isError: true`，并复用原型中的白名单拒绝逻辑。

### MCP 演示步骤

1. 把 `agent_workflow/mcp_client_config.example.json` 中的配置复制到支持 MCP 的客户端配置里。
2. 启动 MCP 客户端，让它加载 `coedx-agent-workflow` 服务。
3. 让客户端调用 `tools/list`，应看到 `get_route_info` 和 `check_game_state`。
4. 调用 `get_route_info`，参数传入 `{"route_id": "secret_tunnel"}`。
5. 预期返回下方暗道路线说明。
6. 调用 `check_game_state`，参数传入 `{}`。
7. 预期返回剩余时间、钥匙状态和任务提示。

## MCP 命令行演示

如果暂时不接真实 MCP 客户端，可以直接运行演示脚本：

```powershell
D:\develop\pythons\.venv\Scripts\python.exe -m agent_workflow.mcp_demo
```

演示脚本会在进程内模拟三次 MCP 请求：

1. `tools/list`
2. `tools/call get_route_info`
3. `tools/call check_game_state`

预期输出包含：

```text
MCP 工具列表：
- get_route_info
- check_game_state

路线工具结果：
下方暗道：往前第二个口子跳下去有一条暗道，暗道内部只有一个站岗守卫。

游戏状态工具结果：
{"ok": true, "remaining_time": 180, "has_key": false, "quest_hint": ""}
```

## 验证命令

```powershell
D:\develop\pythons\.venv\Scripts\python.exe -m unittest agent_workflow.tests.test_tool_calling_memory -v
D:\develop\pythons\.venv\Scripts\python.exe -m unittest agent_workflow.tests.test_mcp_server -v
D:\develop\pythons\.venv\Scripts\python.exe -m unittest agent_workflow.tests.test_mcp_demo -v
D:\develop\pythons\.venv\Scripts\python.exe -m agent_workflow.mcp_demo
D:\develop\pythons\.venv\Scripts\python.exe -m unittest test_api_rag.py -v
D:\develop\pythons\.venv\Scripts\python.exe -m json.tool agent_workflow/mcp_client_config.example.json
```

## 本阶段不做

- 不接真实 MCP Server。
- 不接 Unity。
- 不调用 DeepSeek。
- 不接 RAG。
- 不做长期记忆文件。
- 不做 LangGraph 或多 Agent。

这些内容属于后续阶段。当前阶段达到最小可行性后，应停止继续扩写本原型。
