# 第一次提交范围最小整理

## 文档用途

本文记录 2026-06-24 对第一次 Git 提交范围的建议。目标是先决定提交边界，不执行 `git add`、`git commit` 或文件删除。

## 当前状态

补充 `.gitignore` 并新增本文档后，当前可提交的未跟踪条目为 90 个，主要分布如下：

| 分类 | 数量 | 判断 |
| --- | --- | --- |
| `docs` | 31 | 建议纳入第一次提交 |
| `rag` | 21 | 建议纳入第一次提交 |
| `agent_workflow` | 9 | 建议纳入第一次提交 |
| `level_designer` | 8 | 建议纳入第一次提交 |
| `ai_npc` | 3 | 建议纳入第一次提交 |
| 根目录规则和入口文档 | 5 | 建议纳入第一次提交 |
| `stage5` / `stage6` / `stage7` / `stage8` | 10 | 建议纳入，但在提交说明中标注为 Unity 阶段性脚本副本 |
| `tools` | 3 | 暂不纳入第一次提交 |

## 建议纳入第一次提交

### 根目录入口和协作规则

- `.gitignore`
- `AGENTS.md`
- `HANDOVER.md`
- `README.md`
- `agent.md`

原因：这些文件定义项目入口、协作规则、接手信息和忽略规则，是仓库可维护性的基础。

### 项目文档

- `docs/`

原因：当前项目大量阶段成果、设计决策、验收结论和作品集交付信息都在 `docs/` 中。第一次提交应保留这些上下文，否则后续无法解释项目为什么这样做。

### RAG 原型

- `rag/`

原因：RAG 设定问答、冲突检查器、测试和说明文档已经达到可展示状态，是作品集的重要 AI 策划能力模块。

### AI NPC RAG 适配

- `ai_npc/`

原因：该目录保存 AI NPC 调用 RAG 的适配层和测试，是 AI NPC 与设定知识库连接的最小代码证据。

### Agent Workflow / MCP 原型

- `agent_workflow/`

原因：该目录保存 Tool Calling、Memory、MCP stdio 服务、演示脚本和测试，是 Agent 能力展示的最小代码证据。

### AI 关卡设计助手

- `level_designer/`

原因：该目录保存关卡设计助手的模板生成、DeepSeek 调用、RAG 上下文、评价和 JSON 输出，是 AI 策划工具展示模块。

### Unity 阶段性脚本副本

- `stage5/`
- `stage6/`
- `stage7/`
- `stage8/`

原因：这些目录不是完整 Unity 工程，但记录了 AI 守卫接入 Unity 的阶段性 C# 脚本和测试副本。第一次提交可以保留，提交说明中需要明确它们是阶段性脚本副本，实际 Unity 项目仍位于 `D:\UnityProjects\project03`。

## 暂不纳入第一次提交

### 本地简历生成工具

- `tools/`

原因：当前 `tools/` 中是米哈游简历 PDF 生成脚本，和《囚城营救》AI 游戏作品集主线关系较弱。建议暂不纳入第一次提交，后续如果要整理求职材料，再单独建阶段处理。

## 已由 `.gitignore` 排除

- `tmp/`
- `output/`
- `__pycache__/`
- `*.pyc`
- `rag/rag_data/`
- `.env`
- `.venv/`
- Unity 生成目录：`Library/`、`Temp/`、`Logs/`、`Obj/`、`UserSettings/`

原因：这些属于本地输出、缓存、环境或潜在秘密信息，不适合进入第一次提交。

## 建议的第一次提交分组

如果下一阶段正式执行提交，建议先使用一个总提交：

```text
chore: initialize portfolio project workspace
```

这个提交可以包含：

- 根目录规则和入口文档
- `docs/`
- `rag/`
- `ai_npc/`
- `agent_workflow/`
- `level_designer/`
- `stage5/` 到 `stage8/`

暂不包含：

- `tools/`
- 已忽略的 `tmp/`、`output/`、缓存和环境文件

## 下一阶段建议

进入“第一次提交执行前确认”。

最低可用目标：

```text
用户确认是否按本文建议暂不提交 tools/，并允许执行 git add / git commit。
```
