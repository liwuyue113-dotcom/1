# 《囚城营救》项目交接文档

最后更新：2026-06-30

本文是给下一个 AI 的当前状态快照。接手时先按顺序阅读：

1. `AGENTS.md`
2. `docs/project_context.md`
3. `docs/progress.md`
4. `agent.md`
5. 与当前任务直接相关的设计文档

当文档与实际代码、Unity 场景或当前运行结果冲突时，以实际结果为准，并同步修正文档。

## 1. 项目目标

本项目是一个以 Unity 2D 潜入营救游戏《囚城营救》为核心的个人作品集项目。

游戏中，玩家扮演姬野，需要在倒计时结束前潜入离国边境城堡并找到被俘的吕归尘。当前通关条件是“找到吕归尘”，不包含护送和逃离玩法。

作品集目标是同时展示：

- 游戏策划、三路线关卡和 Unity 2D 开发能力。
- AI NPC 如何影响真实游戏机制，而不是只做聊天。
- RAG 如何管理游戏世界观、引用来源并检查设定冲突。
- AI 关卡设计助手如何生成和评价结构化策划案。
- Tool Calling、Memory、MCP 和 Agent Workflow 如何限制 AI 的可执行行为。
- 后续如何扩展到受规则约束的多 Agent 游戏世界。

目标岗位包括游戏策划、AI 技术策划、AI 游戏设计师、Agent 游戏开发和剧情叙事策划。

项目是基于《九州缥缈录》人物与世界观创作的原创同人支线。潜入营救关卡、三路线玩法、AI NPC、RAG 设定管理和技术实现属于项目原创内容；原著人物、势力和世界观归原作者及相关权利方所有。

## 2. 已完成功能

### 2.1 Unity 游戏与 Level1

- 已有可运行的 Unity 2D 游戏版本。
- 已实现玩家移动、战斗、敌人、基础关卡、UI、剧情、存档和倒计时。
- Unity 版本已确认为 `2022.3.62f3`。
- Level1 已具备上路、中路和下方暗道三条路线。
- 用户已实测确认：上路更绕或更耗时，中路守卫压力更集中，暗道入口默认不明显但获得真实情报后可以找到。
- `Enemy (3)`、`Enemy (4)`、`Enemy (6)` 已人工确认位于暗道陷阱内且不会出来，不计入可走路径上的站岗守卫数量。

### 2.2 胆小守卫 AI NPC 垂直切片

已完成的运行链路：

```text
玩家自由输入
-> DeepSeek 判断意图并生成角色台词
-> Python 规则系统更新信任、恐惧和情报结果
-> FastAPI 返回结构化 JSON
-> Unity 显示对话、情绪、加时和路线提示
```

已验证：

- 意图支持 `comfort`、`threaten`、`ask_route`、`other`。
- 安抚会提高信任、降低恐惧；威胁会降低信任、提高恐惧。
- Python 规则而不是大模型决定 `true_route`、`false_route` 或 `none`。
- 真情报提示“往前第二个口子跳下去有一条暗道”；假情报误导玩家往上走。
- 首次成功对话只增加一次 20 秒。
- 假情报可以在后续成功安抚后更正为真情报。
- AI 对话 UI 会在玩家靠近时显示、远离时隐藏，普通剧情 NPC 不受影响。
- 真路线流程已试跑通过，可以从守卫情报找到暗道入口。

### 2.3 RAG 游戏设定知识库

- `docs/rag_setting.md` 保存已确认的角色、剧情和三路线设定。
- 使用 `BAAI/bge-small-zh-v1.5` 中文 Embedding 和 NumPy 向量索引。
- 支持 Markdown 切片、Top 3 检索、来源引用和证据不足时拒绝编造。
- 默认只索引专用已确认设定，不把进度、交接或临时文档当作世界观事实。
- 已完成 AI NPC RAG 适配层和外部 FastAPI `POST /npc/world_qa`。
- 已完成设定冲突检查器最小原型，可识别守卫数量等明显冲突并输出来源。

### 2.4 AI 关卡设计助手

- 提供 `python -m level_designer.cli` 命令行入口。
- 本地模板可生成固定结构的三路线关卡策划案。
- `--provider deepseek` 支持 DeepSeek，缺少 API Key 或调用失败时回退本地模板。
- `--use-rag` 将检索到的已确认设定作为生成依据。
- `--evaluate` 检查玩家目标、三路线、风险收益和失败条件。
- `--format json` 输出输入、Markdown 策划案、评价结果和回退提示。
- DeepSeek 只生成策划文本，不直接修改 Unity 关卡。

### 2.5 Tool Calling、Memory、Agent Workflow 与 MCP

- `agent_workflow` 已实现本地 Python 原型和命令行演示。
- 白名单工具为 `get_route_info`、`check_game_state`、`update_quest_hint`。
- 未授权工具会被拒绝，例如 `open_prison_gate`。
- 玩家询问路线、任务或发送其他消息时，关键行为会写入本局 Memory。
- 外部 FastAPI 已提供 `POST /agent/turn`。
- MCP stdio JSON-RPC 服务已支持 `initialize`、`tools/list` 和 `tools/call`。
- MCP 当前只暴露 `get_route_info` 和 `check_game_state` 两个只读工具，暂不暴露 `update_quest_hint`。
- `agent_workflow/mcp_demo.py` 可以不依赖真实 MCP 客户端展示工具列表和调用。
- `agent_workflow/mcp_client_config.example.json` 提供客户端启动配置示例。

### 2.6 外部 FastAPI 与作品集交付

- 外部 FastAPI 已提供 `GET /health`、`POST /npc/chat`、`POST /npc/world_qa` 和 `POST /agent/turn`。
- `docs/external_fastapi_delivery.md` 已说明外部项目与当前仓库的关系、必需文件、环境变量和启动步骤。
- 根目录 `README.md` 已作为作品集入口。
- `portfolio_delivery/README.md` 已统一 8 条录屏素材的命名和存放规则。
- `01_level1_overview.mp4` 的检查清单已完成，但用户于 2026-06-30 选择暂缓实际录制；状态不得写成“已完成”。
- GitHub 公开仓库为 `https://github.com/liwuyue113-dotcom/1`，默认分支为 `master`。

### 2.7 2026-06-30 新鲜验证结果

```text
rag/tests                 35 项通过
ai_npc/tests               4 项通过
level_designer/tests      18 项通过
agent_workflow/tests      16 项通过
外部 FastAPI 测试          7 项通过
```

外部 FastAPI 测试会显示 `StarletteDeprecationWarning`，但当前 7 项测试仍全部通过。

对应验证命令：

```powershell
D:\develop\pythons\.venv\Scripts\python.exe -m unittest discover -s rag/tests -v
D:\develop\pythons\.venv\Scripts\python.exe -m unittest discover -s ai_npc/tests -v
D:\develop\pythons\.venv\Scripts\python.exe -m unittest discover -s level_designer/tests -v
D:\develop\pythons\.venv\Scripts\python.exe -m unittest discover -s agent_workflow/tests -v

cd D:\develop\pythons
D:\develop\pythons\.venv\Scripts\python.exe -m unittest test_api_rag.py test_world_qa_demo.py -v
```

## 3. 当前正在做什么

当前已完成 AI NPC、RAG、AI 关卡设计助手、Tool Calling / Memory 和 MCP 的最小原型。

当前不再要求用户录制 `01_level1_overview.mp4`，也不应继续打磨已达到最小可行度的局部原型。

当前下一阶段是：

```text
多 Agent 游戏世界最小原型范围确认
```

这一阶段只需确认：

- 第一版使用哪两个 Agent。
- 两个 Agent 共享哪些最少世界状态。
- Agent 可以申请调用哪些白名单行为。
- Agent 不得直接修改哪些游戏状态。

当前不实现 Unity 接入、LangGraph、大模型调用、长期记忆或复杂多 Agent 协商。

当前 Git 状态：

- 分支：`master`
- 远程：`origin -> https://github.com/liwuyue113-dotcom/1.git`
- 重写本文前的最新提交：`a1ca94a docs: defer level1 overview recording`
- 本地 `master` 与 `origin/master` 同步。
- `tools/` 仍为未跟踪目录，不属于当前游戏作品集主线，不要自动加入提交。

## 4. 修改过哪些文件

以下是下一个 AI 最需要知道的已跟踪文件和目录。完整历史以 `git log --stat` 和 `git ls-files` 为准。

### 4.1 根目录与知识库

- `.gitignore`
- `AGENTS.md`
- `agent.md`
- `README.md`
- `HANDOVER.md`
- `portfolio_delivery/README.md`
- `docs/project_context.md`
- `docs/progress.md`
- `docs/staged_roadmap.md`
- `docs/game_design.md`
- `docs/tech_decision.md`
- `docs/coding_rules.md`
- `docs/ai_npc.md`
- `docs/rag.md`
- `docs/rag_setting.md`
- `docs/rag_conflict_checker_demo.md`
- `docs/level_designer.md`
- `docs/agent_workflow.md`
- `docs/agent_workflow_stage_roles.md`
- `docs/external_fastapi_delivery.md`
- `docs/portfolio_delivery_checklist.md`
- `docs/ai_guard_route_recording_checklist.md`
- `docs/level1_overview_recording_checklist.md`
- `docs/unity_level1_route_audit.md`
- `docs/unity_level1_route_experience_audit.md`
- `docs/pre_commit_cleanup_check.md`
- `docs/first_commit_scope.md`
- `docs/github_push_precheck.md`
- `docs/github_page_check.md`
- `docs/superpowers/specs/`
- `docs/superpowers/plans/`

### 4.2 RAG 与 AI NPC 适配层

- `rag/answer_service.py`
- `rag/ask.py`
- `rag/build_index.py`
- `rag/check_conflict.py`
- `rag/conflict_checker.py`
- `rag/document_loader.py`
- `rag/embedding_service.py`
- `rag/rag_config.py`
- `rag/vector_store.py`
- `rag/requirements.txt`
- `rag/tests/`
- `ai_npc/rag_context.py`
- `ai_npc/tests/`

`rag/rag_data/` 是可重新生成的索引目录，已由 `.gitignore` 忽略。

### 4.3 AI 关卡设计助手

- `level_designer/cli.py`
- `level_designer/deepseek_client.py`
- `level_designer/evaluator.py`
- `level_designer/generator.py`
- `level_designer/json_output.py`
- `level_designer/rag_context.py`
- `level_designer/tests/`

### 4.4 Agent Workflow 与 MCP

- `agent_workflow/prototype.py`
- `agent_workflow/cli.py`
- `agent_workflow/mcp_server.py`
- `agent_workflow/mcp_demo.py`
- `agent_workflow/mcp_client_config.example.json`
- `agent_workflow/tests/`

### 4.5 Unity 阶段脚本副本

- `stage5/AIGuardApiTest.cs`
- `stage5/AIGuardApiClientTests.cs`
- `stage6/AIGuardDialogueUI.cs`
- `stage6/AIGuardDialogueUITests.cs`
- `stage7/AIGuardGameplayRules.cs`
- `stage7/AIGuardGameplayEffects.cs`
- `stage7/AIGuardGameplayEffectsTests.cs`
- `stage8/AIGuardInteractionZone.cs`
- `stage8/AIGuardInteractionZoneTests.cs`
- `stage8/AIGuardNpcOnly.cs`

这些是阶段副本。Unity 项目内的实际脚本和场景必须到 `D:\UnityProjects\project03` 重新确认。

### 4.6 当前仓库外的关键文件

Unity 项目：

```text
D:\UnityProjects\project03
```

外部 Python / FastAPI 项目：

```text
D:\develop\pythons\api.py
D:\develop\pythons\save_guard.py
D:\develop\pythons\guard_state.json
D:\develop\pythons\test_api_rag.py
D:\develop\pythons\world_qa_demo.py
D:\develop\pythons\test_world_qa_demo.py
D:\develop\pythons\.venv\Scripts\python.exe
```

以上外部文件不在当前 Git 仓库内，任何修改都必须先重新读取实际文件。

## 5. 关键架构

### 5.1 总体职责边界

| 组件 | 负责内容 | 不应负责 |
| --- | --- | --- |
| Unity | 可信游戏状态、UI、倒计时、场景对象和游戏效果 | 不把 API Key 写入客户端，不盲信 AI 输出 |
| FastAPI | 为 Unity、AI NPC、RAG 和 Agent Workflow 提供 HTTP JSON 接口 | 不绕过规则系统直接改 Unity 世界 |
| DeepSeek | 理解玩家语言、分类意图、生成角色台词或策划文本 | 不决定信任数值、真假路线或合法游戏行为 |
| Python 规则系统 | 信任、恐惧、真假情报和工具白名单 | 不负责 Unity 场景对象的最终执行 |
| RAG | 检索已确认设定、引用来源、提醒明显冲突 | 不自动改设定，不把检索结果当成可执行指令 |
| Agent Workflow / MCP | 申请受控工具、记录本局行为、返回结构化结果 | 不直接开门、改血量、改任务或绕过白名单 |

### 5.2 AI NPC 数据流

```text
Unity 输入与 UI
-> FastAPI POST /npc/chat
-> DeepSeek 意图判断
-> Python 规则更新信任、恐惧和情报结果
-> DeepSeek 生成符合规则结果的台词
-> Python 输出校验
-> FastAPI 返回 JSON
-> Unity 执行 UI、加时和路线提示
```

核心规则：

```text
安抚：信任 +20，恐惧 -15
威胁：信任 -15，恐惧 +15
问路：
  信任 >= 50 且 信任 >= 恐惧 -> true_route
  恐惧 >= 信任 + 30 -> false_route
  其他 -> none
```

### 5.3 RAG 数据流

```text
docs/rag_setting.md
-> Markdown 切片
-> “标题：正文” Embedding
-> BAAI/bge-small-zh-v1.5
-> NumPy 向量索引
-> 问题 Embedding 与余弦相似度 Top 3
-> 基于证据回答或拒绝编造
-> 返回来源与匹配片段
```

冲突检查器复用相同检索结果，再由第一版规则判断守卫数量等明显冲突。

### 5.4 Agent Workflow 与 MCP 数据流

```text
玩家消息
-> run_agent_turn()
-> 决定是否申请工具
-> call_tool() 白名单校验
-> 工具返回受控路线或游戏状态
-> record_memory() 写入本局记忆
-> 返回 reply、tool_calls、memory 和 game_state
```

```text
MCP 客户端
-> stdio JSON-RPC
-> agent_workflow.mcp_server
-> initialize / tools/list / tools/call
-> 复用 call_tool() 白名单边界
-> 返回 content 或 isError
```

### 5.5 外部 FastAPI 与当前仓库的关系

```text
D:\develop\pythons\api.py
-> /npc/chat 复用外部 save_guard.py
-> /npc/world_qa 延迟导入当前仓库 ai_npc.rag_context
-> /agent/turn 延迟导入当前仓库 agent_workflow.prototype
```

`COEDX_LEARNING_ROOT` 用于告诉外部 FastAPI 当前仓库路径。`DEEPSEEK_API_KEY` 只从环境变量读取，不得写入代码或 Git。

## 6. 已知问题

1. **Unity 实际项目在仓库外。** `D:\UnityProjects\project03` 不属于当前 Git 仓库，任何 Unity 修改都必须先读取实际场景和脚本。不要直接手改 `.unity` YAML。
2. **外部 FastAPI 项目不可独立重建。** `D:\develop\pythons` 当前没有 `requirements.txt`、`pyproject.toml`、README 或 `.env.example`，只能使用现有 `.venv` 直接验证。
3. **Python 守卫状态可能跨 Play 模式保留。** 关卡重开流程曾验收通过，但退出并重新进入 Unity Play 模式时，外部 `guard_state.json` 仍可能被重新读取。正式录屏或扩展前需要重新实测，后续可增加新一局重置接口。
4. **RAG 对 Python 环境敏感。** 正式中文 Embedding 依赖 `sentence-transformers` 和 `BAAI/bge-small-zh-v1.5`；如果误用其他 Python，可能回退本地文本向量并与 512 维 BGE 索引不匹配。
5. **RAG 冲突检查范围有限。** 当前只覆盖守卫数量等第一批明显规则冲突，不是完整剧情审稿器，不会自动改设定。
6. **Agent Workflow 仍是最小原型。** 当前 Memory 是进程内的本局字典，没有长期持久化；MCP 是最小 stdio JSON-RPC 实现，没有依赖官方 MCP SDK。
7. **RAG、MCP 和 Agent 尚未接入 Unity 游戏流程。** Unity 当前主要使用 `/npc/chat`，`/npc/world_qa` 和 `/agent/turn` 主要供本地演示。
8. **AI 守卫尚未实现“真情报削弱守卫”。** 该玩法保留在后期，不阻塞当前阶段。
9. **录屏素材未完成。** `01_level1_overview.mp4` 已按用户决定暂缓，不得伪造视频文件或把状态写为已完成。
10. **外部 FastAPI 测试有弃用警告。** FastAPI `TestClient` 当前显示 `StarletteDeprecationWarning`，但不影响 7 项现有测试通过。
11. **Git 代理需要显式传给 Git。** 2026-06-30 检测到 Windows 系统代理为 `127.0.0.1:7897`，但 Git 不会自动使用它。推送前先确认代理端口仍然有效；当时成功使用的临时命令为：

```powershell
git -c http.proxy=http://127.0.0.1:7897 -c https.proxy=http://127.0.0.1:7897 push origin master
```

12. **`tools/` 仍未跟踪。** 该目录主要是简历 PDF 生成工具，与当前游戏作品集主线关系较弱，不要自动加入提交。
13. **同人作品有 IP 展示边界。** 对外展示时需说明原著来源，并突出原创支线设计、玩法实现和 AI 系统能力。
14. **部分长期文档仍保留历史快照。** `docs/project_context.md` 和 `docs/progress.md` 的早期段落中仍可能出现“尚无 Git 提交”或“路线待验证”等旧描述。当前状态以实际代码、新鲜测试、Git 和本交接文为准；只在相关任务需要时再修正对应旧段落。

## 7. 下一步开发计划

### 7.1 下一阶段：多 Agent 最小原型范围确认

本阶段只做范围设计，不写 LangGraph 或 Unity 接入代码。

最低交付内容：

1. 从守卫、囚犯、盗贼和商人中选择两个 Agent。
2. 为两个 Agent 定义目标、可见状态和本局记忆。
3. 定义最少共享世界状态，候选字段为 `alert_level`、`prison_gate_locked`、`key_owner` 和 `player_reputation`。
4. 定义 Agent 可以申请的白名单行为。
5. 明确 Agent 不得直接开门、改血量、修改任务或绕过游戏规则。
6. 把范围、作用和暂不实现内容写入专用设计文档。

验收后必须停止扩写，再决定是否进入本地 Python 多 Agent 原型。

### 7.2 后续候选顺序

1. 用普通 Python 字典和函数实现两个 Agent 的本地回合原型。
2. 验证两个 Agent 只能通过白名单行为影响共享世界状态。
3. 为本地原型添加自动测试和命令行演示。
4. 只在本地原型达到最小可行度后，再评估 LangGraph、大模型或 Unity 接入。

### 7.3 非当前阻塞的后期项

- 补全外部 FastAPI 的依赖清单和可移植交付结构。
- 重新实测并修复 Unity Play 模式的 Python 守卫状态重置问题。
- 扩展 RAG 冲突规则。
- 实现真情报削弱指定守卫的后期玩法。
- 补录作品集视频、截图和封面。
- 继续改善玩家操作、打击感和关卡细节，但不要在无明确验收标准时泛化打磨。
