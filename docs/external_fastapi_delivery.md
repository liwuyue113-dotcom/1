# 外部 FastAPI 项目交付说明

## 文档用途

本文说明 `D:\develop\pythons` 与当前 Git 仓库的关系、现有接口所需文件以及最小启动和验证步骤。

本阶段只整理经实际文件和运行结果确认的交付信息，不迁移外部代码，不修改 Unity 项目。

## 两个目录的关系

```text
D:\develop\pythons
|-- api.py
|-- save_guard.py
|-- guard_state.json
`-- .venv
        |
        | COEDX_LEARNING_ROOT
        v
C:\Users\eurp\Documents\coedx_learning
|-- ai_npc/
|-- rag/
`-- agent_workflow/
```

- `D:\develop\pythons` 保存 FastAPI 入口、胆小守卫规则代码和本地 Python 虚拟环境。
- 当前 Git 仓库保存 RAG、AI NPC RAG 适配层和 Agent Workflow 原型。
- `api.py` 通过 `COEDX_LEARNING_ROOT` 找到当前仓库，再延迟导入 `ai_npc.rag_context` 和 `agent_workflow.prototype`。
- 如果没有设置 `COEDX_LEARNING_ROOT`，当前默认值是 `C:\Users\eurp\Documents\coedx_learning`。

## 已确认路由

| 路由 | 作用 | 主要依赖 |
| --- | --- | --- |
| `GET /health` | 检查 FastAPI 服务是否存活 | `api.py` |
| `POST /npc/chat` | 胆小守卫对话、信任恐惧和真假路线 | `api.py`、`save_guard.py` |
| `POST /npc/world_qa` | 使用当前仓库的 RAG 回答世界观问题 | `ai_npc/`、`rag/` |
| `POST /agent/turn` | 调用 Tool Calling / Memory 最小工作流 | `agent_workflow/` |

## 外部项目文件

| 文件 | 是否必需 | 说明 |
| --- | --- | --- |
| `api.py` | 是 | FastAPI 应用和四个已确认路由的入口 |
| `save_guard.py` | 是 | `api.py` 启动时会直接导入，同时提供胆小守卫规则 |
| `guard_state.json` | 否 | 本局守卫状态文件；缺失时会创建新状态，不应当作源代码 |
| `test_api_rag.py` | 建议保留 | 验证四个路由的接口边界 |
| `world_qa_demo.py` | 演示需要 | 在不接 Unity UI 的情况下演示 RAG 世界观问答 |
| `test_world_qa_demo.py` | 建议保留 | 验证世界观问答演示脚本 |
| `.venv/` | 仅当前本机需要 | 已安装依赖的本地虚拟环境，不应作为正式交付文件 |

## 当前依赖快照

2026-06-28 在实际虚拟环境中读取到：

```text
fastapi=0.136.3
pydantic=2.13.4
openai=2.38.0
uvicorn=0.48.0
```

外部项目根目录当前没有 `requirements.txt`、`pyproject.toml`、`README.md` 或 `.env.example`。因此上述版本只是当前本机的已验证快照，不是已完成的可移植安装方案。

## 环境变量

| 变量 | 是否必需 | 用途 |
| --- | --- | --- |
| `COEDX_LEARNING_ROOT` | 当前本机可选，换路径时必需 | 告诉 `api.py` 当前 Git 仓库的位置 |
| `DEEPSEEK_API_KEY` | 调用真实模型时必需 | 用于胆小守卫的意图判断和台词生成；缺失时使用本地备用逻辑 |

不要把 API Key 写入代码、本文档或 Git 提交。

## 最小启动步骤

在 PowerShell 中执行：

```powershell
cd D:\develop\pythons
$env:COEDX_LEARNING_ROOT='C:\Users\eurp\Documents\coedx_learning'
D:\develop\pythons\.venv\Scripts\python.exe -m uvicorn api:app --host 127.0.0.1 --port 8000
```

启动后在另一个 PowerShell 窗口验证：

```powershell
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:8000/health |
    Select-Object StatusCode, Content
```

预期结果：

```text
StatusCode: 200
Content: {"status":"ok"}
```

## 最小测试步骤

```powershell
cd D:\develop\pythons
D:\develop\pythons\.venv\Scripts\python.exe -m unittest test_api_rag.py test_world_qa_demo.py -v
```

2026-06-28 实际结果：7 项测试通过。运行时出现 `StarletteDeprecationWarning`，但未导致测试失败，当前不阻塞交付。

## 本阶段作用

这一阶段把“我的电脑上可以运行”变成了“接手者知道代码在哪里、怎么启动、如何验证、还缺什么”。

对作品集的价值是：能清楚解释 Unity、FastAPI、Python 规则、RAG 和 Agent Workflow 的代码边界，不把外部路径假装成已经完整打包的开源项目。

## 当前边界

- 不迁移 `D:\develop\pythons` 中的业务代码。
- 不提交 `.venv/`、`guard_state.json` 或 API Key。
- 不为了补文档而改动现有 `/npc/chat`、`/npc/world_qa` 或 `/agent/turn`。
- 不把当前依赖快照冒充为已验证的全新环境安装清单。

## 下一阶段

进入“Unity Level1 主演示录屏前最小检查”，只确认 `01_level1_overview.mp4` 的录制范围、成功标准和需要避免暴露的信息。
