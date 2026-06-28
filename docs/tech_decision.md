# 技术决策记录

## 2026-06-24 GitHub 页面确认使用 API 与 README 最小修正

决策：GitHub 页面确认阶段只验证仓库公开状态、默认分支、远程 README 和最新提交，不做 GitHub Pages 或 Releases。

原因：当前作品集入口已经由根目录 `README.md` 承担；继续扩展页面能力会超出当前最小阶段目标。

影响：新增 `docs/github_page_check.md`，并修正 README 的“下一步”为录屏素材命名与交付文件夹整理。

## 2026-06-24 GitHub 首次推送完成

决策：保留 `master` 作为当前远程分支，不额外改名为 `main`。

原因：本地历史已经在 `master`，用户提供的空仓库已成功接收 `master -> master`，继续改名会增加非必要步骤。

影响：后续常规流程使用 `git add`、`git commit` 和 `git push`；当前 `master` 已追踪 `origin/master`。

## 文档用途

本文档记录项目采用某项技术或方案的原因。每次完成新功能或改变实现方案时，应新增一条决策记录，避免关键原因只保留在聊天记录中。

## 当前技术栈

| 模块 | 当前选择 | 状态 |
| --- | --- | --- |
| 游戏客户端 | Unity 2D、C# | 已使用，Unity 版本已确认为 2022.3.62f3 |
| AI 服务端 | Python、FastAPI | 已用于胆小守卫 AI NPC |
| 大模型服务 | DeepSeek API | 已用于意图判断与角色台词生成 |
| 本地模型 | Ollama | 已有本地部署经验，是否用于最终展示待评估 |
| 数据交换 | HTTP、JSON | 已用于 Unity 与 FastAPI 通信 |
| RAG | Python、BGE 中文 Embedding、NumPy | 正式语义模型已启用 |
| AI NPC RAG 适配层 | Python、复用现有 RAG 检索与问答服务、FastAPI 独立世界观问答接口 | 已接入外部 FastAPI |
| AI 关卡设计助手 | Python 命令行、固定 Markdown 模板、DeepSeek API、RAG 检索、规则评价、JSON 输出 | JSON 输出版 MVP 已完成 |
| Agent | Tool Calling、Memory、Agent Workflow、FastAPI 最小接口、MCP stdio 最小服务 | MCP 最小服务 MVP 已完成 |
| 多 Agent | LangGraph 或轻量状态机 | 后期评估 |
| 版本管理 | Git、GitHub | GitHub 会使用，Git 工作流需要加强 |

## Unity 版本

- 当前版本：2022.3.62f3
- 确认方式：在实际 Unity 项目中查看 `ProjectSettings/ProjectVersion.txt`
- 维护要求：确认后在此处记录，升级 Unity 前必须新增技术决策

## FastAPI 方案

FastAPI 作为 Unity 与 AI 服务之间的中间层：

```text
Unity 客户端 -> HTTP JSON 请求 -> FastAPI -> 大模型或 RAG/Agent -> JSON 响应 -> Unity 执行游戏逻辑
```

采用原因：

- Python 生态适合调用大模型、构建 RAG 和 Agent
- Unity 无需直接保存 API Key
- 接口容易独立测试和演示
- 后续可以逐步加入记忆、工具调用与世界状态

## AI NPC 方案

- 大模型负责生成符合角色设定的语言，以及给出受约束的行为建议
- Unity 负责验证并执行真正的游戏行为
- AI 不直接开启门、修改任务或改变世界状态
- AI 输出使用固定 JSON 结构，避免自由文本破坏游戏逻辑
- 第一位 AI NPC 优先与隐藏路线机制结合

## RAG 方案

- 用于保存角色、阵营、地图、任务和剧情设定
- AI NPC 回答与剧情生成优先检索已有设定
- 回答应保留来源信息，便于检查世界观冲突
- 第一版优先选择简单、可本地运行的向量数据库；Chroma 与 FAISS 的最终选择待原型验证

## Agent 方案

- Agent 被定义为：具有目标、状态、工具、记忆与行动流程的 AI 系统
- 游戏行为必须来自预先允许的工具集合
- 典型工具包括：查看地图、查询任务状态、尝试开门、更新信任度
- 多 Agent 世界后期才加入，先完成单个 AI NPC 垂直切片

## GitHub 管理规范

- 使用 Git 记录所有代码与文档变更
- 每个提交只完成一个清晰目标
- 不提交 API Key、密码、缓存文件或 Unity 临时目录
- 功能开发建议使用分支，分支命名格式：`feature/<功能名>`
- 重要功能完成后，在 README 或作品集说明中补充演示方式

建议的 Unity `.gitignore` 排除项：

- `Library/`
- `Temp/`
- `Logs/`
- `Obj/`
- `UserSettings/`

## 后续技术决策

| 日期 | 决策 | 原因 | 影响 |
| --- | --- | --- | --- |
| 2026-06-07 | 当前工作区作为完整作品集总仓库 | 需要同时维护 Unity、AI NPC、RAG 与 Agent 项目知识 | `docs/` 覆盖全部作品集方向 |
| 2026-06-07 | 优先制作与隐藏路线联动的 AI NPC | 能结合现有三路线关卡，并形成可展示的 AI 游戏机制 | 暂缓多 Agent，先完成单 NPC 垂直切片 |
| 2026-06-07 | 使用 FastAPI 隔离 Unity 与大模型服务 | 便于保护 API Key、测试接口并扩展 RAG/Agent | Unity 通过 HTTP 和 JSON 通信 |
| 2026-06-12 | 大模型只负责语言理解与台词，规则系统决定真假路线 | 防止模型随意改变游戏机制，同时保留自然语言交互 | Python 验证结构化结果，Unity 只执行合法字段 |
| 2026-06-12 | RAG 第一版使用本地 Embedding 与 NumPy 向量检索 | 便于学习核心流程、本地演示和后续替换存储层 | 第一版先实现设定问答与来源引用，之后可替换为 Chroma |
| 2026-06-12 | 正式 Embedding 不可用时启用内置文本向量兜底 | 依赖安装审批超时，不能阻塞第一版完整流程验收 | 当前可本地运行，后续安装 BGE 模型提升语义检索质量 |
| 2026-06-12 | 正式语义检索使用 `BAAI/bge-small-zh-v1.5` | 中文语义检索效果优于依赖文字重合的内置兜底，模型体积适合本地作品集演示 | 索引与查询必须使用相同虚拟环境和模型；下一阶段优化设定数据与切片 |
| 2026-06-13 | 构建索引时使用“标题：正文”生成 Embedding | 单义标题包含直接问题语义，仅编码正文会浪费标题信息 | 查询和展示结构不变；五题验收从 3 项通过提升到 4 项通过 |
| 2026-06-13 | 设定问答默认只索引专用已确认设定文档 | 完整策划案包含通用玩法、评价指标和待开发内容，会干扰具体设定问答 | `docs/game_design.md` 不再进入默认索引；五题 Top 3 验收全部通过 |
| 2026-06-17 | AI 关卡设计助手第一版使用本地命令行模板 | 先完成可运行、可测试、可讲解的最低版本，避免还没定输出格式就提前接入 API 和复杂架构 | 新增 `level_designer` 包；后续可在同一输入输出接口外接 DeepSeek、RAG 或网页 |
| 2026-06-17 | AI 关卡设计助手 DeepSeek 版仍保留本地模板兜底 | API Key 可能未设置或网络调用可能失败，作品集演示工具不能因此完全不可用 | `--provider deepseek` 调用 DeepSeek；缺少 `DEEPSEEK_API_KEY` 或调用失败时回退到本地模板 |
| 2026-06-17 | AI 关卡设计助手 RAG 版只检索已确认设定，不让 RAG 直接生成策划案 | 关卡助手需要稳定输出固定模板；RAG 更适合作为事实来源，避免二次生成造成结构漂移 | `--use-rag` 会把检索片段加入模板输出或 DeepSeek Prompt；RAG 索引不可用时保留命令行路线资料 |
| 2026-06-17 | AI 关卡设计助手质量评价第一版使用规则检查 | 当前目标是最低可用的策划结构验收，不需要先引入模型评分或复杂数值平衡算法 | `--evaluate` 检查玩家目标、三条路线、风险收益和失败条件，并输出改进建议 |
| 2026-06-17 | AI 关卡设计助手 JSON 输出保留 Markdown 正文 | DeepSeek 生成文本不一定稳定适合拆段解析，第一版结构化输出先包裹完整 Markdown 和评价结果 | `--format json` 输出 `plan_markdown`、`evaluation`、`warnings` 和输入参数，便于未来网页或 Unity 工具读取 |
| 2026-06-17 | Unity 场景核对先采用静态读取，不直接手改场景 YAML | Unity MCP 连续超时，直接编辑 `.unity` YAML 风险较高；当前阶段目标是确认是否阻塞下一步 | 先记录 Level1 的对象、坐标和疑似不一致点；实际摆放调整应进入 Unity 编辑器完成 |
| 2026-06-23 | RAG 接入 AI NPC 先做当前仓库内 Python 适配层 | 实际 FastAPI 项目位于 `D:\develop\pythons`，不在当前仓库内；先用可测试适配层确认 query、证据格式化和拒答规则 | 新增 `ai_npc.rag_context`，可复用现有 RAG 索引返回 NPC 回复依据；下一步再接入外部 FastAPI |
| 2026-06-23 | 外部 FastAPI 通过独立接口接入 RAG，不改 `/npc/chat` | 现有 Unity 已依赖 `/npc/chat` 的请求结构和真假路线字段；独立接口风险最低，适合最低可用展示 | 新增 `POST /npc/world_qa`；Unity 原有 AI 守卫对话不受影响 |
| 2026-06-23 | RAG 世界观问答演示使用 FastAPI `TestClient` 进程内调用 | 当前目标只是验证 `/npc/world_qa` 可展示，不需要提前接 Unity UI 或要求用户手动启动 uvicorn | 新增外部脚本 `D:\develop\pythons\world_qa_demo.py`；一条命令即可展示回答、RAG 状态和来源 |
| 2026-06-23 | Tool Calling / Memory 先做本地 Python 最小原型 | 当前目标是理解 Agent Workflow 的基本边界，不需要提前接真实 MCP、Unity、LangGraph 或长期记忆 | 新增 `agent_workflow` 包；先验证白名单工具、本局记忆和命令行演示 |
| 2026-06-23 | Agent Workflow 先通过独立 FastAPI 接口暴露，不改现有 NPC 接口 | `/npc/chat` 已被 Unity 使用，`/npc/world_qa` 已用于 RAG 演示；独立 `/agent/turn` 风险最低，也便于讲解 Agent 输入输出 | 外部 `D:\develop\pythons\api.py` 新增 `POST /agent/turn`，返回 `reply`、`tool_calls`、`memory` 和 `game_state`；当前不接 Unity、不接真实 MCP、不做长期记忆 |
| 2026-06-23 | 真实 MCP 第一版使用 stdio JSON-RPC 最小实现，不新增外部依赖 | 当前虚拟环境没有安装 `mcp` SDK；本阶段目标是证明 MCP 工具暴露和白名单边界，不需要先引入完整 SDK 和配置复杂度 | 新增 `agent_workflow/mcp_server.py`，支持 `initialize`、`tools/list` 和 `tools/call`，第一版只暴露 `get_route_info` |
| 2026-06-24 | MCP 客户端配置先提供示例 JSON，不写入真实本机客户端配置 | 不同 MCP 客户端的配置位置不同，直接修改用户本机配置风险较高；示例文件足够支撑作品集讲解和后续手动接入 | 新增 `agent_workflow/mcp_client_config.example.json`，文档说明 `command`、`args` 和 `cwd` |
| 2026-06-24 | MCP 第二个工具选择 `check_game_state`，暂不暴露 `update_quest_hint` | 当前阶段只做只读能力，避免 MCP 客户端过早修改任务状态；先证明 MCP 可以读取受控游戏状态 | `tools/list` 新增 `check_game_state`，`tools/call` 可返回剩余时间、钥匙状态和任务提示 |
| 2026-06-24 | MCP 演示先使用进程内脚本，不强依赖真实客户端 | 真实 MCP 客户端配置差异较大，当前作品集阶段更需要稳定、可录制、可讲解的演示方式 | 新增 `agent_workflow/mcp_demo.py`，展示 `tools/list`、`get_route_info` 和 `check_game_state` 调用结果 |
| 2026-06-24 | Agent Workflow 阶段作用说明单独成文 | 当前代码原型已经达到 MCP 演示 MVP，下一步更需要把每个阶段的价值讲清楚，而不是继续扩展工具 | 新增 `docs/agent_workflow_stage_roles.md`，用于作品集录屏、答辩和面试讲解 |
| 2026-06-24 | RAG 冲突检查器第一版使用规则判断，不调用大模型 | 当前目标是最低可用的设定冲突提醒，不需要让模型审稿或自动改设定；规则判断更稳定，也更容易解释给面试官 | 新增 `rag.conflict_checker` 和 `rag.check_conflict`，先识别守卫数量这类明显冲突 |
| 2026-06-24 | RAG 冲突检查器演示说明单独成文 | 功能 MVP 已完成，下一步更需要把问题、命令、输出和边界讲清楚，而不是继续扩展规则 | 新增 `docs/rag_conflict_checker_demo.md`，用于录屏、答辩和面试讲解 |
| 2026-06-24 | Unity Level1 路线核对继续采用静态读取，不直接手改场景 YAML | Unity MCP 读取活动场景超时，直接编辑 `.unity` 文件风险高；当前阶段只需要确认是否存在阻塞性不一致 | 新增 `docs/unity_level1_route_audit.md`，记录下方层级 3 个敌人的待确认问题，下一步应进 Unity 编辑器复核 |
| 2026-06-24 | 下方暗道敌人归属以 Unity 编辑器人工复核为准 | 静态 y 坐标只能说明敌人在下方层级，不能证明它们都在暗道内部；Unity MCP 直接读取 `Enemy (3)` 继续超时 | 先记录人工复核清单，不移动或删除敌人；等确认 `Enemy (3)`、`Enemy (4)`、`Enemy (6)` 归属后再做最小场景调整 |
| 2026-06-24 | 下方暗道陷阱敌人不计入站岗守卫数量 | 用户在 Unity 编辑器确认 `Enemy (3)`、`Enemy (4)`、`Enemy (6)` 都在陷阱里且不会出来；它们不会形成可走路径上的巡逻或站岗压力 | 保留当前场景敌人，不移动或删除；设定文档改为区分陷阱敌人与可走路径上的站岗守卫 |
| 2026-06-24 | 路线整体体验核对先分离静态证据和实际游玩判断 | 静态坐标可以证明上/中/下层级和对象分布，但不能证明路径长度、入口可见性和敌人实际压力 | 新增 `docs/unity_level1_route_experience_audit.md`；下一步只用 Unity Scene 视图或实际游玩回答三个体验问题 |
| 2026-06-24 | Level1 三路线体验达到最低可用后停止继续打磨 | 用户已确认上路更绕、中路压力更集中、下方暗道入口需要真实情报后可理解；继续微调会偏离阶段式推进 | 当前不重摆敌人、不改路线长度、不调数值；下一步转向 AI 守卫路线提示展示流程复核 |
| 2026-06-24 | AI 守卫真路线录屏先做最小复核清单 | 已有 `docs/ai_npc.md` 完整录制指南，本阶段只需要验证真情报到暗道入口的展示链路是否顺畅 | 新增 `docs/ai_guard_route_recording_checklist.md`，不改 Unity、不改 AI 逻辑、不扩展假路线录屏 |
| 2026-06-24 | 真路线录屏链路跑通后停止继续打磨 | 用户已确认可以从胆小守卫真实情报顺利走到下方暗道入口；继续优化录屏细节会拖慢作品集收束 | 当前不再调整该链路，下一步转向作品集交付清单最小整理 |
| 2026-06-24 | 作品集收束先做交付清单，不继续扩功能 | 当前已经有多个可展示模块，继续做新功能会稀释主线；需要先明确展示顺序和缺口 | 新增 `docs/portfolio_delivery_checklist.md`，下一步转向 README 入口整理 |
| 2026-06-24 | 先新增最小 README 作为作品集入口 | 当前仓库缺少入口说明，接手者难以判断项目定位、展示模块和外部路径 | 新增根目录 `README.md`，下一步转向提交前清理最小检查 |
| 2026-06-24 | 第一次提交前先补全最小 `.gitignore` | 当前仓库存在本地输出、缓存和潜在秘密文件风险；直接提交容易混入生成物或个人素材 | `.gitignore` 新增 `.env`、虚拟环境、`tmp/`、`output/`、Unity 生成目录、日志和缓存目录；下一步整理第一次提交范围 |
| 2026-06-24 | 第一次提交范围先保留作品集主线，暂不纳入简历生成工具 | `tools/` 当前主要服务个人简历 PDF 生成，和《囚城营救》AI 游戏作品集主线关系较弱；第一次提交应先聚焦项目本体 | 新增 `docs/first_commit_scope.md`，建议提交主线文档与原型代码，暂不提交 `tools/` |
| 2026-06-27 | 录屏素材采用“两位顺序号 + 模块 + 内容”命名，Git 只跟踪目录说明 | 录制和剪辑需要稳定排序，但原始视频大文件不适合在当前阶段直接提交 | 新增 `portfolio_delivery/README.md`，映射 8 个展示模块；视频保留在本地目录，正式成片后再决定交付方式 |

新增决策时使用以下格式：

```text
日期：
决策：
备选方案：
选择原因：
带来的影响：
```
## 2026-06-24 GitHub remote 配置

决策：使用用户提供的仓库地址 `https://github.com/liwuyue113-dotcom/1.git` 作为当前仓库的 `origin`。

原因：当前作品集仓库已经有本地提交历史，下一步需要推送到用户指定的 GitHub 仓库。

影响：remote 配置已完成；推送命令 `git push -u origin master` 因本机无法连接 `github.com:443` 暂未完成。

## 2026-06-24 GitHub 推送前检查

决策：GitHub 推送前先检查 remote，不在没有仓库地址时直接推送。

原因：当前本地提交已完成，但 `git remote -v` 无输出。直接推送会失败，也无法判断仓库公开/私有和默认分支策略。

影响：新增 `docs/github_push_precheck.md`；下一步由用户提供 GitHub 仓库地址后，再配置 `origin` 并推送。
