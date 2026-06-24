# 《囚城营救》RAG 设定问答原型

第一版 RAG 从精选游戏设定文档中检索相关内容，回答问题并显示来源。

构建索引时，系统会组合片段标题与正文生成 Embedding；检索结果和回答仍显示原始正文与来源。

## 当前索引范围

- `docs/rag_setting.md`

完整策划案、开发进度、技术决策和交接文档不会直接进入设定问答索引。适合问答的已确认事实应先整理到专用设定文档。

## 安装依赖

在仓库根目录执行：

```powershell
python -m pip install -r rag/requirements.txt
```

首次加载本地 Embedding 模型时需要下载模型文件。

如果没有安装 `sentence-transformers`，程序会自动使用无需下载的本地文本向量兜底。兜底可以验证完整流程，但语义检索质量低于正式中文 Embedding 模型。

## 构建索引

修改设定文档后，需要重新构建索引：

```powershell
python -m rag.build_index
```

成功后会生成：

```text
rag/rag_data/chunks.json
rag/rag_data/embeddings.npy
```

## 开始问答

如需 DeepSeek 生成答案，先配置环境变量：

```powershell
$env:DEEPSEEK_API_KEY="你的 API Key"
```

启动：

```powershell
python -m rag.ask
```

没有配置 API Key 时，程序仍会显示最相关的设定原文和来源。

不要在截图、代码、文档或 Git 中公开 API Key。若 Key 意外出现在截图或聊天记录中，应立即在服务商控制台撤销并生成新 Key。

## 检查新增设定是否冲突

第一版冲突检查器会检索最相关的已确认设定，并用简单规则判断明显冲突。

示例：

```powershell
python -m rag.check_conflict "新增设定：下方暗道内部有多个守卫来回巡逻。"
```

预期会输出：

- 结论：可能冲突。
- 冲突原因：守卫数量与已确认设定不一致。
- 来源：`docs/rag_setting.md`。
- 相关设定片段。

当前版本不调用大模型，不自动修改设定，只作为策划检查提醒。

作品集讲解稿见：

```text
docs/rag_conflict_checker_demo.md
```

## 运行自动测试

```powershell
python -m unittest discover -s rag/tests -v
```

## 验收问题

```text
姬野为什么要潜入城堡？
吕归尘被谁关押在哪里？
为什么营救任务有时间限制？
怎样才算完成关卡？
找到吕归尘后是否需要护送他逃离？
```

预期：

- 前四个问题检索到对应的已确认核心剧情事实。
- 第五个问题明确回答当前版本不包含护送吕归尘逃离城堡的玩法。

## 添加新设定文档

1. 在 `docs/` 中创建专门的角色、阵营、地图、任务或剧情设定文档。
2. 将相对路径添加到 `rag/rag_config.py` 的 `SOURCE_FILES`。
3. 重新运行 `python -m rag.build_index`。
