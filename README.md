# 囚城营救作品集项目

这是一个以 Unity 2D 潜入营救游戏《囚城营救》为核心的个人作品集项目。项目重点不是单独展示后端或大模型调用，而是展示游戏策划、Unity 关卡、AI NPC、RAG 设定知识库和 Agent 工具调用如何组合成可讲解的 AI 游戏设计案例。

《囚城营救》是基于《九州缥缈录》原著人物与世界观创作的原创同人支线。当前原创内容包括潜入营救关卡流程、三路线设计、胆小守卫 AI NPC、RAG 设定管理和 Agent 原型。原著人物、势力与世界观归原作者及相关权利方所有。

## 当前可展示内容

| 模块 | 当前状态 | 展示重点 |
| --- | --- | --- |
| Unity Level1 | 已有可运行关卡，三路线体验已复核 | 限时潜入、敌人压力、隐藏暗道路线 |
| 胆小守卫 AI NPC | 已完成 Unity + FastAPI + DeepSeek + 规则系统垂直切片 | 玩家自由输入影响信任、恐惧和路线情报 |
| 真路线录屏流程 | 已试跑通过 | 从真实情报找到下方暗道入口 |
| 假路线演示流程 | 已有录制指南 | 威胁守卫可能获得误导情报 |
| RAG 世界观问答 | 已有本地检索、来源引用和 FastAPI 问答接口 | 回答设定问题并避免编造 |
| RAG 冲突检查器 | 已有命令行原型和演示说明 | 检查新设定是否可能冲突 |
| Agent Workflow / MCP | 已有白名单工具、Memory、FastAPI 接口和 MCP stdio 演示 | Agent 只能调用受控工具 |
| AI 关卡设计助手 | 已有命令行模板、DeepSeek、RAG、评价和 JSON 输出 | AI 辅助生成和评估关卡方案 |

完整交付盘点见 [docs/portfolio_delivery_checklist.md](docs/portfolio_delivery_checklist.md)。
录屏素材命名和目录规则见 [portfolio_delivery/README.md](portfolio_delivery/README.md)。

## 推荐录屏顺序

1. Unity Level1 基础游玩：展示倒计时、移动、敌人和三路线选择。
2. 胆小守卫真路线：安抚守卫，获得“往前第二个口子跳下去”的真实情报，并找到下方暗道入口。
3. 胆小守卫假路线：威胁守卫，获得“往上走最安全”的误导情报。
4. RAG 世界观问答：询问真实路线或角色设定，展示回答和来源。
5. RAG 冲突检查器：输入候选设定，展示可能冲突提醒。
6. AI 关卡设计助手：生成关卡方案并输出评价结果。
7. Agent Workflow / MCP：展示白名单工具调用、记忆记录和受控游戏状态读取。

## 重要路径

| 内容 | 路径 |
| --- | --- |
| 当前总仓库 | `C:\Users\eurp\Documents\coedx_learning` |
| 实际 Unity 项目 | `D:\UnityProjects\project03` |
| 外部 FastAPI 项目 | `D:\develop\pythons` |
| 推荐 Python 虚拟环境 | `D:\develop\pythons\.venv\Scripts\python.exe` |

当前仓库主要保存文档、RAG 原型、Agent 原型和阶段性记录。Unity 场景和部分外部 FastAPI 文件在上表对应路径中，接手时需要重新确认实际文件状态。

## 关键文档

- [docs/project_context.md](docs/project_context.md)：项目总览和开发者背景。
- [docs/progress.md](docs/progress.md)：阶段进度与验收记录。
- [docs/game_design.md](docs/game_design.md)：关卡与路线设计。
- [docs/ai_npc.md](docs/ai_npc.md)：胆小守卫 AI NPC 方案、架构和录制指南。
- [docs/rag.md](docs/rag.md)：RAG 设定知识库说明。
- [docs/agent_workflow.md](docs/agent_workflow.md)：Tool Calling / Memory / MCP 原型说明。
- [docs/portfolio_delivery_checklist.md](docs/portfolio_delivery_checklist.md)：作品集交付清单。
- [docs/external_fastapi_delivery.md](docs/external_fastapi_delivery.md)：外部 FastAPI 项目关系、必需文件和最小运行步骤。
- [docs/level1_overview_recording_checklist.md](docs/level1_overview_recording_checklist.md)：`01_level1_overview.mp4` 录屏范围、成功标准和隐私边界。
- [HANDOVER.md](HANDOVER.md)：接手提醒和当前已知问题。

## 当前边界

- 不在仓库中保存 API Key、密码或截图中的秘密信息。
- 当前版本找到吕归尘即通关，不包含护送与逃离玩法。
- 真实情报削弱指定守卫血量属于后期扩展，当前未实现。
- RAG、MCP 和 Agent 原型主要用于作品集讲解，当前不强行接入 Unity。
- LangGraph 和多 Agent 世界放在更后面，不提前做。

## 下一步

GitHub 仓库入口、录屏素材命名、外部 FastAPI 交付说明和 Level1 主演示录屏前检查已完成。`01_level1_overview.mp4` 的实际录制已按用户决定暂缓。

下一阶段建议做“多 Agent 游戏世界最小原型范围确认”：只定义两个 Agent、最少共享世界状态和禁止行为，暂不接 Unity、LangGraph 或大模型。
