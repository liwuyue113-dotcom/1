# AI 关卡设计助手

## 文档用途

本文档记录《囚城营救》AI 关卡设计助手的目标、当前最低可用功能和后续扩展方向。

## 当前阶段

当前阶段为 AI 关卡设计助手 JSON 输出版 MVP。

第一版已完成本地命令行模板，第二版已完成 DeepSeek 调用能力，第三版已完成 RAG 检索能力，第四版已完成最低质量评价规则。当前版本新增 JSON 输出，方便未来网页或 Unity 工具读取。工具不接 Unity，不保存 API Key。

## MVP 输入

命令行输入包含：

- 关卡主题
- 玩家目标
- 难度
- 三条路线资料

示例：

```powershell
D:\develop\pythons\.venv\Scripts\python.exe -m level_designer.cli --theme "离国边境城堡潜入" --goal "在黎明前找到吕归尘" --difficulty "普通" --routes "上路较长，敌人数量一般；中路长度一般，敌人略多；下方暗道长度正常，敌人最少。"
```

使用 DeepSeek：

```powershell
$env:DEEPSEEK_API_KEY="你的 DeepSeek API Key"
D:\develop\pythons\.venv\Scripts\python.exe -m level_designer.cli --provider deepseek --theme "离国边境城堡潜入" --goal "在黎明前找到吕归尘" --difficulty "普通" --routes "上路较长，敌人数量一般；中路长度一般，敌人略多；下方暗道长度正常，敌人最少。"
```

如果未设置 `DEEPSEEK_API_KEY`，工具会提示 DeepSeek 未启用，并回退到本地模板。

使用 RAG：

```powershell
D:\develop\pythons\.venv\Scripts\python.exe -m level_designer.cli --use-rag --theme "离国边境城堡潜入" --goal "在黎明前找到吕归尘" --difficulty "普通" --routes "上路较长，敌人数量一般；中路长度一般，敌人略多；下方暗道长度正常，敌人最少。"
```

RAG 会检索 `docs/rag_setting.md` 的已确认设定，并在输出中加入 `RAG 设定依据`。如果 RAG 索引不存在或读取失败，工具会保留命令行路线资料并提示原因。

使用质量评价：

```powershell
D:\develop\pythons\.venv\Scripts\python.exe -m level_designer.cli --evaluate --theme "离国边境城堡潜入" --goal "在黎明前找到吕归尘" --difficulty "普通" --routes "上路较长，敌人数量一般；中路长度一般，敌人略多；下方暗道长度正常，敌人最少。"
```

质量评价会追加 `质量评价` 区块，检查：

- 玩家目标是否清楚
- 是否包含上路、中路和下方暗道三条路线
- 是否包含风险与奖励
- 是否包含失败条件

使用 JSON 输出：

```powershell
D:\develop\pythons\.venv\Scripts\python.exe -m level_designer.cli --format json --evaluate --theme "离国边境城堡潜入" --goal "在黎明前找到吕归尘" --difficulty "普通" --routes "上路较长，敌人数量一般；中路长度一般，敌人略多；下方暗道长度正常，敌人最少。"
```

JSON 输出字段包括：

- `provider`：实际使用的生成方式
- `input`：输入参数
- `plan_markdown`：完整 Markdown 策划案
- `evaluation`：质量评价结果；未启用 `--evaluate` 时为 `null`
- `warnings`：DeepSeek 回退或其他提示信息

## MVP 输出

工具输出固定 Markdown 策划案，包含：

- 玩家目标
- 三条路线设计
- 敌人配置
- 风险与奖励
- 失败条件
- 设计意图
- 优化建议

## 当前已内置的三路线规则

- 上路：正常路线，路线较长，敌人数量一般；前段分散，后段有连续守卫站岗。
- 中路：正常路线，长度一般，敌人略多；部分位置有多个守卫站岗。
- 下方暗道：隐藏路线，长度正常，敌人最少；需要胆小守卫真实情报才能明确入口方向。

## 后续扩展

当前 JSON 输出版 MVP 达标后不继续扩写关卡助手。下一阶段建议暂停关卡助手阶段，转向 Unity 关卡实装检查。
