# 作品集录屏素材交付目录

## 目录作用

本目录用于统一《囚城营救》作品集录屏素材的命名、存放位置和展示顺序。当前只提交说明文档，不提交视频、封面或截图大文件。

推荐在本地按以下结构整理：

```text
portfolio_delivery/
|-- videos/       # 原始录屏和剪辑后视频
|-- screenshots/  # 作品集页面或文档截图
|-- covers/       # 视频封面
`-- README.md     # 命名和模块对应表
```

## 录屏文件命名

命名规则：

```text
两位顺序号_模块_展示内容.mp4
```

| 顺序 | 推荐文件名 | 对应模块 | 本阶段作用 |
| --- | --- | --- | --- |
| 01 | `01_level1_overview.mp4` | Unity Level1 | 先让观看者理解限时潜入、敌人压力和三路线基础玩法 |
| 02 | `02_ai_guard_true_route.mp4` | 胆小守卫真路线 | 展示安抚守卫后，真实情报如何影响玩家路线选择 |
| 03 | `03_ai_guard_false_route.mp4` | 胆小守卫假路线 | 展示威胁导致假情报和玩法风险 |
| 04 | `04_rag_world_qa.mp4` | RAG 世界观问答 | 展示设定检索、来源引用和证据不足时拒绝编造 |
| 05 | `05_rag_conflict_checker.mp4` | RAG 设定冲突检查器 | 展示新设定与已确认设定的一致性检查 |
| 06 | `06_level_designer.mp4` | AI 关卡设计助手 | 展示结构化关卡方案生成和最低质量评价 |
| 07 | `07_agent_workflow.mp4` | Tool Calling / Memory | 展示白名单工具、本局记忆和未授权工具拒绝 |
| 08 | `08_mcp_tools_demo.mp4` | MCP 最小服务 | 展示 `tools/list` 以及两个只读工具的受控调用 |

`01_level1_overview.mp4` 的录屏前检查见 [../docs/level1_overview_recording_checklist.md](../docs/level1_overview_recording_checklist.md)。

## 截图与封面命名

与对应视频保持相同前缀：

```text
screenshots/02_ai_guard_true_route_dialogue.png
covers/02_ai_guard_true_route_cover.png
```

同一模块有多张截图时，在内容名后补充用途，不使用 `final` 、`new` 或 `test` 这类无法判断内容的名称。

## 当前边界

- 录制前先使用对应模块的检查清单，不在本文中扩写演示脚本。
- 不把视频大文件直接加入 Git 提交。
- 不创建 GitHub Release，等正式成片准备好后再决定交付方式。
- 不改 Unity 场景、Python 服务或已完成的演示逻辑。

## 录制时的使用方式

1. 按编号从 `01` 到 `08` 录制，每个文件只展示一个主题。
2. 原始素材先放入本地 `videos/`，不立即加入 Git。
3. 录制后检查文件名、演示内容和对应模块是否一致。
4. 正式交付时再选择压缩后视频、网盘链接或 GitHub Release。
