# 《囚城营救》项目交接文档

## 2026-06-30 Level1 主演示实际录制已暂缓

- 用户明确选择跳过 `01_level1_overview.mp4` 的实际录制。
- 录制状态为“暂缓”，不是“已完成”。
- 保留 `docs/level1_overview_recording_checklist.md` 和预留文件名，当前不创建视频或占位文件。
- 下一步进入“多 Agent 游戏世界最小原型范围确认”，暂不接 Unity、LangGraph 或大模型。

## 2026-06-28 Unity Level1 主演示录屏前检查已完成

- 新增 `docs/level1_overview_recording_checklist.md`。
- `01_level1_overview.mp4` 只展示倒计时、玩家移动、敌人压力和路线选择。
- 胆小守卫 AI 对话和真路线闭环留给 `02_ai_guard_true_route.mp4`。
- 已确认 Unity 项目、`2022.3.62f3` 版本和 `Level1.unity` 仍然存在。
- 录屏只显示 Game 视图，不暴露桌面、本机路径、API Key 或调试窗口。
- 视频保存在本地 `portfolio_delivery/videos/`，不加入 Git。
- 下一步由用户按清单实际试录 `01_level1_overview.mp4`。

## 2026-06-28 外部 FastAPI 项目交付说明已整理

- 新增 `docs/external_fastapi_delivery.md`。
- 已核对 `D:\develop\pythons\api.py` 的 `/health`、`/npc/chat`、`/npc/world_qa` 和 `/agent/turn` 四个路由。
- 已记录外部 FastAPI 与当前仓库中 `ai_npc`、`rag` 和 `agent_workflow` 的依赖关系。
- 外部测试 7 项通过，实际启动 Uvicorn 后 `GET /health` 返回 HTTP `200`。
- 外部项目当前没有 `requirements.txt`、`pyproject.toml`、README 或 `.env.example`，尚不是可独立重建的完整交付包。
- 当前不迁移外部代码，不提交 `.venv`、`guard_state.json` 或 API Key。
- 下一步进入“Unity Level1 主演示录屏前最小检查”。

## 2026-06-27 录屏素材命名与交付目录已整理

- 新增 `portfolio_delivery/README.md`。
- 推荐本地使用 `videos/`、`screenshots/`和 `covers/` 三类素材目录。
- 8 条演示素材已按 `01` 到 `08` 统一命名，覆盖 Unity、AI NPC、RAG、关卡助手、Agent Workflow 和 MCP。
- 当前 Git 只跟踪目录说明，不提交视频大文件。
- 当前不创建 GitHub Release，等正式成片后再决定交付方式。
- 下一步进入“外部 FastAPI 项目交付说明最小整理”，暂不迁移代码。

## 2026-06-24 GitHub 页面确认与入口检查已完成

- GitHub 仓库页面：`https://github.com/liwuyue113-dotcom/1`
- 仓库为公开仓库，默认分支为 `master`。
- 页面检查时的远程提交为 `1701fade docs: record successful github push`。
- 远程 `README.md` 已存在，并作为作品集入口。
- 已新增 `docs/github_page_check.md`。
- README 的“下一步”已更新为录屏素材命名与作品集交付文件夹最小整理。
- 当前不继续打磨 GitHub 页面，不做 GitHub Pages，不创建 Releases。

## 2026-06-24 GitHub 首次推送已完成

- 用户已在本机 PowerShell 成功执行 `git push -u origin master`。
- 远程仓库：`https://github.com/liwuyue113-dotcom/1.git`。
- 当前分支：`master`。
- upstream：`origin/master`。
- 本地验证：`git status -sb` 显示 `## master...origin/master`。
- `tools/` 仍为未跟踪目录，暂不纳入作品集主线提交。
- 下一步建议只做 GitHub 页面确认与作品集展示入口检查，不继续打磨推送流程。

更新时间：2026-06-30

## 1. 项目目标

本项目是一个面向个人作品集的 Unity 2D 潜入营救游戏与 AI 游戏系统综合项目。

核心作品是《囚城营救》：玩家扮演姬野，潜入离国边境城堡，在倒计时结束前找到被俘的吕归尘。当前版本的通关条件是找到吕归尘，不包含后续护送和逃离玩法。

项目用于展示以下能力：

- 游戏策划与关卡设计。
- Unity 2D 游戏开发。
- AI NPC 与稳定游戏规则结合。
- RAG 世界观知识库与来源引用。
- AI 关卡设计助手。
- Tool Calling / Memory / Agent Workflow 原型。
- 后续多 Agent 游戏世界原型。

重要边界：

- 本项目是基于《九州缥缈录》原著人物与世界观的原创同人支线。
- 原著人物、势力与人物关系归原作者及相关权利方所有。
- 项目原创部分是潜入营救支线、关卡流程、AI NPC 机制、RAG 设定管理和技术实现。
- 不保存 API Key、密码或其他秘密。

## 2. 已完成功能

### 2.1 Unity 游戏基础

- 已有可运行的 Unity 2D 游戏版本。
- 已实现角色移动、战斗、敌人、基础关卡、UI、剧情和存档。
- Unity 版本已确认为 `2022.3.62f3`。
- 实际 Unity 项目位于 `D:\UnityProjects\project03`，不在当前仓库内。
- 当前仓库保存的是文档、Python 原型、RAG 代码、AI 关卡助手代码和阶段性 Unity 脚本副本。

### 2.2 胆小守卫 AI NPC 垂直切片

已完成一个可录制展示的 AI NPC 流程：

```text
玩家自由输入
-> DeepSeek 判断意图并生成角色台词
-> Python 规则系统更新信任和恐惧
-> Python 规则系统决定真实路线、虚假路线或拒绝透露
-> FastAPI 返回结构化 JSON
-> Unity 显示回复、情绪、路线提示和倒计时效果
```

已验证能力：

- 玩家可以与胆小守卫进行中文自由对话。
- DeepSeek 能识别 `comfort`、`threaten`、`ask_route`、`other`。
- Python 规则系统负责信任、恐惧、真假情报和历史状态。
- FastAPI 已提供 `GET /health` 与 `POST /npc/chat`。
- Unity 已通过 HTTP 调用 FastAPI。
- 首次对话只增加一次 20 秒。
- `true_route` 会提示：往前第二个口子跳下去有一条几乎无人镇守的暗道。
- `false_route` 会误导玩家往上走。
- 假情报可以在后续成功安抚后更正为真情报。
- 普通剧情 NPC 不受 AI 守卫系统影响。

### 2.3 RAG 游戏设定知识库

已完成本地 RAG 最小可用版本：

- `docs/rag_setting.md` 保存已确认设定。
- 使用 `BAAI/bge-small-zh-v1.5` 中文 Embedding。
- 使用 NumPy 向量索引。
- 支持 Top 3 检索、来源引用和证据不足拒答。
- 已验证三条路线、敌人分布、巡逻方式、隐藏暗道和剧情设定的检索。
- 当前 RAG 默认只索引已确认设定，不把进度文档、交接文档或临时讨论加入索引。

已验证命令：

```powershell
D:\develop\pythons\.venv\Scripts\python.exe -m unittest discover -s rag/tests -v
```

最近一次验证结果：31 项测试通过。

### 2.4 AI 关卡设计助手

已完成命令行 MVP：

- 本地模板生成固定结构的关卡策划案。
- DeepSeek 接入，未配置 API Key 或调用失败时回退本地模板。
- RAG 接入，为关卡设计提供已确认设定依据。
- 质量评价规则，检查玩家目标、三条路线、风险收益和失败条件。
- JSON 输出，便于未来网页或 Unity 工具读取。

当前原则：

- DeepSeek 只生成策划文本，不直接修改关卡。
- RAG 只提供事实依据，不直接生成策划案。
- 质量评价只做最低结构检查，不代替人工策划判断。
- 当前阶段已经达到最小可行性，不继续打磨关卡助手。

### 2.5 RAG 接入 AI NPC / 外部 FastAPI

已完成：

- 当前仓库新增 `ai_npc.rag_context`。
- 外部 FastAPI 项目 `D:\develop\pythons` 新增 `POST /npc/world_qa`。
- `/npc/world_qa` 通过 lazy import 引用当前仓库代码。
- 没有修改现有 `/npc/chat`。
- 没有影响 Unity 当前胆小守卫真假路线流程。
- 新增 `world_qa_demo.py`，可以不用 Unity 演示 RAG 世界观问答。

实际演示结果：

```text
问题：真正安全的路线在哪里？
回答：未调用 DeepSeek。最相关设定片段：胆小守卫提供的真实安全路线是：往前第二个口子跳下去有一条暗道，几乎无人镇守。这条路线可以帮助玩家绕过守卫巡逻。
是否使用 RAG：是
来源：docs/rag_setting.md
```

### 2.6 Tool Calling / Memory 最小原型

已完成本地 Python 原型：

- 新增 `agent_workflow` 包。
- Agent 只能调用白名单工具。
- 未授权工具会被拒绝。
- 工具调用可以读取或更新受控游戏状态字段。
- 玩家关键行为会写入本局内存记忆。
- 提供命令行演示。

当前白名单工具：

| 工具 | 用途 |
| --- | --- |
| `get_route_info` | 查询上路、中路或下方暗道的基础路线设定 |
| `check_game_state` | 读取剩余时间、钥匙状态和当前任务提示 |
| `update_quest_hint` | 更新任务提示文本 |

当前阶段不做：

- 不接真实 MCP Server。
- 不接 Unity。
- 不调用 DeepSeek。
- 不接 RAG。
- 不做长期记忆文件。
- 不做 LangGraph 或多 Agent。

已验证命令：

```powershell
D:\develop\pythons\.venv\Scripts\python.exe -m unittest discover -s agent_workflow/tests -v
D:\develop\pythons\.venv\Scripts\python.exe -m agent_workflow.cli
```

最近一次验证结果：4 项测试通过，CLI 能输出路线回复、工具名 `get_route_info` 和记忆数量。

### 2.7 Agent Workflow 接入外部 FastAPI

已完成最小 HTTP 接口：

- 外部 FastAPI 项目 `D:\develop\pythons` 新增 `POST /agent/turn`。
- 接口接收 `player_message`。
- 接口通过 lazy import 调用当前仓库的 `agent_workflow.prototype.run_agent_turn()`。
- 返回 `reply`、`tool_calls`、`memory` 和 `game_state`。
- 没有修改现有 `/npc/chat`。
- 没有修改现有 `/npc/world_qa`。
- 没有接 Unity、真实 MCP、LangGraph 或长期记忆。

已验证命令：

```powershell
D:\develop\pythons\.venv\Scripts\python.exe -m unittest test_api_rag.py -v
```

最近一次验证结果：4 项测试通过，覆盖 `/health`、`/npc/chat`、`/npc/world_qa` 和 `/agent/turn`。

### 2.8 真实 MCP 最小服务

已完成 MCP 风格的最小 stdio JSON-RPC 服务：

- 新增 `agent_workflow/mcp_server.py`。
- 支持 `initialize`，返回 MCP 协议版本、工具能力和服务信息。
- 支持 `tools/list`，列出当前暴露的工具。
- 支持 `tools/call`，调用 `get_route_info`。
- 复用现有 `agent_workflow.prototype.call_tool()` 白名单逻辑。
- 未授权工具会返回 `isError: true`，例如 `open_prison_gate`。
- 已处理 Windows 管道可能带来的 BOM 或前缀字符问题。
- 当前没有安装或依赖外部 `mcp` SDK。
- 不接 Unity、不接 LangGraph、不做长期记忆。

已验证命令：

```powershell
D:\develop\pythons\.venv\Scripts\python.exe -m unittest agent_workflow.tests.test_mcp_server -v
```

最近一次验证结果：8 项测试通过，覆盖初始化、工具列表、工具调用、未知工具拒绝、单行 JSON-RPC 处理、多请求 stdio 输出和 Windows 管道前缀兼容。

### 2.9 MCP 服务启动说明与配置示例

已完成：

- 新增 `agent_workflow/mcp_client_config.example.json`。
- 配置示例使用 `D:\develop\pythons\.venv\Scripts\python.exe` 启动。
- 配置示例参数为 `-m agent_workflow.mcp_server`。
- 配置示例包含 `cwd`，指向 `C:\Users\eurp\Documents\coedx_learning`。
- `docs/agent_workflow.md` 已补充 MCP 客户端配置示例和演示步骤。
- 当前没有直接修改任何真实 MCP 客户端配置。

已验证命令：

```powershell
D:\develop\pythons\.venv\Scripts\python.exe -m json.tool agent_workflow/mcp_client_config.example.json
D:\develop\pythons\.venv\Scripts\python.exe -m unittest discover -s agent_workflow/tests -v
```

最近一次验证结果：配置示例 JSON 合法，Agent Workflow 测试 12 项通过。

### 2.10 MCP 第二个只读工具 check_game_state

已完成：

- `agent_workflow/mcp_server.py` 新增 `check_game_state` 工具声明。
- `tools/list` 现在返回 `get_route_info` 和 `check_game_state`。
- `tools/call` 可以调用 `check_game_state`。
- `check_game_state` 不需要参数，使用 `{}` 即可。
- `check_game_state` 返回默认游戏状态，包括 `remaining_time`、`has_key` 和 `quest_hint`。
- 当前仍然不暴露 `update_quest_hint`，避免 MCP 客户端过早修改任务状态。

已验证命令：

```powershell
D:\develop\pythons\.venv\Scripts\python.exe -m unittest agent_workflow.tests.test_mcp_server -v
```

最近一次验证结果：9 项测试通过，覆盖两个工具的列表展示、路线工具调用、状态工具调用、未知工具拒绝和 stdio 处理。

### 2.11 MCP 命令行演示脚本

已完成：

- 新增 `agent_workflow/mcp_demo.py`。
- 新增 `agent_workflow/tests/test_mcp_demo.py`。
- 演示脚本在进程内模拟 MCP 请求，不需要真实 MCP 客户端。
- 演示 `tools/list`，输出 `get_route_info` 和 `check_game_state`。
- 演示 `tools/call get_route_info`，输出下方暗道路线。
- 演示 `tools/call check_game_state`，输出默认游戏状态。
- `docs/agent_workflow.md` 已补充演示命令和预期输出。

已验证命令：

```powershell
D:\develop\pythons\.venv\Scripts\python.exe -m unittest agent_workflow.tests.test_mcp_demo -v
D:\develop\pythons\.venv\Scripts\python.exe -m agent_workflow.mcp_demo
```

最近一次验证结果：演示脚本测试 3 项通过，实际命令能输出工具列表、路线工具结果和游戏状态工具结果。

### 2.12 Agent Workflow 阶段作用说明

已完成：

- 新增 `docs/agent_workflow_stage_roles.md`。
- 说明 Tool Calling / Memory 本地原型、命令行演示、FastAPI 接口、MCP 服务、MCP 配置示例、MCP 只读状态工具和 MCP 演示脚本分别解决什么问题。
- 每个阶段都补充了对应游戏意义和作品集讲法。
- `docs/agent_workflow.md` 已链接到该说明文档。

用途：

- 用于作品集录屏、答辩和面试讲解。
- 帮助解释为什么 AI 不能直接改游戏状态，只能调用白名单工具。
- 帮助解释为什么当前阶段不继续接 Unity、LangGraph 或长期记忆。

### 2.13 RAG 设定冲突检查器最小原型

已完成：

- 新增 `rag/conflict_checker.py`。
- 新增 `rag/check_conflict.py`。
- 新增 `rag/tests/test_conflict_checker.py`。
- 复用现有 RAG 索引检索相关旧设定。
- 第一版能识别明显的守卫数量冲突，例如“下方暗道只有一个守卫”和“下方暗道有多个守卫”。
- 命令行输出结论、冲突原因、来源和相关设定片段。

演示命令：

```powershell
D:\develop\pythons\.venv\Scripts\python.exe -m rag.check_conflict "新增设定：下方暗道内部有多个守卫来回巡逻。"
```

当前边界：

- 不接 Unity。
- 不调用 DeepSeek。
- 不自动修改 `docs/rag_setting.md`。
- 不替代人工策划判断，只做新增设定前的提醒工具。

### 2.14 RAG 冲突检查器作品集演示说明

已完成：

- 新增 `docs/rag_conflict_checker_demo.md`。
- 说明冲突检查器解决的问题。
- 补充演示命令、预期输出重点、录屏讲解顺序和面试讲法。
- 明确当前边界：不自动改设定、不替代人工策划判断、不接 Unity。
- `docs/rag.md` 和 `rag/README.md` 已链接到该说明文档。

用途：

- 用于作品集录屏。
- 用于答辩或面试解释 RAG 不只是问答，也可以辅助维护设定一致性。
- 用于说明为什么第一版先用规则判断，而不是让大模型直接审稿。

### 2.15 Unity Level1 三路线一致性静态核对

已完成：

- 新增 `docs/unity_level1_route_audit.md`。
- 静态读取实际 Unity 工程 `D:\UnityProjects\project03`。
- 确认 Unity 版本为 `2022.3.62f3`。
- 确认 `Level1.unity` 存在。
- 确认 Level1 中存在 `AIguard`、`AIGuardDialogueSystem`、`AIGuardInteractionZone` 和 `Route Hint Text`。
- 静态读取到 25 个 `Enemy` 对象。
- 下方层级 y 约为 `-37` 的位置有 `Enemy (3)`、`Enemy (4)`、`Enemy (6)` 三个敌人。

当前结论：

- 不能仅凭 YAML 判定这 3 个敌人都在下方暗道内部。
- 但这已经足够作为下一阶段 Unity 编辑器复核目标。
- 如果它们都在暗道可用路径内，就与“暗道内部只有一个站岗守卫”的设定冲突。
- 如果只有 1 个在暗道内部，其他属于下方普通区域，则不用改场景，只需在文档中标清归属。

## 3. 当前正在做什么

当前最新决定：`01_level1_overview.mp4` 实际录制已暂缓。

当前不要继续要求用户录制 `01` 视频，也不要将未录制素材写成已完成。

下一步建议：

进入“多 Agent 游戏世界最小原型范围确认”，只定义两个 Agent、最少共享世界状态、白名单行为和禁止行为。

## 4. 修改过哪些文件

### 4.1 项目规则与知识库

- `AGENTS.md`
- `agent.md`
- `HANDOVER.md`
- `docs/project_context.md`
- `docs/progress.md`
- `docs/game_design.md`
- `docs/tech_decision.md`
- `docs/coding_rules.md`
- `docs/ai_npc.md`
- `docs/agent_workflow.md`
- `docs/agent_workflow_stage_roles.md`
- `docs/rag_conflict_checker_demo.md`
- `docs/unity_level1_route_audit.md`
- `docs/staged_roadmap.md`
- `docs/level_designer.md`
- `docs/rag.md`
- `docs/rag_setting.md`

### 4.2 RAG 代码

- `rag/__init__.py`
- `rag/rag_config.py`
- `rag/document_loader.py`
- `rag/embedding_service.py`
- `rag/vector_store.py`
- `rag/build_index.py`
- `rag/answer_service.py`
- `rag/ask.py`
- `rag/conflict_checker.py`
- `rag/check_conflict.py`
- `rag/README.md`
- `rag/requirements.txt`
- `rag/tests/test_document_loader.py`
- `rag/tests/test_embedding_service.py`
- `rag/tests/test_vector_store.py`
- `rag/tests/test_answer_service.py`
- `rag/tests/test_rag_acceptance.py`
- `rag/tests/test_conflict_checker.py`
- `rag/tests/fixtures/`

生成索引位于 `rag/rag_data/`，该目录属于可重新生成数据，已被 `.gitignore` 忽略。

### 4.3 AI 关卡设计助手代码

- `level_designer/__init__.py`
- `level_designer/generator.py`
- `level_designer/deepseek_client.py`
- `level_designer/rag_context.py`
- `level_designer/evaluator.py`
- `level_designer/json_output.py`
- `level_designer/cli.py`
- `level_designer/tests/test_generator.py`

### 4.4 AI NPC RAG 适配层代码

- `ai_npc/__init__.py`
- `ai_npc/rag_context.py`
- `ai_npc/tests/test_rag_context.py`

### 4.5 Agent Workflow 最小原型代码

- `agent_workflow/__init__.py`
- `agent_workflow/prototype.py`
- `agent_workflow/cli.py`
- `agent_workflow/mcp_server.py`
- `agent_workflow/mcp_demo.py`
- `agent_workflow/mcp_client_config.example.json`
- `agent_workflow/tests/test_tool_calling_memory.py`
- `agent_workflow/tests/test_mcp_server.py`
- `agent_workflow/tests/test_mcp_demo.py`

### 4.6 Unity 阶段脚本副本

当前仓库内保存了以下 Unity 脚本副本：

- `stage5/AIGuardApiClientTests.cs`
- `stage5/AIGuardApiTest.cs`
- `stage6/AIGuardDialogueUI.cs`
- `stage6/AIGuardDialogueUITests.cs`
- `stage7/AIGuardGameplayEffects.cs`
- `stage7/AIGuardGameplayEffectsTests.cs`
- `stage7/AIGuardGameplayRules.cs`
- `stage8/AIGuardInteractionZone.cs`
- `stage8/AIGuardInteractionZoneTests.cs`
- `stage8/AIGuardNpcOnly.cs`

Unity 实际项目状态必须到 `D:\UnityProjects\project03` 内重新确认。

### 4.7 外部 AI NPC Python / FastAPI 项目

外部项目位置：

```text
D:\develop\pythons
```

已知关键文件：

- `D:\develop\pythons\save_guard.py`
- `D:\develop\pythons\api.py`
- `D:\develop\pythons\guard_state.json`
- `D:\develop\pythons\test_api_rag.py`
- `D:\develop\pythons\world_qa_demo.py`
- `D:\develop\pythons\test_world_qa_demo.py`
- `D:\develop\pythons\.venv\Scripts\python.exe`

该目录不属于当前 Git 仓库，接手时必须以实际文件为准。

## 5. 关键架构

### 5.1 总体职责边界

- Unity 负责可信游戏状态、UI、计时器、场景对象和游戏效果。
- FastAPI 负责提供本地 HTTP 接口，连接 Unity、Python 规则、模型和 RAG。
- DeepSeek 负责语言理解和角色台词生成。
- Python 规则系统负责信任、恐惧、真假情报等稳定玩法规则。
- RAG 负责提供可追溯来源的设定事实，不直接改游戏状态。
- Agent Workflow 负责受限制的工具调用和记忆流程，不直接绕过规则系统。

### 5.2 胆小守卫 AI NPC 架构

```text
Unity 输入 / UI
-> FastAPI /npc/chat
-> DeepSeek 意图识别
-> Python 规则系统
-> DeepSeek 角色台词生成
-> Python 输出验证
-> FastAPI 返回 JSON
-> Unity 执行情绪、加时和路线提示
```

核心规则：

```text
安抚守卫：信任 +20，恐惧 -15
威胁守卫：信任 -15，恐惧 +15
询问路线：
  信任 >= 50 且 信任 >= 恐惧 -> true_route
  恐惧 >= 信任 + 30 -> false_route
  其他 -> none
```

### 5.3 RAG 架构

索引构建：

```text
docs/rag_setting.md
-> Markdown 切片
-> build_embedding_text(chunk)
-> BAAI/bge-small-zh-v1.5
-> embeddings.npy + chunks.json
```

问答流程：

```text
玩家问题
-> 问题 Embedding
-> 余弦相似度 Top 3
-> answer_question()
-> DeepSeek 有依据回答或本地拒答
-> 来源文档与检索片段展示
```

冲突检查流程：

```text
新增候选设定
-> 候选设定 Embedding
-> 余弦相似度 Top 3
-> check_setting_conflict()
-> 规则判断明显冲突
-> 输出结论、原因、来源和相关片段
```

### 5.4 AI 关卡设计助手架构

```text
命令行参数
-> LevelDesignInput
-> provider 判断
-> use_rag: retrieve_rag_context()
-> template: generate_level_plan()
-> deepseek: DeepSeekClient -> AI Markdown 策划案
-> evaluate: evaluate_level_plan()
-> format=json: build_json_output()
```

### 5.5 Agent Workflow 最小原型架构

```text
玩家输入
-> FastAPI /agent/turn 或本地 CLI
-> run_agent_turn()
-> 判断是否需要工具
-> call_tool() 白名单校验
-> 工具返回受控结果
-> record_memory() 写入本局记忆
-> 返回 reply、tool_calls、memory、game_state
```

MCP 最小服务流程：

```text
MCP Client
-> stdio JSON-RPC
-> agent_workflow.mcp_server
-> tools/list 查看 get_route_info
-> tools/call 调用 get_route_info
-> call_tool() 白名单校验
-> 返回 MCP content 文本或 isError
```

当前白名单工具：

- `get_route_info`
- `check_game_state`
- `update_quest_hint`

当前 MCP 暴露工具：

- `get_route_info`
- `check_game_state`

## 6. 已知问题

1. Unity 实际项目不在当前仓库内，任何 Unity 相关修改都必须去 `D:\UnityProjects\project03` 重新确认代码和场景。
2. 外部 FastAPI 项目不在当前仓库内，文档中的外部文件状态可能过期，接手时必须重新读取 `D:\develop\pythons`。
3. 当前 Git 仓库尚无提交记录，许多文件处于未跟踪状态。首次提交前必须检查 `.gitignore`、索引文件、缓存文件和秘密信息。
4. 用户曾在截图中暴露过 DeepSeek API Key。不要复用截图中的 Key，不要把任何 API Key 写入仓库或文档。
5. RAG 必须使用安装了 `sentence-transformers` 的虚拟环境运行，推荐 Python 路径为 `D:\develop\pythons\.venv\Scripts\python.exe`。
6. 如果误用其他 Python，程序可能回退到本地文本向量，导致与 512 维 BGE 索引不匹配。
7. Unity 退出并重新进入 Play 模式后，Python 侧可能继续读取上一局 `guard_state.json`，导致信任、恐惧、情绪和历史没有重置。后续可增加重置接口。
8. “真实情报削弱指定守卫血量”的玩法效果已确认后期再做，目前没有实现。
9. `Level1.unity` 静态读取曾发现下方区域存在 `Enemy (3)`、`Enemy (4)`、`Enemy (6)`。用户已在 Unity 编辑器人工确认：这 3 个敌人都在暗道内部陷阱里，不会出来，不按“暗道可走路径上的站岗守卫”计算。当前不需要移动或删除它们。
10. `docs/unity_level1_route_experience_audit.md` 已记录 Level1 路线整体体验复核。用户已确认：上路明显更绕或更耗时，中路更容易看到密集守卫或形成集中压力，下方暗道入口默认不明显但听到“往前第二个口子跳下去”后能找到。当前不继续打磨路线整体体验。
11. `docs/ai_guard_route_recording_checklist.md` 已记录 AI 守卫路线提示录屏最小复核清单。用户已试跑并确认：可以从胆小守卫真实情报顺利走到下方暗道入口。当前不继续打磨该录屏链路。
12. `docs/portfolio_delivery_checklist.md` 已整理当前可展示模块和推荐录屏顺序；`portfolio_delivery/README.md` 已统一 8 条素材的命名和存放规则。下一步应进入外部 FastAPI 项目交付说明最小整理。
13. 根目录 `README.md` 已新增，作为作品集入口，说明项目定位、可展示模块、录屏顺序、外部路径、关键文档和当前边界。
14. `docs/pre_commit_cleanup_check.md` 已记录提交前最小检查。`.gitignore` 已补充 `.env`、虚拟环境、`tmp/`、`output/`、Unity 生成目录、日志和常见缓存目录。尚未做正式 Git 提交。
15. `docs/first_commit_scope.md` 已记录第一次提交范围建议。建议提交根目录入口与规则文件、`docs/`、`rag/`、`ai_npc/`、`agent_workflow/`、`level_designer/`、`stage5` 到 `stage8`；建议暂不提交 `tools/`。
16. 当前 `/npc/world_qa` 没有接 Unity UI，Unity 仍只使用 `/npc/chat`。
17. 当前 `agent_workflow` 已有本地 Python 原型、外部 FastAPI 最小接口、MCP stdio 最小服务和阶段作用说明；MCP 当前暴露 `get_route_info` 和 `check_game_state`，不接 Unity，不接长期记忆。
18. 当前 RAG 冲突检查器只覆盖最明显的规则冲突，不代表完整剧情审稿。
19. 同人作品存在 IP 展示边界风险，作品集表达时应说明原著来源，并突出自己的原创支线设计、玩法实现和 AI 系统能力。

## 7. 下一步开发计划

### 7.1 可选后续扩展：RAG 设定冲突检查器

目标：

```text
扩展当前冲突检查器，让它覆盖更多设定冲突类型。
```

后续可扩展方向：

- 路线长度冲突，例如“上路较长”和“上路很短”。
- 入口可见性冲突，例如“下方暗道默认明显”和“下方暗道默认不明显”。
- 任务流程冲突，例如“找到吕归尘后必须护送逃离”和“当前版本找到吕归尘即通关”。
- 第一版 MVP 已完成，后续扩展不应阻塞进入新阶段。

### 7.2 可选下一阶段：真实 MCP 最小服务

目标：

```text
把当前白名单工具思想扩展成真实 MCP 服务的最低可用版本。
```

最低可用标准：

- 当前 MCP 已暴露 `get_route_info` 和 `check_game_state` 两个只读工具。
- 保持工具白名单边界。
- 不接 Unity。
- 不接 LangGraph。
- 不做复杂长期记忆。

### 7.3 可选下一阶段：Unity 关卡打磨

如果用户选择回到 Unity，下一步应进入：

- 优先进入第一次提交执行前确认。
- 只确认是否按 `docs/first_commit_scope.md` 的范围执行 `git add` 和 `git commit`。
- 不要继续打磨路线长度、敌人数量、入口表现或真路线录屏链路。
- `Enemy (3)`、`Enemy (4)`、`Enemy (6)` 已确认是陷阱内不会出来的敌人，当前不作为待调整问题。
- 不要直接手改 `.unity` YAML，优先在 Unity 编辑器中调整。

### 7.4 后续长期计划

- 扩展 RAG 设定冲突检查器的更多规则，或整理成作品集演示说明。
- 将 Agent Workflow 扩展成真实 MCP 最小服务。
- 修复 Unity 新一局开始时 AI 守卫状态不重置的问题。
- 后期实现真实情报削弱指定守卫血量或降低巡逻威胁。
- 将 AI 关卡设计助手接入当前关卡和路线设计案例。
- 后续再扩充姬野、吕归尘、胆小守卫、离国军守卫的角色设定。
- 后续再扩充边境城堡地图结构、巡逻路线、暗道、牢房和转移路线。
- LangGraph 与多 Agent 游戏世界放到更后面，不要提前做。

## 8. 接手提醒

- 先读 `AGENTS.md`，再读 `docs/project_context.md`、`docs/progress.md`、`agent.md`。
- 当前代码、场景和实际运行结果优先级高于旧文档。
- 阶段式推进：每轮只做当前阶段最低可用版本，不提前堆高级架构。
- 一旦某阶段达到最小可行性，必须停止继续补充、打磨或扩写该阶段。
- 用户是以作品集为目标的数字媒体技术学生，回复时要边做边教，但一次只讲一个小知识点。
- 每次教学回复必须说明当前阶段、本阶段目标、是否完成、下一步和本次修改文件。
- 完成功能或重要设定变更后，同步更新 `docs/progress.md` 和直接相关设计文档。
## 10. 2026-06-24 GitHub 推送状态（历史记录）

- 用户提供的 GitHub 仓库地址为 `https://github.com/liwuyue113-dotcom/1.git`。
- 当前仓库已配置 remote：`origin -> https://github.com/liwuyue113-dotcom/1.git`。
- 用户已成功执行 `git push -u origin master`。
- 后续文档提交 `1701fad docs: record successful github push` 也已推送到 `origin/master`。
- 当前工作区仍只有 `tools/` 未跟踪。
- 当前不需要继续打磨推送流程。

## 9. 2026-06-24 最新接手补充

### 9.1 第一次本地提交

- 第一次本地 Git 提交已完成。
- 第一次本地提交：`f9ea39e chore: initialize portfolio project workspace`。
- 提交范围包含项目入口文档、`docs/`、`rag/`、`ai_npc/`、`agent_workflow/`、`level_designer/` 和 `stage5` 到 `stage8`。
- `tools/` 仍然未跟踪，暂不纳入《囚城营救》AI 游戏作品集主线提交。

### 9.2 GitHub 推送前状态（历史记录）

- 当前分支：`master`。
- 当前远程仓库为 `origin -> https://github.com/liwuyue113-dotcom/1.git`。
- 新增 `docs/github_push_precheck.md` 记录推送前最小检查。
- GitHub 首次推送已完成，仓库为公开仓库，默认分支为 `master`。
