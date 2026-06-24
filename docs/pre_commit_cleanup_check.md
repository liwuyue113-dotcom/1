# 提交前清理最小检查

## 文档用途

本文记录 2026-06-24 的提交前最小检查结果。目标是确认第一次正式提交前需要注意哪些文件、缓存和秘密信息风险。

本阶段只做检查和 `.gitignore` 最小补全，不做正式 Git 提交，不删除文件。

## 检查范围

- `.gitignore`
- `git status --short`
- `git ls-files --others --exclude-standard`
- 常见缓存目录
- 常见秘密信息字符串

## 检查结果

### `.gitignore`

原本只忽略：

```text
__pycache__/
*.pyc
rag/rag_data/
```

本阶段补充了：

- `.env` 和 `.env.*`
- `.venv/`、`venv/`
- `tmp/`
- `output/`
- Unity 生成目录：`Library/`、`Temp/`、`Logs/`、`Obj/`、`UserSettings/`
- 常见缓存：`.pytest_cache/`、`.mypy_cache/`、`.ruff_cache/`
- `*.log`

### 未跟踪文件

补充 `.gitignore` 前，`git ls-files --others --exclude-standard` 统计为 97 个未跟踪条目。

主要分类：

| 分类 | 数量 |
| --- | --- |
| `docs` | 29 |
| `rag` | 21 |
| `agent_workflow` | 9 |
| `level_designer` | 8 |
| `tmp` | 6 |
| `output` | 3 |
| `stage5` / `stage6` / `stage7` / `stage8` | 10 |
| 根目录文档与规则文件 | 5 |

`tmp/` 和 `output/` 包含本地生成的图片、PDF 或简历预览素材，不建议进入第一次代码提交。

补充 `.gitignore` 后，`git ls-files --others --exclude-standard` 统计为 89 个未跟踪条目，`tmp/`、`output/`、`__pycache__`、`*.pyc` 和 `rag/rag_data` 不再出现在可提交的未跟踪列表中。

当前仍需整理的主要未跟踪分类：

| 分类 | 数量 |
| --- | --- |
| `docs` | 30 |
| `rag` | 21 |
| `agent_workflow` | 9 |
| `level_designer` | 8 |
| `stage5` / `stage6` / `stage7` / `stage8` | 10 |
| 其他源码、工具和根目录文档 | 11 |

### 缓存目录

检查发现多个 `__pycache__` 目录和 `rag/rag_data`。这些已经被 `.gitignore` 忽略，不应提交。

### 秘密信息

常见 secret 字符串扫描没有发现真实 API Key。命中的内容是代码参数名或文档占位示例，例如：

- `api_key`
- `DEEPSEEK_API_KEY="你的 API Key"`

当前仍需注意：不要提交真实 `.env` 文件、截图中的 Key、终端环境变量或包含个人敏感信息的输出文件。

补充 `.gitignore` 后再次扫描，未发现真实 API Key 命中。

## 当前结论

- `.gitignore` 已补到当前阶段最低可用。
- 本阶段没有删除文件，没有提交 Git。
- 仍然有大量未跟踪源码和文档，需要下一阶段决定第一次提交范围。
- `tmp/` 和 `output/` 已被标记为本地生成输出，不应进入默认提交范围。

## 下一阶段建议

进入“第一次提交范围最小整理”。

最低可用目标：

```text
只决定哪些文件应该进入第一次提交，哪些文件继续保持忽略或暂不提交。
```
