# 项目进度

## 阶段验收：GitHub 页面确认与作品集入口检查

日期：2026-06-24

完成内容：
- 通过 GitHub API 确认远程仓库 `liwuyue113-dotcom/1` 存在。
- 确认仓库为公开仓库，默认分支为 `master`。
- 确认页面检查时的远程提交为 `1701fade docs: record successful github push`。
- 确认远程 `README.md` 已存在。
- 更新 README 的“下一步”，避免继续指向已经完成的提交前检查阶段。
- 新增 `docs/github_page_check.md` 记录页面确认结果。

验证方式：
- `Invoke-WebRequest https://api.github.com/repos/liwuyue113-dotcom/1` 返回 `private: false`、`visibility: public`、`default_branch: master`。
- `Invoke-WebRequest https://api.github.com/repos/liwuyue113-dotcom/1/contents/README.md` 返回远程 `README.md` 元数据和 GitHub 页面链接。
- `Invoke-WebRequest https://api.github.com/repos/liwuyue113-dotcom/1/commits/master` 在页面检查时返回提交 `1701fade...`。

结论：
- 当前阶段已完成，达到最小可行度。
- 下一步进入“录屏素材命名与作品集交付文件夹最小整理”，不继续打磨 GitHub 页面。

## 阶段验收：GitHub 首次推送完成

日期：2026-06-24

完成内容：
- 用户在本机 PowerShell 成功执行 `git push -u origin master`。
- 远程仓库为 `https://github.com/liwuyue113-dotcom/1.git`。
- `master` 已建立 upstream 到 `origin/master`。

验证方式：
- 截图显示 GitHub 返回 `master -> master`，并提示 `branch 'master' set up to track 'origin/master'`。
- 本地 `git status -sb` 显示 `## master...origin/master`。
- 本地 `git rev-parse --abbrev-ref --symbolic-full-name '@{u}'` 返回 `origin/master`。

结论：
- GitHub 首次推送完成，达到最小可行度。
- 下一步进入 GitHub 页面确认与作品集展示入口检查，不继续打磨 Git 推送流程。

## 文档用途

本文档是整个作品集项目的唯一进度总表。每次完成、开始或取消功能时都要更新本文件，并同步更新对应设计文档与技术决策。

最后更新：2026-06-24

## 总体阶段

当前阶段：GitHub 页面确认与作品集入口检查已完成，建议进入录屏素材命名与作品集交付文件夹最小整理。

完整阶段路线与验收标准见 `docs/staged_roadmap.md`。

## 阶段式教学执行规则

- 每个阶段只完成最低可用版本，不提前优化。
- 用户反馈运行结果后，先验收当前阶段。
- 没有阻塞下一阶段的问题时，立即进入下一阶段。
- 一旦某阶段达到最小可行性，必须停止继续补充、打磨或扩写该阶段内容，并开始下一阶段。
- 同一段代码停留超过 2 轮时，主动提醒当前阶段是否已完成。
- 每次回复必须说明当前阶段、阶段目标、完成状态、下一步和需要修改的文件。

## 已完成

### 《囚城营救》

- 已确定游戏核心：限时潜入并营救目标
- 已确定主角姓名：姬野
- 已完成一个可运行的 Unity 2D 游戏版本
- 已实现角色移动
- 已实现战斗
- 已实现敌人
- 已实现基础关卡
- 已实现 UI
- 已实现存档
- 已有三条不同路线的初步设计构想
- 已完成《囚城营救》策划案初稿

### AI 与开发基础

- 已安装并使用 PyCharm
- 跟随教学编写过 Python 文件
- 使用过 `pip` 安装依赖
- 调用过 DeepSeek 与阿里云大模型 API
- 本地部署过 Ollama
- 对 RAG、LangChain、Agent、Skill、MCP 有初步概念认识
- 会使用 GitHub
- 已完成胆小守卫 AI NPC 的 Python 规则原型第一阶段练习
- 已掌握本原型中用到的字典、函数、`if` 判断、列表、JSON 保存/读取、文件不存在处理、`input()`、`while` 循环和简单意图判断
- 已完成第 1 阶段验收：Python 规则原型能够连续对话、更新状态、判断路线并保存读取 JSON
- 已完成第 2 阶段验收：DeepSeek API 已接通，并能正确返回 `comfort`、`threaten`、`ask_route`、`other`
- 已完成第 3 阶段验收：DeepSeek 能根据规则结果生成胆小守卫台词，且 `none` 状态不会泄露路线
- 已完成第 4 阶段验收：FastAPI 的 `GET /health` 与 `POST /npc/chat` 已成功返回 JSON
- 已完成第 5 阶段验收：Unity 已通过 HTTP POST 调用 FastAPI，并在 Console 正常打印中文结构化 JSON
- 已完成第 6 阶段验收：Unity AI 对话 UI 已支持输入、发送、回复、情绪显示和请求期间禁止重复发送
- 已完成第 7 阶段验收：首次对话只增加一次 20 秒，真假路线显示不同固定提示，假路线能够更正为真路线
- 已完成第 8 阶段验收：Level1 完整流程、状态重置、普通 NPC 隔离和交互范围 UI 显示隐藏均正常
- 已完成第 9 阶段：录制指南、系统架构说明和作品集项目介绍已整理完成

### 项目管理

- 已初始化 Git 仓库
- 已建立长期维护的 `docs/` 项目知识库
- 已创建根目录 `AGENTS.md`，让新项目对话自动读取项目背景并维护知识库
- 已将 `AGENTS.md` 与 `agent.md` 整理为“总规则 + 详细实施手册”的主次结构
- 已将开发者个人信息摘要加入主规则 `AGENTS.md`
- 已将 AI 游戏策划 + Python + Agent 导师定位、六阶段学习路线和最终作品集方向合并进 `agent.md`
- 已将项目知识库摘要合并进 `docs/project_context.md`
- 已将 AI NPC 架构、作品集介绍和录制指南合并进 `docs/ai_npc.md`

## 阶段总结：Python 胆小守卫规则原型

日期：2026-06-07

本阶段完成了《囚城营救》AI NPC 的第一个 Python 小原型。这个原型暂时不接 DeepSeek，也不接 Unity，而是先建立一个稳定的 NPC 规则骨架。

### 已完成内容

- 使用 `guard_state` 字典保存胆小守卫的核心状态：
  - `trust`：信任值
  - `fear`：恐惧值
  - `intel_result`：当前情报结果
  - `time_bonus_given`：是否已发放加时奖励
  - `history`：本局对话历史
- 使用 `comfort_guard()` 表示玩家安抚守卫，效果是增加信任、降低恐惧。
- 使用 `threaten_guard()` 表示玩家威胁守卫，效果是降低信任、增加恐惧。
- 使用 `decide_intel()` 根据规则判断守卫是否提供真实路线、虚假路线或拒绝透露。
- 使用 `get_emotion()` 将内部数值转换为玩家能看到的情绪状态。
- 使用 `chat_once()` 处理一轮玩家输入，并返回未来 Unity 可使用的结构化结果。
- 使用 `history` 记录玩家和守卫的对话，形成短期记忆。
- 使用 `save_state()` 和 `load_state()` 将守卫状态保存到 `guard_state.json`，并从 JSON 中读取。
- 使用 `while True` 实现连续对话，玩家输入 `退出` 时保存状态并结束。
- 初步使用关键词列表和 `get_player_intent()` 判断玩家意图，为后续 DeepSeek 接入预留接口。

### 当前原型规则

```text
安抚守卫：
信任 +20
恐惧 -15

威胁守卫：
信任 -15
恐惧 +15

询问路线时：
信任 >= 50 且 信任 >= 恐惧 -> true_route
恐惧 >= 信任 + 30 -> false_route
其他情况 -> none
```

### 学到的核心概念

- `dict`：保存 NPC 状态。
- `list`：保存多轮对话历史。
- `function`：把安抚、威胁、判断路线等行为封装成独立功能。
- `if / elif / else`：根据状态决定守卫行为。
- `return`：让函数把结果交还给主程序。
- `json.dump()`：把 Python 状态保存到 JSON 文件。
- `json.load()`：从 JSON 文件读取状态。
- `os.path.exists()`：检查存档文件是否存在，避免第一次运行时报错。
- `input()`：接收玩家输入。
- `while True` 和 `break`：实现连续对话和退出。

### 为什么先做这个原型

这一步不是为了把关键词聊天做得复杂，而是为了建立 AI NPC 的后端骨架：

```text
玩家输入
-> 判断玩家意图
-> 修改 NPC 状态
-> 决定真假情报
-> 生成结构化结果
-> 保存本局记忆
```

后续接入 DeepSeek 后，关键词判断会被大模型替代，但信任、恐惧、真假路线和 Unity 执行规则仍然保留。这样可以避免让大模型直接决定游戏机制，保证玩法公平、稳定、可测试。

### 当前代码阅读重点

当前最重要的函数是：

```python
def chat_once(state, player_message):
```

它代表一轮 AI NPC 对话的完整流程：

```text
理解玩家行为
-> 修改守卫状态
-> 判断真假路线
-> 生成回复
-> 记录记忆
-> 返回结果
```

### 下一步

停止继续堆关键词规则，进入 DeepSeek API 接入。下一阶段目标是让 DeepSeek 只负责判断玩家意图，例如：

```json
{
  "intent": "comfort"
}
```

规则系统仍然负责信任、恐惧、真假情报和结构化结果。

## 阶段验收：DeepSeek 判断玩家意图

日期：2026-06-09

第 2 阶段已完成并通过验收。

验收输入与结果：

```text
“我保证不会伤害你” -> comfort
“如果不说，我会让你后悔” -> threaten
“哪条道路巡逻的人最少” -> ask_route
“今天天气不错” -> other
```

验收结论：

- DeepSeek API 已成功接通。
- 非关键词化表达能够被正确分类。
- Python 规则仍负责更新信任、恐惧和情报结果。
- 程序可以正常退出。
- 没有阻塞第 3 阶段的问题。

## 阶段验收：DeepSeek 生成守卫台词

日期：2026-06-09

第 3 阶段已完成并通过验收。

验收结论：

- DeepSeek 能生成符合胆小守卫性格的动态台词。
- `true_route` 时，守卫正确透露往前第二个口子跳下去的无人镇守暗道。
- `false_route` 时，守卫以犹豫语气欺骗玩家往上走最安全。
- `none` 时，通过按结果限制 Prompt 和 Python 输出拦截，守卫不再泄露路线。
- Python 规则仍负责信任、恐惧和真假情报，DeepSeek 只负责语言表达。
- 没有阻塞 FastAPI 接口开发的问题。

## 阶段验收：FastAPI 对话接口

日期：2026-06-09

第 4 阶段已完成并通过验收。

验收结论：

- FastAPI 与 Uvicorn 能正常启动。
- `GET /health` 可用于确认服务状态。
- `POST /npc/chat` 能接收 `player_message`。
- 对话接口成功返回 HTTP `200`。
- 返回 JSON 包含 `reply`、`emotion`、`trust`、`fear`、`intent`、`intel_result`。
- FastAPI 能复用现有胆小守卫逻辑并保存状态。
- 根路径 `/` 未定义时返回 `404 Not Found` 属于正常行为。
- 没有阻塞 Unity HTTP 调用的问题。

## 开发中

### 《囚城营救》完善

- 细化三条路线的玩法差异
- 搭建与调整地图
- 改善玩家操作与打击感
- 梳理 Player 代码设计

### 能力建设

- 从“能看懂简单 C#”提升到“能修改并调试简单功能”
- 从“跟随教程写 Python”提升到“能独立完成小型 AI 服务”
- 学习基础 Git 工作流与提交规范

## 待开发

### 第一优先级：AI NPC 垂直切片

- [已完成] 设计第一位 AI NPC 的身份、性格、目标、秘密与状态
- [已完成] 用 Python 实现并验收可连续对话的 NPC 规则原型
- [已完成] DeepSeek 判断玩家意图
- [已完成] DeepSeek 根据已确定的规则结果生成胆小守卫台词
- [已完成] 让大模型与规则系统稳定输出固定 JSON
- [已完成] 创建 FastAPI 对话接口
  - [已完成] FastAPI 服务启动与 `GET /health` 健康检查
  - [已完成] 创建最低可用的 `POST /npc/chat`
- [已完成] Unity 通过 HTTP 调用 FastAPI
- [已完成] Unity AI 对话 UI
- [已完成] 真假路线影响游戏机制
  - [已验证] 首次成功对话后触发增加 20 秒
  - [已验证] 后续对话不会重复增加 20 秒
  - [已验证] `true_route` 显示往前第二个口子跳下去的暗道提示
  - [已验证] `false_route` 显示往上走的虚假路线提示
  - [后期开发] 真实情报降低指定守卫血量
- [已完成] Level1 完整整合
  - [已验证] AI 守卫对话 UI、倒计时和路线提示已放入 Level1
  - [已验证] 安抚与威胁能够在 Level1 产生不同路线提示
  - [已验证] 重开关卡后 Unity 与 Python 守卫状态按设计重置
  - [已验证] 普通剧情 NPC 不受 AI 守卫功能影响
  - [已验证] 玩家远离守卫时 AI 对话 UI 隐藏，靠近时显示
- [已完成] 测试、展示与作品集整理
  - [已完成] 安抚获得真路线的录制脚本
  - [已完成] 威胁获得假路线的录制脚本
  - [已完成] AI NPC 系统架构图与职责说明
  - [已完成] AI NPC 作品集项目介绍
  - [已完成] 真路线与假路线演示流程已确认可稳定运行
- 加入 NPC 信任度与历史互动
- 信任度达到条件后透露并开启隐藏路线
- 完成可录制、可讲解的作品集演示

### 第二优先级：RAG 游戏设定知识库

- [已完成] 本地设定问答与来源引用原型
  - [已完成] 精选设定文档切分与来源元数据
  - [已完成] NumPy 向量索引与 Top 3 检索
  - [已完成] 依据不足时拒绝编造
  - [已完成] 命令行连续问答
  - [已完成] 14 项自动测试与 3 个真实问题验收
  - [已完成] 安装并启用正式中文 Embedding 模型 `BAAI/bge-small-zh-v1.5`
- [已完成] 优化设定内容、检索输入与索引范围
  - [已完成] 将胆小守卫已确认设定拆为按玩家问题组织的单义片段
  - [已完成] 构建索引时让片段标题参与 Embedding
  - [已完成] 默认索引范围只包含专用已确认设定文档
  - [已验证] 五题同义改写 Top 3 检索全部通过
- [已完成] DeepSeek 真实回答验收
  - [已验证] 三个已确认问题均依据检索片段正确回答
  - [已验证] 未确认营救原因明确拒绝编造
  - [已验证] 四题均显示 `docs/rag_setting.md` 来源
- [已完成] 第一批核心剧情设定
  - [已完成] 明确项目为基于《九州缥缈录》原著人物与世界观的原创同人支线
  - [已完成] 确认姬野营救吕归尘、离国军囚禁与黎明前转移
  - [已完成] 确认找到吕归尘即通关，当前版本不包含护送逃离
  - [已验证] 五个剧情问题 Top 1 均命中正确片段
- [已完成] 三条主路基础设定
  - [已完成] 确认当前可用道路为三条主路：上路、中路和下方暗道路线
  - [已完成] 确认上路较长，敌人数量一般
  - [已完成] 确认中路长度一般，敌人数量略多
  - [已完成] 确认下方暗道路线长度正常，敌人最少，并通过胆小守卫真实情报发现
  - [已完成] 撤回不符合实际地图的“城堡外侧、侧门、正门上层、牢房区五区域”扩写
  - [已验证] 上路、中路和下方暗道路线问题 Top 3 均命中对应设定片段
- [已完成] 三条路线提示方式设定
  - [已完成] 确认上路入口通过更远、更绕、较长走廊、拐弯或远处火把提示路线较长
  - [已完成] 确认中路入口通过更多守卫或更密集的巡逻点提示敌人略多
  - [已完成] 确认下方暗道默认不明显，需要胆小守卫真实情报提示“往前第二个口子跳下去”
  - [已验证] 三个路线提示问题 Top 3 均命中对应设定片段
- [已完成] 三条路线敌人站位设定
  - [已完成] 确认上路前段敌人分散，主要是一个一个的守卫，后段有连续几个守卫站岗
  - [已完成] 确认中路敌人分布很多，有的地方有好几个守卫站岗
  - [已完成] 确认下方暗道只有暗道内部有一个站岗守卫
  - [已验证] 三个敌人站位问题 Top 3 均命中对应设定片段
- [已完成] 三条路线巡逻方式设定
  - [已完成] 确认上路前半段守卫分散站岗或短距离巡逻，后半段连续守卫偏固定站岗形成压力区
  - [已完成] 确认中路守卫更密集，部分位置有多个守卫同时站岗，玩家更容易战斗或等待空隙
  - [已完成] 确认下方暗道内部只有一个站岗守卫，不做复杂巡逻
  - [已验证] 三个巡逻方式问题 Top 3 均命中对应设定片段
- [已完成] 三条路线 Unity 场景核对清单
  - [已完成] 将上路、中路、下方暗道路线和提示方式拆成可逐项检查的 Unity 场景核对项
  - [已完成] 明确该清单只用于核对实际场景，不用于新增设定
  - [待验证] 需要进入 `D:\UnityProjects\project03` 的实际 Unity 场景逐项检查
- 整理角色、阵营、地图、任务与剧情设定
- 完成文档切分、Embedding 与向量检索
- 支持根据已有设定回答问题并引用来源
- 支持检查剧情设定冲突
- 支持根据已有设定生成支线任务

### 第三优先级：AI 关卡设计助手

- [已完成] 定义结构化关卡策划模板
- [已完成] 使用固定输入生成路线、敌人、奖励与设计意图
- [已完成] 创建本地命令行 MVP：`python -m level_designer.cli`
- [已完成] 为模板生成和命令行入口添加自动化测试
- [已完成] 接入 DeepSeek：`python -m level_designer.cli --provider deepseek`
- [已完成] DeepSeek API Key 只从环境变量 `DEEPSEEK_API_KEY` 读取，未设置时回退到本地模板
- [已完成] 接入 RAG：`python -m level_designer.cli --use-rag`
- [已完成] 将 RAG 检索到的已确认设定加入模板输出或 DeepSeek Prompt
- [已完成] 增加最低质量评价：`python -m level_designer.cli --evaluate`
- [已完成] 检查玩家目标、三条路线、风险收益和失败条件四项
- [已完成] 增加 JSON 输出：`python -m level_designer.cli --format json`
- [已完成] JSON 输出包含输入、Markdown 策划案、质量评价和回退提示
- 将《囚城营救》的三路线设计作为案例

### 第四优先级：Agent 与多 Agent 世界

- 为 NPC 定义可用工具、目标、状态与记忆
- 实现目标到规划、行动、反思的基础流程
- 建立警戒等级、牢门、钥匙、玩家声望等世界状态
- 实现守卫、囚犯、盗贼、商人等多个 Agent
- 限制 Agent 只能执行允许的游戏行为

## 当前风险

- Unity 项目尚未放入当前总仓库，无法自动检查版本与代码状态
- C# 与 Python 独立开发能力仍需通过实际功能逐步建立
- 地图路线差异尚未形成可验证的玩法
- 玩家打击感问题尚未拆解为具体指标
- AI 概念接触较多，但需要避免同时开发过多系统
- 已知瑕疵：退出并重新进入 Unity Play 模式后，Python 侧可能继续读取上一局的 `guard_state.json`，导致信任、恐惧、情绪和对话历史没有刷新。后续应在新一局开始时调用重置接口或清理本局状态文件。
- RAG 必须使用安装了 `sentence-transformers` 的虚拟环境运行；如果误用其他 Python，程序会退回本地文本向量，无法匹配已构建的 BGE 索引。
- AI 关卡设计助手已达到当前最低可用闭环：模板、DeepSeek、RAG、质量评价和 JSON 输出。继续扩展前应先确认是否真的需要网页或 Unity 工具读取。

## 阶段验收：正式中文 Embedding 模型

日期：2026-06-12

验收结论：

- 已在项目使用的 Python 虚拟环境中安装 `sentence-transformers 5.5.1`。
- 已下载并启用 `BAAI/bge-small-zh-v1.5`。
- 已使用 BGE 重建 26 个设定片段的索引，向量维度为 512。
- 14 项自动化测试全部通过。
- 同义改写问题“有什么近路能绕过看守？”能够正确检索到第二个口子下方的暗道。
- 部分宽泛问题仍会命中游戏设计概述，下一阶段优化设定内容与切片质量。

## 阶段验收：胆小守卫单义设定片段

日期：2026-06-13

完成内容：

- 将胆小守卫身份、安抚、威胁、真假路线条件和路线结果拆为独立设定片段。
- 新增 2 项设定边界测试，自动化测试总数增加到 16 项。
- 使用 BGE 重建 26 个设定片段的 512 维索引。

验收结果：

- 通过：近路绕过看守命中真实安全路线 Top 1。
- 通过：避开巡逻兵命中真实安全路线 Top 3。
- 通过：营救原因命中未确认设定 Top 1，并拒绝编造。
- 未通过：恐吓逃岗士兵的问题未在 Top 3 命中威胁结果或虚假路线。
- 未通过：让躲藏士兵愿意帮忙的问题未在 Top 3 命中安抚结果或真实路线条件。

结论：

- 当前阶段完成了设定内容整理，但五题检索验收未全部通过，因此检索质量优化继续保持开发中。
- 该阶段结束时确定下一步评估标题参与 Embedding；此方案已在后续阶段完成。

## 阶段验收：标题参与 Embedding

日期：2026-06-13

完成内容：

- 新增 `build_embedding_text()`，构建索引时将标题与正文组合为“标题：正文”。
- 查询、检索结果、答案正文和来源结构保持不变。
- 新增 2 项索引文本组合测试，自动化测试总数增加到 18 项。
- 使用 BGE 重建 26 个设定片段的 512 维索引。

验收结果：

- 五题同义改写检索从 3 项通过提升到 4 项通过。
- “恐吓那个逃岗士兵，他会怎么指路？”由未命中目标片段改善为虚假危险路线 Top 2。
- “如何让躲起来的士兵愿意帮忙？”仍未在 Top 3 命中安抚结果或真实路线条件。

结论：

- 标题参与 Embedding 的最低可用方案已完成并产生实际改善。
- 该阶段发现剩余问题主要受 `docs/game_design.md` 中通用玩法片段干扰；索引范围优化已在后续阶段完成。

## 阶段验收：专用设定索引范围

日期：2026-06-13

完成内容：

- 默认索引范围从完整策划案与专用设定文档，缩小为只包含 `docs/rag_setting.md`。
- `docs/game_design.md` 继续作为策划文档维护，不再直接进入设定问答索引。
- 新增默认索引范围测试，自动化测试总数增加到 19 项。
- 使用 BGE 重建 11 个专用设定片段的 512 维索引。

验收结果：

- 索引片段来源全部为 `docs/rag_setting.md`。
- 五题同义改写 Top 3 检索全部通过。
- “如何让躲起来的士兵愿意帮忙？”的真实路线条件进入 Top 3。
- 未确认营救原因继续命中未确认设定并拒绝编造。

结论：

- 当前语义检索最低可用阶段已完成，建议进入 DeepSeek 真实回答验收。
- 宽泛问题的 Top 1 排名仍有优化空间，但不阻塞下一阶段。

## 阶段验收：DeepSeek 真实回答

日期：2026-06-15

验收结果：

- 真实安全路线回答正确：往前第二个口子跳下去有暗道，几乎无人镇守。
- 威胁结果回答正确：降低信任、提高恐惧，并可能提供虚假路线。
- 获得真实路线条件回答正确：信任大于等于 50，并且信任大于等于恐惧。
- 未确认营救原因正确回答当前知识库没有足够信息。
- 四题均显示来源 `docs/rag_setting.md`。
- 在线回答过程中未出现 DeepSeek 调用失败。

结论：

- RAG 检索、DeepSeek 有依据回答、来源显示和未知信息拒答的最低可用流程已完成。
- 命令行会直接显示 DeepSeek 返回的 Markdown 加粗标记，但不阻塞下一阶段。
- 当前阶段已完成，建议进入高质量设定知识扩充。

## 阶段验收：第一批核心剧情设定

日期：2026-06-15

完成内容：

- 明确《囚城营救》是基于《九州缥缈录》原著人物与世界观创作的原创同人支线。
- 主角为姬野，营救目标为昔日战友吕归尘。
- 吕归尘在战争中被离国军俘获，被关押于离国边境城堡接受审问。
- 离国军将在黎明前把吕归尘转移至主力军营。
- 姬野找到吕归尘后关卡完成；倒计时结束前未找到则失败。
- 当前版本不包含找到吕归尘后的护送与逃离玩法。

验证结果：

- RAG 自动化测试增加到 20 项并全部通过。
- BGE 索引包含 17 个专用设定片段，向量维度为 512。
- 营救动机、囚禁势力与地点、限时原因、通关条件和护送边界五题的 Top 1 均命中正确片段。

结论：

- 第一批核心剧情设定已完成，不再将营救原因标记为未确认。
- 下一阶段扩充姬野与吕归尘的角色性格、离国边境城堡和关卡路线设定。

## 阶段验收：三条主路基础设定

日期：2026-06-16

完成内容：

- 确认当前关卡包含三条主路：上路、中路和下方暗道路线。
- 上路是玩家可以直接选择的正常路线，路线较长，敌人数量一般。
- 中路是玩家可以直接选择的正常路线，长度一般，敌人数量略多。
- 下方暗道路线是隐藏路线，长度正常，敌人最少，需要玩家先与胆小守卫对话并取得真实路线情报，才能得知往前第二个口子跳下去有一条暗道。
- 撤回不符合实际地图的“城堡外侧绕行区、正门与上层通道、侧门、暗道入口、牢房区”五区域扩写。

验证结果：

- RAG 自动化测试增加到 25 项并全部通过。
- BGE 索引包含 21 个专用设定片段，向量维度为 512。
- 上路、中路和下方暗道路线问题的 Top 3 均命中对应设定片段。

结论：

- 当前阶段已回到实际 Unity 地图约束：记录三条可用主路，不再凭空补侧门、外侧绕行或上层通道。
- 下一阶段建议继续确认三条路线的巡逻方式、提示方式或具体入口表现。

## 阶段验收：三条路线提示方式设定

日期：2026-06-16

完成内容：

- 确认上路入口看起来更远、更绕，可以用较长走廊、拐弯或远处火把表现，让玩家理解上路更长但敌人压力一般。
- 确认中路入口附近可以看到更多守卫或更密集的巡逻点，让玩家理解中路长度一般但敌人略多。
- 确认下方暗道默认不明显，需要通过胆小守卫真实情报得知“往前第二个口子跳下去”。

验证结果：

- RAG 自动化测试增加到 27 项并全部通过。
- BGE 索引包含 24 个专用设定片段，向量维度为 512。
- 上路提示、中路提示和下方暗道提示三个问题的 Top 3 均命中对应设定片段。

结论：

- 三条路线不仅有了长度和敌人数量差异，也有了最低可用的玩家提示方式。
- 下一阶段建议扩充具体巡逻逻辑或在 Unity 地图中对照检查入口表现。

## 阶段验收：三条路线敌人站位设定

日期：2026-06-17

完成内容：

- 确认上路敌人开始很分散，主要是一个一个的守卫，后面会有连续几个守卫站岗。
- 确认中路敌人分布很多，有的地方有好几个守卫站岗。
- 确认下方暗道只有暗道内部有一个站岗的守卫。

验证结果：

- RAG 自动化测试增加到 29 项并全部通过。
- BGE 索引包含 27 个专用设定片段，向量维度为 512。
- 上路、中路和下方暗道敌人站位三个问题的 Top 3 均命中对应设定片段。

结论：

- 三条路线已经具备最低可用的长度、敌人数量、提示方式和敌人站位设定。
- 下一阶段建议检查这些设定是否与实际 Unity 场景摆放一致，或继续扩充具体巡逻逻辑。

## 阶段验收：三条路线巡逻方式设定

日期：2026-06-17

完成内容：

- 确认上路前半段守卫主要是分散站岗或短距离巡逻，玩家可以逐个观察和处理；后半段连续几个守卫更偏固定站岗，形成一段压力区。
- 确认中路守卫更密集，部分位置有多个守卫同时站岗，表现为正面压力较高的路线；玩家更容易被迫战斗或等待空隙。
- 确认下方暗道内部只有一个站岗守卫，不做复杂巡逻；玩家获得真实情报后，主要挑战是找到暗道入口，而不是连续战斗。

验证结果：

- RAG 自动化测试增加到 31 项并全部通过。
- BGE 索引包含 30 个专用设定片段，向量维度为 512。
- 上路、中路和下方暗道巡逻方式三个问题的 Top 3 均命中对应设定片段。

结论：

- 三条路线已经具备最低可用的长度、敌人数量、提示方式、敌人站位和巡逻方式设定。
- 下一阶段建议对照实际 Unity 场景检查文档是否与敌人摆放一致，或继续补入口表现与录制说明。

## 阶段验收：三条路线 Unity 场景核对清单

日期：2026-06-17

完成内容：

- 在 `docs/game_design.md` 中新增 Unity 场景核对清单。
- 核对清单覆盖上路、中路、下方暗道路线和提示方式四类内容。
- 清单用于进入 Unity 场景后检查路线长度、敌人站位、巡逻压力和提示方式是否与文档一致。

验证结果：

- 已确认核对清单写入 `docs/game_design.md`。
- 本阶段未修改 RAG 索引内容，因此无需重建 RAG 索引。

结论：

- 当前路线设定的文档阶段已完成，下一步应进入实际 Unity 项目 `D:\UnityProjects\project03` 核对场景。
- 如果 Unity 场景与文档不一致，应优先以实际场景和用户确认为准修正文档或关卡。

## 阶段验收：AI 关卡设计助手 MVP

日期：2026-06-17

完成内容：

- 新增 `level_designer` Python 包。
- 新增 `LevelDesignInput` 数据输入结构。
- 新增 `generate_level_plan()`，可以根据关卡主题、玩家目标、难度和三条路线资料生成固定 Markdown 策划案。
- 新增命令行入口 `python -m level_designer.cli`。
- 第一版输出包含玩家目标、三条路线设计、敌人配置、风险与奖励、失败条件、设计意图和优化建议。

验证结果：

- `D:\develop\pythons\.venv\Scripts\python.exe -m unittest discover -s level_designer/tests -v` 通过，3 项测试全部成功。

结论：

- AI 关卡设计助手的最低可用命令行版本已完成。
- 当前阶段不继续扩写模板或增加复杂功能。
- 下一阶段建议二选一：接入 DeepSeek 生成自然语言策划案，或先做关卡质量评价规则。

## 阶段验收：AI 关卡设计助手 DeepSeek 接入版

日期：2026-06-17

完成内容：

- 新增 `level_designer/deepseek_client.py`。
- 新增 DeepSeek OpenAI 兼容接口调用，默认模型为 `deepseek-chat`。
- 新增 `build_level_design_prompt()`，把关卡主题、玩家目标、难度和三条路线资料组织成固定栏目 Prompt。
- 新增 `generate_plan_with_deepseek()`，由 DeepSeek 生成 Markdown 关卡策划案。
- 命令行新增 `--provider template|deepseek` 和 `--model` 参数。
- DeepSeek API Key 只从环境变量 `DEEPSEEK_API_KEY` 读取。
- 未设置 API Key 或调用失败时，工具回退到本地模板。

验证结果：

- `D:\develop\pythons\.venv\Scripts\python.exe -m unittest discover -s level_designer/tests -v` 通过，6 项测试全部成功。
- 已验证缺少 `DEEPSEEK_API_KEY` 时，`--provider deepseek` 会提示未启用并回退到本地模板。

结论：

- DeepSeek 接入版最低可用流程已完成。
- 当前阶段不继续扩写 Prompt 或增加复杂质量评价。
- 下一阶段建议进入“关卡质量评价规则”或“RAG 接入关卡助手”。

## 阶段验收：AI 关卡设计助手 RAG 接入版

日期：2026-06-17

完成内容：

- 新增 `level_designer/rag_context.py`。
- 新增 `build_rag_query()`，构造路线设定检索问题。
- 新增 `retrieve_rag_context()`，读取现有 RAG 索引并检索路线相关设定。
- 新增 `format_rag_matches()`，把检索片段整理为关卡助手可使用的设定依据。
- `LevelDesignInput` 新增可选字段 `rag_context`。
- 命令行新增 `--use-rag`。
- 本地模板输出新增 `RAG 设定依据` 区块。
- DeepSeek Prompt 会在存在 RAG 设定时优先要求模型遵守该依据。

验证结果：

- `D:\develop\pythons\.venv\Scripts\python.exe -m unittest discover -s level_designer/tests -v` 通过，10 项测试全部成功。
- `D:\develop\pythons\.venv\Scripts\python.exe -m unittest discover -s rag/tests -v` 通过，31 项测试全部成功。
- `--use-rag` 实际试运行已命中路线相关片段：三条潜入路线总览、下方暗道路线和上路。

结论：

- RAG 接入关卡助手的最低可用流程已完成。
- 当前阶段不继续扩写 RAG 内容，也不继续打磨 Prompt。
- 下一阶段建议进入“关卡质量评价规则”，检查生成策划案是否满足路线差异、风险收益和失败条件清晰。

## 阶段验收：AI 关卡设计助手质量评价版

日期：2026-06-17

完成内容：

- 新增 `level_designer/evaluator.py`。
- 新增 `EvaluationResult`，保存通过状态、通过数量、总检查数量和改进建议。
- 新增 `evaluate_level_plan()`，检查玩家目标、三条路线、风险收益和失败条件四项。
- 新增 `format_evaluation_report()`，输出固定 Markdown 质量评价报告。
- 命令行新增 `--evaluate`。
- `--evaluate` 可以与本地模板、RAG、DeepSeek 生成流程组合使用。

验证结果：

- `D:\develop\pythons\.venv\Scripts\python.exe -m unittest discover -s level_designer/tests -v` 通过，14 项测试全部成功。
- `D:\develop\pythons\.venv\Scripts\python.exe -m unittest discover -s rag/tests -v` 通过，31 项测试全部成功。
- `--evaluate` 实际试运行输出 `质量评价` 区块，最低检查结果为 `通过：4 / 4`。
- `--use-rag --evaluate` 实际试运行可以同时输出 RAG 设定依据和质量评价。

结论：

- AI 关卡设计助手的本地模板、DeepSeek、RAG 和最低质量评价闭环已完成。
- 当前阶段不继续扩写评价规则或复杂评分。
- 下一阶段建议进入 JSON 输出版本，方便未来网页或 Unity 工具读取；也可以暂时停止关卡助手阶段，转向 Unity 关卡实装检查。

## 阶段验收：AI 关卡设计助手 JSON 输出版

日期：2026-06-17

完成内容：

- 新增 `level_designer/json_output.py`。
- 新增 `build_json_output()`，将输入、生成方式、Markdown 策划案、质量评价和提示信息组织成结构化字典。
- 新增 `format_json_output()`，使用 `ensure_ascii=False` 输出中文可读 JSON。
- 命令行新增 `--format markdown|json`。
- DeepSeek 未配置或调用失败时，JSON 输出会把提示放入 `warnings`，不污染 JSON 结构。

验证结果：

- `D:\develop\pythons\.venv\Scripts\python.exe -m unittest discover -s level_designer/tests -v` 通过，18 项测试全部成功。
- `D:\develop\pythons\.venv\Scripts\python.exe -m unittest discover -s rag/tests -v` 通过，31 项测试全部成功。
- `--format json --evaluate` 实际试运行成功，输出包含 `provider`、`input`、`plan_markdown`、`evaluation` 和 `warnings`。
- `--format json --provider deepseek` 在未设置 API Key 时实际试运行成功，回退提示进入 `warnings`。

结论：

- AI 关卡设计助手的当前最低可用闭环已完成：本地模板、DeepSeek、RAG、质量评价和 JSON 输出。
- 当前阶段不继续扩写关卡助手。
- 下一阶段建议暂停关卡助手，转向 Unity 关卡实装检查。

## 阶段验收：Unity Level1 场景静态核对

日期：2026-06-17

完成内容：
- 确认实际 Unity 项目位置为 `D:\UnityProjects\project03`。
- 确认 Unity 工程版本为 `2022.3.62f3`。
- 确认当前主要关卡场景位于 `D:\UnityProjects\project03\Assets\scens\Level1.unity`。
- 静态读取 `Level1.unity`，确认场景中存在 `AIguard`、`AIGuardDialogueSystem`、`AIGuardInteractionZone`、多个 `Enemy`、多个 `CheckPoint` 和多个 `sceneportal`。
- 按敌人坐标初步判断，当前 Level1 已有上、中、下多层敌人分布。

核对发现：
- AI NPC 与路线提示相关对象已经出现在 Level1 中，说明胆小守卫垂直切片不是单独游离的原型。
- 当前下方区域静态读取到多名 `Enemy`，与“下方暗道内部只有一个站岗守卫”的设计目标疑似不一致。
- 当前无法仅凭 YAML 静态读取完全确认三条路线的可走性、入口显眼程度和玩家实际体验，必须进入 Unity 编辑器或 Play 模式复核。

验证方式：
- 读取 `D:\UnityProjects\project03\ProjectSettings\ProjectVersion.txt`。
- 静态解析 `D:\UnityProjects\project03\Assets\scens\Level1.unity` 中 GameObject 名称、Transform 坐标和脚本 GUID 挂载关系。
- Unity MCP 连续超时，本阶段没有直接修改 Unity 场景。

结论：
- Unity 关卡实装核对的最低可用检查已完成。
- 当前阶段不继续扩写关卡助手，也不直接手改 Unity YAML。
- 原建议下一阶段进入 Unity 编辑器调整敌人摆放，但用户已于 2026-06-23 明确要求“这一步跳过”，因此该调整不再作为当前阻塞项。

## 阶段决策：跳过 Unity Level1 敌人摆放调整

日期：2026-06-23

决策内容：
- 跳过 Unity 编辑器中的 Level1 三条路线敌人摆放调整。
- 不在当前阶段处理下方暗道敌人数量疑似过多的问题。
- 该问题保留为后续关卡打磨项，不阻塞 AI 与 RAG 功能继续推进。

下一阶段：
- 进入 RAG 接入 AI NPC。
- 目标是让 AI NPC 在回答世界观、角色、地点、任务等问题时，可以先检索 `docs/rag_setting.md` 中的已确认设定，并在回答中保持来源依据。
- 最低可用版本只做后端/Python 侧验证，不提前做 Unity UI 或复杂长期记忆。

## 阶段验收：RAG 接入 AI NPC Python 适配层

日期：2026-06-23

完成内容：
- 新增 `ai_npc` Python 包。
- 新增 `ai_npc/rag_context.py`，把玩家问题整理为 AI NPC 世界观问答检索 query。
- 新增 `format_npc_rag_context()`，把 RAG 命中片段整理为 NPC 可用的设定依据。
- 新增 `answer_npc_world_question()`，复用现有 `rag.answer_service.answer_question()`，在证据不足时返回统一拒答。
- 新增 `answer_npc_with_rag()`，可以读取现有 RAG 索引并返回 NPC 回复、来源、命中片段和是否使用 RAG 的状态。
- 新增 `ai_npc/tests/test_rag_context.py`，覆盖 query 构造、证据格式化、证据不足拒答和证据充足返回来源。

验证方式：
- `D:\develop\pythons\.venv\Scripts\python.exe -m unittest ai_npc.tests.test_rag_context -v` 通过，4 项测试成功。
- 实际运行 `answer_npc_with_rag("真正安全的路线在哪里？", api_key="")`，返回往前第二个口子跳下去的暗道设定，来源为 `docs/rag_setting.md`，`used_rag` 为 `True`。

结论：
- RAG 接入 AI NPC 的最低可用 Python 适配层已完成。
- 当前阶段不提前制作 Unity UI，也不加入复杂长期记忆。
- 当前仓库内尚未修改外部 FastAPI 项目 `D:\develop\pythons`，下一阶段如继续，应把该适配层接入实际 `/npc/chat` 或新增世界观问答接口。

## 阶段验收：RAG 接入外部 FastAPI

日期：2026-06-23

完成内容：
- 在外部 FastAPI 项目 `D:\develop\pythons\api.py` 中新增 `WorldQuestionRequest`。
- 新增 `POST /npc/world_qa` 世界观问答接口。
- 新增 `load_answer_npc_with_rag()`，通过 `COEDX_LEARNING_ROOT` 或默认路径 `C:\Users\eurp\Documents\coedx_learning` lazy import 当前仓库的 `ai_npc.rag_context`。
- 新增 `answer_world_question()`，让外部服务复用当前仓库 RAG 适配层。
- 保持 `POST /npc/chat`、`ChatRequest`、`chat_once()`、守卫状态保存和真假路线逻辑不变。
- 新增外部测试文件 `D:\develop\pythons\test_api_rag.py`。

验证方式：
- `D:\develop\pythons\.venv\Scripts\python.exe -m unittest D:\develop\pythons\test_api_rag.py -v` 通过，3 项测试成功。
- 路径导入命令返回 `True`，确认外部虚拟环境可以导入当前仓库的 `ai_npc.rag_context`。
- 使用 FastAPI `TestClient` 调用 `POST /npc/world_qa`，问题为“真正安全的路线在哪里？”，返回 HTTP `200`、`used_rag=True`、来源 `docs/rag_setting.md`，回复包含“往前第二个口子跳下去”的暗道设定。

结论：
- RAG 已完成到外部 FastAPI 的最低可用接入。
- 当前阶段没有改 Unity UI，也没有改现有 `/npc/chat` 请求结构。
- 下一阶段如果继续，可以选择用 Unity 或独立调试工具调用 `/npc/world_qa` 做展示。

## 阶段验收：RAG 世界观问答最小调用演示

日期：2026-06-23

完成内容：
- 在外部 FastAPI 项目 `D:\develop\pythons` 新增 `world_qa_demo.py`。
- 新增 `test_world_qa_demo.py`，覆盖演示脚本调用 `/npc/world_qa`、格式化回答和命令行输出。
- 演示脚本使用 FastAPI `TestClient` 在进程内调用接口，不需要先启动 uvicorn，也不接 Unity UI。
- 演示输出会显示问题、回答、是否使用 RAG 和来源文档。

验证方式：
- `D:\develop\pythons\.venv\Scripts\python.exe -m unittest test_world_qa_demo.py -v` 通过：3 项测试成功。
- `D:\develop\pythons\.venv\Scripts\python.exe -m unittest test_api_rag.py -v` 通过：3 项测试成功。
- `D:\develop\pythons\.venv\Scripts\python.exe D:\develop\pythons\world_qa_demo.py` 实际返回暗道设定，`used_rag=True`，来源为 `docs/rag_setting.md`。

结论：
- `/npc/world_qa` 已具备可录制、可讲解的最小演示方式。
- 当前阶段不继续扩写 Unity UI、不改 `/npc/chat`，也不加入长期记忆。
- 下一步应进入新的阶段，而不是继续打磨 RAG 世界观问答演示。

## 阶段验收：Tool Calling / Memory 最小原型

日期：2026-06-23

完成内容：
- 新增 `agent_workflow` Python 包。
- 新增 `call_tool()`，只允许调用白名单工具。
- 新增 `get_route_info`、`check_game_state` 和 `update_quest_hint` 三个最小工具能力。
- 新增 `create_initial_memory()` 和 `record_memory()`，用于记录本局玩家关键行为。
- 新增 `run_agent_turn()`，根据玩家输入选择受限工具，并返回回复、工具调用记录、记忆和游戏状态。
- 新增 `agent_workflow.cli` 命令行演示。
- 新增 `docs/agent_workflow.md` 记录本阶段边界。

验证方式：
- `D:\develop\pythons\.venv\Scripts\python.exe -m unittest agent_workflow.tests.test_tool_calling_memory -v` 通过：4 项测试成功。
- `D:\develop\pythons\.venv\Scripts\python.exe -m agent_workflow.cli` 实际输出路线回复、工具名 `get_route_info` 和记忆数量。

结论：
- Tool Calling / Memory 阶段已经达到最小可行原型：Agent 能调用白名单工具，拒绝未授权工具，并写入本局记忆。
- 当前阶段不接真实 MCP、不接 Unity、不接 RAG、不做 LangGraph，也不做长期记忆文件。
- 下一步应进入新阶段，而不是继续扩写本原型。

## 阶段验收：Agent Workflow 接入 FastAPI 最小接口

日期：2026-06-23

完成内容：
- 在外部 FastAPI 项目 `D:\develop\pythons\api.py` 中新增 `AgentTurnRequest`。
- 新增 `POST /agent/turn` 接口，接收 `player_message`。
- 新增 `load_run_agent_turn()`，通过 `COEDX_LEARNING_ROOT` 或默认路径 `C:\Users\eurp\Documents\coedx_learning` lazy import 当前仓库的 `agent_workflow.prototype.run_agent_turn`。
- 新增 `run_agent_turn_from_workflow()`，让外部服务复用当前仓库的 Tool Calling / Memory 原型。
- 保持 `GET /health`、`POST /npc/chat` 和 `POST /npc/world_qa` 的现有行为不变。
- 在外部测试文件 `D:\develop\pythons\test_api_rag.py` 中新增 `/agent/turn` 接口测试。

验证方式：
- 先运行失败测试，确认 `/agent/turn` 未实现时返回 `404`。
- `D:\develop\pythons\.venv\Scripts\python.exe -m unittest test_api_rag.py -v` 通过：4 项测试成功。

结论：
- Agent Workflow 已完成到外部 FastAPI 的最低可用接入。
- 当前阶段不接 Unity、不接真实 MCP、不接 LangGraph，也不做跨请求长期记忆。
- 下一步应进入新阶段，而不是继续打磨 `/agent/turn`。

## 阶段验收：真实 MCP 最小服务

日期：2026-06-23

完成内容：
- 新增 `agent_workflow/mcp_server.py`。
- 使用 stdio JSON-RPC 实现 MCP 最小服务，不依赖外部 MCP SDK。
- 支持 `initialize`，返回服务信息和工具能力。
- 支持 `tools/list`，返回当前暴露的工具清单。
- 支持 `tools/call`，调用 `get_route_info` 工具。
- 复用 `agent_workflow.prototype.call_tool()` 的白名单规则，未授权工具会返回 `isError: true`。
- 新增 `agent_workflow/tests/test_mcp_server.py`，覆盖初始化、工具列表、工具调用、未知工具拒绝、单行 JSON-RPC 处理、多请求 stdio 输出和 Windows 管道前缀兼容。

验证方式：
- 先运行失败测试，确认 `agent_workflow.mcp_server` 不存在时测试失败。
- `D:\develop\pythons\.venv\Scripts\python.exe -m unittest agent_workflow.tests.test_mcp_server -v` 通过：8 项测试成功。

结论：
- 真实 MCP 最小服务已经达到当前阶段最低可用度：可以通过 MCP 风格的 JSON-RPC 暴露一个受控工具，并保持白名单边界。
- 当前阶段不接 Unity、不接 LangGraph、不扩展更多工具、不做复杂长期记忆。
- 下一步应进入新阶段，而不是继续打磨 MCP 服务。

## 阶段验收：MCP 服务启动说明与配置示例

日期：2026-06-24

完成内容：
- 新增 `agent_workflow/mcp_client_config.example.json`。
- 在 `docs/agent_workflow.md` 中补充 MCP 客户端配置示例。
- 在 `docs/agent_workflow.md` 中补充 MCP 演示步骤。
- 明确 `cwd` 的作用：从当前仓库根目录启动服务，保证 Python 能找到 `agent_workflow.mcp_server`。

验证方式：
- `D:\develop\pythons\.venv\Scripts\python.exe -m json.tool agent_workflow/mcp_client_config.example.json` 通过，确认配置示例是合法 JSON。
- `D:\develop\pythons\.venv\Scripts\python.exe -m unittest discover -s agent_workflow/tests -v` 通过：12 项测试成功。

结论：
- MCP 服务已经具备最小启动说明和配置示例。
- 当前阶段不继续扩展 MCP 工具，不接 Unity，不做完整客户端集成。
- 下一步应进入新阶段。

## 阶段验收：MCP 第二个只读工具 check_game_state

日期：2026-06-24

完成内容：
- 在 `agent_workflow/mcp_server.py` 中新增 `check_game_state` 的 MCP 工具声明。
- `tools/list` 现在会返回 `get_route_info` 和 `check_game_state`。
- `tools/call` 可以调用 `check_game_state`，参数为空 `{}`。
- `check_game_state` 复用现有 `call_tool()` 白名单逻辑，只读取默认游戏状态。
- `check_game_state` 返回内容包含 `remaining_time`、`has_key` 和 `quest_hint`。
- 更新 `agent_workflow/tests/test_mcp_server.py`，覆盖工具列表和工具调用结果。

验收标准：
- `tools/list` 能看到 `check_game_state`。
- `tools/call` 能调用 `check_game_state`。
- 返回内容包含剩余时间、钥匙状态和任务提示。

验证方式：
- 先运行失败测试，确认 `tools/list` 尚未暴露 `check_game_state` 时测试失败。
- `D:\develop\pythons\.venv\Scripts\python.exe -m unittest agent_workflow.tests.test_mcp_server -v` 通过：9 项测试成功。

结论：
- MCP 第二个只读工具已经达到当前阶段最低可用度。
- 当前阶段不暴露 `update_quest_hint`，不允许 MCP 修改任务状态，不接 Unity，不做长期记忆。
- 下一步应进入新阶段。

## 阶段验收：MCP 命令行演示脚本

日期：2026-06-24

完成内容：
- 新增 `agent_workflow/mcp_demo.py`。
- 新增 `agent_workflow/tests/test_mcp_demo.py`。
- 演示脚本在进程内调用 `agent_workflow.mcp_server.handle_request()`。
- 演示 `tools/list`，输出 `get_route_info` 和 `check_game_state`。
- 演示 `tools/call get_route_info`，输出下方暗道路线。
- 演示 `tools/call check_game_state`，输出默认游戏状态。
- 更新 `docs/agent_workflow.md`，补充演示命令和预期输出。

验收标准：
- 演示脚本能展示工具列表。
- 演示脚本能展示路线工具结果。
- 演示脚本能展示游戏状态工具结果。

验证方式：
- 先运行失败测试，确认 `agent_workflow.mcp_demo` 不存在时测试失败。
- `D:\develop\pythons\.venv\Scripts\python.exe -m unittest agent_workflow.tests.test_mcp_demo -v` 通过：3 项测试成功。
- `D:\develop\pythons\.venv\Scripts\python.exe -m agent_workflow.mcp_demo` 实际输出工具列表、路线工具结果和游戏状态工具结果。

结论：
- MCP 命令行演示脚本已经达到当前阶段最低可用度。
- 当前阶段不接真实 MCP 客户端，不新增工具，不接 Unity。
- 下一步应进入新阶段。

## 阶段验收：Agent Workflow 阶段作用说明

日期：2026-06-24

完成内容：
- 新增 `docs/agent_workflow_stage_roles.md`。
- 按阶段说明 Tool Calling / Memory 本地原型、命令行演示、FastAPI 接口、MCP 服务、MCP 配置示例、第二个只读工具、MCP 演示脚本和阶段说明本身的作用。
- 为每个阶段补充对应游戏意义和作品集讲法。
- 在 `docs/agent_workflow.md` 中加入阶段作用说明文档链接。

验收标准：
- 能说明每个阶段解决什么问题。
- 能说明每个阶段为什么不提前扩展高级功能。
- 能作为录屏、答辩或面试讲解材料使用。

验证方式：
- `Select-String -Path docs/agent_workflow_stage_roles.md -Pattern "阶段 1","阶段 8","作品集讲法"` 通过，确认关键段落存在。
- `D:\develop\pythons\.venv\Scripts\python.exe -m unittest discover -s agent_workflow/tests -v` 通过：16 项测试成功。
- `git diff --check -- docs/agent_workflow_stage_roles.md docs/agent_workflow.md docs/progress.md HANDOVER.md docs/tech_decision.md` 通过。
- `Select-String -Path docs/agent_workflow_stage_roles.md,docs/agent_workflow.md,docs/progress.md,HANDOVER.md,docs/tech_decision.md -Pattern "[ \t]$"` 无输出，确认本次文档没有尾随空白。

结论：
- Agent Workflow 这一组阶段已经有可讲解的作品集说明。
- 当前阶段不继续扩写 MCP 工具、不接 Unity、不做 LangGraph。
- 下一步应进入新的功能阶段。

## 阶段验收：RAG 设定冲突检查器最小原型

日期：2026-06-24

完成内容：
- 新增 `rag/conflict_checker.py`。
- 新增 `rag/check_conflict.py` 命令行入口。
- 新增 `rag/tests/test_conflict_checker.py`。
- 复用现有 RAG 索引检索最相关的已确认设定片段。
- 第一版使用规则判断明显冲突，例如“下方暗道只有一个守卫”和“下方暗道有多个守卫”之间的冲突。
- 输出包含结论、冲突原因、来源文档和相关设定片段。

验收标准：
- 输入一段候选设定文本。
- 能检索最相关的已确认设定片段。
- 能输出“可能冲突 / 暂未发现明显冲突 / 证据不足”。
- 能显示来源片段。
- 第一版只做 Python 函数和命令行，不接 Unity，不调用大模型自动改设定。

验证方式：
- 先运行失败测试，确认 `rag.conflict_checker` 不存在时测试失败。
- `D:\develop\pythons\.venv\Scripts\python.exe -m unittest rag.tests.test_conflict_checker -v` 通过：4 项测试成功。
- `D:\develop\pythons\.venv\Scripts\python.exe -m unittest discover -s rag/tests -v` 通过：35 项测试成功。
- `D:\develop\pythons\.venv\Scripts\python.exe -m rag.check_conflict "新增设定：下方暗道内部有多个守卫来回巡逻。"` 可以输出可能冲突、守卫数量冲突原因和 `docs/rag_setting.md` 来源片段。

结论：
- RAG 设定冲突检查器已经达到当前阶段最低可用度。
- 当前阶段不继续扩展更多冲突规则，不接 Unity，不调用大模型，不自动修改设定。
- 下一步应进入新的功能阶段。

## 阶段验收：RAG 冲突检查器作品集演示说明

日期：2026-06-24

完成内容：
- 新增 `docs/rag_conflict_checker_demo.md`。
- 说明 RAG 冲突检查器解决的问题。
- 补充可直接录屏的演示命令。
- 补充预期输出重点、录屏讲解顺序、面试讲法和当前边界。
- 在 `docs/rag.md` 和 `rag/README.md` 中加入演示说明文档链接。

验收标准：
- 能说明冲突检查器为什么存在。
- 能展示一条可运行命令。
- 能解释“可能冲突”的来源依据。
- 能说明第一版不自动修改设定、不替代人工策划判断。

验证方式：
- `Select-String -Path docs/rag_conflict_checker_demo.md -Pattern "演示命令","面试讲法","当前边界"` 通过。
- `D:\develop\pythons\.venv\Scripts\python.exe -m unittest discover -s rag/tests -v` 通过：35 项测试成功。
- `git diff --check -- docs/rag_conflict_checker_demo.md docs/rag.md rag/README.md docs/progress.md HANDOVER.md docs/tech_decision.md` 通过。

结论：
- RAG 冲突检查器已经具备可录屏、可答辩、可面试讲解的说明材料。
- 当前阶段不继续扩展冲突规则，也不继续扩写讲解稿。
- 下一步应进入新的功能阶段。

## 阶段验收：Unity Level1 三路线一致性静态核对

日期：2026-06-24

完成内容：
- 新增 `docs/unity_level1_route_audit.md`。
- 静态读取实际 Unity 工程 `D:\UnityProjects\project03`。
- 确认 Unity 版本为 `2022.3.62f3`。
- 确认 `D:\UnityProjects\project03\Assets\scens\Level1.unity` 存在。
- 确认 Level1 中存在 `AIguard`、`AIGuardDialogueSystem`、`AIGuardInteractionZone` 和 `Route Hint Text`。
- 静态读取到 25 个 `Enemy` 对象。
- 发现 y 约为 `-37` 的下方层级存在 `Enemy (3)`、`Enemy (4)`、`Enemy (6)` 三个敌人。

验收标准：
- 能说明当前三条路线设定目标。
- 能说明 Level1 中已确认存在的 AI 守卫和路线提示对象。
- 能指出下方暗道敌人数量的待复核点。
- 不直接手改 `.unity` YAML。

验证方式：
- `Test-Path D:\UnityProjects\project03\ProjectSettings\ProjectVersion.txt` 返回 `True`。
- `Get-Content D:\UnityProjects\project03\ProjectSettings\ProjectVersion.txt` 显示 `2022.3.62f3`。
- `Test-Path D:\UnityProjects\project03\Assets\scens\Level1.unity` 返回 `True`。
- `Select-String` 静态检索确认 `AIguard`、`AIGuardInteractionZone`、`Route Hint Text` 和多个 `Enemy` 存在。
- 静态坐标提取确认 `Enemy (3)`、`Enemy (4)`、`Enemy (6)` 位于 y 约为 `-37` 的下方层级。
- Unity MCP `get_scene_info` 本次超时，未作为验收依据。

结论：
- 当前阶段已经达到最低可用度：确认了 Level1 中的 AI 守卫对象、路线提示 UI 和下方层级敌人待复核问题。
- 当前阶段不直接修改 Unity 场景。
- 下一阶段应进入 Unity 编辑器 Scene 视图，确认 `Enemy (3)`、`Enemy (4)`、`Enemy (6)` 是否都在下方暗道内部。

## 阶段验收：Unity 下方暗道敌人归属复核准备

日期：2026-06-24

完成内容：
- 尝试通过 Unity MCP 直接读取 `Enemy (3)`。
- Unity MCP `get_gameobject` 等待 300 秒后超时，未能取得编辑器实时对象数据。
- 在 `docs/unity_level1_route_audit.md` 中补充 Unity 编辑器人工复核清单。
- 明确下一步只需要确认 `Enemy (3)`、`Enemy (4)`、`Enemy (6)` 是否属于下方暗道内部。

验收标准：
- 不把静态 y 坐标直接判定为暗道内部归属。
- 不直接手改 `.unity` YAML。
- 给出可以在 Unity Scene 视图中执行的最小复核步骤。

验证方式：
- Unity MCP `get_gameobject Enemy (3)` 超时，未作为场景事实依据。
- 文档已记录人工复核对象和判断格式。

结论：
- 当前阶段达到最低可用度：已经确认实时工具暂不可用，并把下一步收束为人工 Scene 视图复核。
- 本阶段不移动、不删除、不新增敌人。
- 下一步需要用户在 Unity 编辑器里确认 3 个敌人的归属后，再决定是否做最小场景调整。

## 阶段验收：Unity 下方暗道敌人归属人工复核

日期：2026-06-24

完成内容：
- 根据 Unity 编辑器人工复核，确认 `Enemy (3)`、`Enemy (4)`、`Enemy (6)` 都位于暗道内部的陷阱里面，不会出来。
- 明确这 3 个敌人不按“暗道可走路径上的站岗守卫”计算。
- 更新 `docs/unity_level1_route_audit.md`、`docs/game_design.md` 和 `docs/rag_setting.md`，区分陷阱敌人与站岗守卫。

验收标准：
- 能解释为什么静态读取到 3 个下方敌人不一定构成设定冲突。
- 能说明陷阱里的敌人与可走路径上的站岗守卫不是同一种关卡压力。
- 不移动、不删除、不新增 Unity 场景敌人。

验证方式：
- 用户在 Unity 编辑器中人工确认：`Enemy (3)`、`Enemy (4)`、`Enemy (6)` 都在暗道内部陷阱中，不会出来。
- 文档已记录陷阱敌人与站岗守卫的区别。

结论：
- 当前阶段已完成，达到最小可行度。
- 下方暗道敌人数量暂不阻塞下一阶段。
- 下一步应进入新的最小阶段，不继续打磨下方暗道敌人归属。

## 阶段验收：Unity Level1 路线整体体验最小核对准备

日期：2026-06-24

完成内容：
- 新增 `docs/unity_level1_route_experience_audit.md`。
- 静态整理 `Level1.unity` 中 `AIguard`、`CheckPoint` 和主要敌人层级坐标。
- 确认 Level1 已经具备上方、中部、下方三个路线层级。
- 明确仅靠静态坐标不能判断玩家实际路径长度、敌人压力和暗道入口可见性。
- 将下一次 Unity 复核压缩为三个问题：上路是否更绕、中路是否压力更集中、暗道入口是否需要真实情报才能理解。

验收标准：
- 能说明哪些路线体验已经有静态证据支持。
- 能说明哪些体验必须通过 Unity Scene 视图或实际游玩确认。
- 不修改 Unity 场景，不移动敌人，不调整战斗数值。

验证方式：
- 只读提取 `Level1.unity` 中 `Enemy`、`CheckPoint` 和 `AIguard` 坐标。
- 文档记录上/中/下层级证据和下一阶段复核问题。

结论：
- 当前阶段已达到最低可用度：路线体验核对的证据、边界和下一步问题已经明确。
- 下一步需要在 Unity 编辑器或实际游玩中回答三个体验问题。

## 阶段验收：Unity Level1 路线整体体验实测复核

日期：2026-06-24

完成内容：
- 用户在 Unity 编辑器或实际游玩中确认：上路明显更绕或更耗时。
- 用户确认：中路更容易看到密集守卫或形成集中压力。
- 用户确认：下方暗道入口默认不明显，但听到“往前第二个口子跳下去”后能找到。
- 更新 `docs/unity_level1_route_experience_audit.md` 和 `docs/game_design.md`，记录三条路线的实测复核结论。

验收标准：
- 上路、中路、下方暗道三条路线都具有可感知差异。
- 复核只确认最低可用体验，不继续扩展路线、不重摆敌人、不调整数值。
- 下方暗道入口与胆小守卫真实情报形成可理解联动。

验证方式：
- 用户在 Unity 编辑器或实际游玩中给出三项确认结果。
- 文档已记录实测结论。

结论：
- 当前阶段已完成，达到最小可行度。
- Level1 三路线体验差异暂不阻塞下一阶段。
- 下一步应进入新的最小阶段，不继续打磨路线整体体验。

## 阶段验收：AI 守卫路线提示录屏脚本最小复核

日期：2026-06-24

完成内容：
- 新增 `docs/ai_guard_route_recording_checklist.md`。
- 将录屏链路压缩为：靠近胆小守卫、安抚并询问路线、获得真实情报、看到路线提示、离开守卫、找到下方暗道入口。
- 在 `docs/ai_npc.md` 的演示录制指南中加入最小复核清单链接。
- 明确本阶段不录威胁假路线、不改 Unity 场景、不接 RAG 或 MCP 到 Unity。

验收标准：
- 能用 60 到 90 秒视频展示真情报到暗道入口的连贯流程。
- 能说明每一步成功判定。
- 能在失败时定位是 UI、对话规则、路线提示还是入口表现问题。

验证方式：
- 文档已记录前置条件、录屏步骤、成功判定和失败处理。
- 本阶段只改文档，没有修改 Unity 或 Python 逻辑。

结论：
- 当前阶段已达到最小可行度。
- 下一步需要用户按清单实际录制或试跑一次真路线展示流程。

## 阶段验收：AI 守卫真路线录屏流程实际试跑

日期：2026-06-24

完成内容：
- 用户按 `docs/ai_guard_route_recording_checklist.md` 试跑真路线流程。
- 用户确认：可以从胆小守卫真实情报顺利走到下方暗道入口。
- 更新 `docs/ai_guard_route_recording_checklist.md`，记录实际试跑结论。

验收标准：
- 玩家能通过胆小守卫真实情报理解暗道入口方向。
- 从对话、路线提示到实际找到入口的展示流程连贯。
- 本阶段不继续扩写录屏脚本，不改 Unity 场景，不改 AI 逻辑。

验证方式：
- 用户实际试跑后确认“可以”。
- 文档已记录试跑结论。

结论：
- 当前阶段已完成，达到最小可行度。
- 真路线录屏流程暂不阻塞作品集展示。
- 下一步应进入新的收束阶段，不继续打磨该录屏链路。

## 阶段验收：作品集交付清单最小整理

日期：2026-06-24

完成内容：
- 新增 `docs/portfolio_delivery_checklist.md`。
- 整理当前可展示模块：Unity Level1、胆小守卫 AI NPC、真路线/假路线演示、RAG 问答、RAG 冲突检查器、Agent Workflow / MCP、AI 关卡设计助手。
- 补充推荐录屏顺序：主作品演示、AI 策划能力演示、Agent 技术扩展演示。
- 整理高优先级缺口：作品集入口说明、Git 提交前清理、外部 FastAPI 项目说明、Unity 项目路径说明、录屏文件命名。
- 明确不继续打磨三路线、真路线录屏链路或提前接 Unity MCP / LangGraph。

验收标准：
- 能一眼看出当前作品集可以展示什么。
- 能知道推荐录屏顺序。
- 能知道下一步最小收束任务是什么。

验证方式：
- 文档已列出可展示模块、录屏顺序、高优先级缺口和下一阶段建议。
- 本阶段只改文档，没有修改 Unity 或 Python 逻辑。

结论：
- 当前阶段已完成，达到最小可行度。
- 下一步应进入“作品集入口 README 最小整理”。

## 阶段验收：作品集入口 README 最小整理

日期：2026-06-24

完成内容：
- 新增根目录 `README.md`。
- 说明项目定位、同人作品边界、当前可展示模块和推荐录屏顺序。
- 记录当前总仓库、实际 Unity 项目、外部 FastAPI 项目和推荐 Python 虚拟环境路径。
- 链接关键文档：项目总览、进度、关卡设计、AI NPC、RAG、Agent Workflow、交付清单和接手文档。
- 明确当前边界：不保存秘密信息、不做护送逃离、不实现守卫削弱、不提前接 Unity MCP / LangGraph。

验收标准：
- 打开仓库后能快速理解项目是什么。
- 能知道当前能展示什么。
- 能知道推荐录屏顺序。
- 能知道哪些外部路径需要注意。

验证方式：
- `README.md` 已包含项目定位、展示模块、录屏顺序、重要路径、关键文档、当前边界和下一步。
- 本阶段只改文档，没有修改 Unity 或 Python 逻辑。

结论：
- 当前阶段已完成，达到最小可行度。
- 下一步应进入提交前清理最小检查。

## 阶段验收：提交前清理最小检查

日期：2026-06-24

完成内容：
- 新增 `docs/pre_commit_cleanup_check.md`。
- 检查 `.gitignore`、未跟踪文件、缓存目录和常见秘密信息字符串。
- 补充 `.gitignore`：忽略 `.env`、虚拟环境、`tmp/`、`output/`、Unity 生成目录、日志和常见缓存目录。
- 确认 `tmp/` 和 `output/` 包含本地生成图片、PDF 或简历预览素材，不建议进入第一次代码提交。
- 常见 secret 字符串扫描没有发现真实 API Key，命中项为变量名或占位示例。

验收标准：
- 能知道哪些文件存在提交风险。
- 能知道 `.gitignore` 是否覆盖当前主要缓存和本地输出。
- 不做正式提交，不删除文件。

验证方式：
- `git status --short` 和 `git ls-files --others --exclude-standard` 已检查。
- 缓存目录、输出目录和常见 secret 字符串已扫描。
- 本阶段只做 `.gitignore` 最小补全和文档记录。

结论：
- 当前阶段已完成，达到最小可行度。
- 下一步应进入第一次提交范围最小整理。

## 阶段验收：第一次提交范围最小整理

日期：2026-06-24

完成内容：
- 新增 `docs/first_commit_scope.md`。
- 将当前 90 个可提交未跟踪条目分为建议纳入、暂不纳入和已由 `.gitignore` 排除三类。
- 建议第一次提交纳入根目录入口与规则文件、`docs/`、`rag/`、`ai_npc/`、`agent_workflow/`、`level_designer/`、`stage5` 到 `stage8`。
- 建议暂不纳入 `tools/`，因为当前内容主要是简历 PDF 生成脚本，和《囚城营救》AI 游戏作品集主线关系较弱。
- 明确本阶段不执行 `git add`、`git commit` 或删除文件。

验收标准：
- 能知道第一次提交建议包含哪些文件。
- 能知道哪些文件暂不提交。
- 能知道正式提交前还需要用户确认什么。

验证方式：
- `git ls-files --others --exclude-standard` 已重新统计。
- 文档已记录提交范围建议。
- 本阶段没有执行 Git 暂存或提交。

结论：
- 当前阶段已完成，达到最小可行度。
- 下一步应进入第一次提交执行前确认。

## 下一里程碑

下一阶段建议：进入录屏素材命名与作品集交付文件夹最小整理。只确认演示视频应该如何命名、放在哪里、对应哪些展示模块。

## 更新模板

每次完成一个功能后追加：

```text
日期：
完成内容：
验证方式：
涉及文档：
后续任务：
```
## 阶段记录：GitHub remote 配置与推送尝试

日期：2026-06-24

完成内容：
- 用户提供 GitHub 仓库地址：`https://github.com/liwuyue113-dotcom/1.git`。
- 已将该地址配置为 Git remote：`origin`。
- 已尝试执行 `git push -u origin master`。

验证方式：
- `git remote -v` 显示 `origin https://github.com/liwuyue113-dotcom/1.git`。
- `git push -u origin master` 两次尝试均失败，报错为无法连接 `github.com:443`。
- `git status --short` 仍只显示 `?? tools/`，说明代码提交内容没有被破坏。

结论：
- remote 配置已完成。
- GitHub 推送尚未完成，当前阻塞原因是本机到 GitHub 的网络连接失败。
- 网络恢复后，继续执行 `git push -u origin master` 即可。

## 阶段验收：第一次本地 Git 提交执行

日期：2026-06-24

完成内容：
- 已按 `docs/first_commit_scope.md` 建议范围完成第一次本地提交。
- 提交号为 `f9ea39e`，提交信息为 `chore: initialize portfolio project workspace`。
- 提交范围包含根目录入口文档、`docs/`、`rag/`、`ai_npc/`、`agent_workflow/`、`level_designer/` 和 `stage5` 到 `stage8`。
- `tools/` 仍保持未跟踪状态，暂不纳入作品集主线提交。

验证方式：
- `git log --oneline` 可看到 `f9ea39e chore: initialize portfolio project workspace`。
- `git status --short` 仅显示 `?? tools/`。
- `rag/tests` 35 项通过。
- `ai_npc/tests` 4 项通过。
- `agent_workflow/tests` 16 项通过。
- `level_designer/tests` 18 项通过。

结论：
- 第一次本地提交阶段已完成，达到最小可行度。
- 下一阶段进入 GitHub 推送前最小检查。

## 阶段验收：GitHub 推送前最小检查

日期：2026-06-24

完成内容：
- 新增 `docs/github_push_precheck.md`。
- 确认当前分支为 `master`。
- 确认第一次本地提交为 `f9ea39e chore: initialize portfolio project workspace`。
- 确认当前尚未配置 GitHub remote。
- 确认当前未跟踪文件只剩 `tools/`，且本阶段不处理它。

验证方式：
- `git branch --show-current` 返回 `master`。
- `git remote -v` 无输出，说明尚未配置远程仓库。
- `git log --oneline` 可看到第一次本地提交 `f9ea39e chore: initialize portfolio project workspace`。
- `git status --short` 返回 `?? tools/`。

结论：
- GitHub 推送前检查已达到最小可行度。
- 当前不能直接推送，因为还缺 GitHub 仓库地址、公开/私有选择，以及是否保留 `master` 分支的决定。
- 下一步应由用户提供 GitHub 仓库地址，或先在 GitHub 创建空仓库。
