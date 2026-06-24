# RAG 标题参与 Embedding 设计

## 目标

让 Markdown 片段标题参与索引向量生成，提高玩家同义改写问题命中直接答案片段的概率。

## 当前问题

当前索引只对片段正文 `text` 生成 Embedding。`heading` 虽然被保存并展示，但不参与向量计算，因此“威胁胆小守卫的结果”等明确标题不会帮助检索。

## 方案

新增一个只负责构建索引文本的函数：

```python
def build_embedding_text(chunk: dict) -> str:
    heading = chunk.get("heading", "").strip()
    text = chunk["text"].strip()
    if not heading:
        return text
    return f"{heading}：{text}"
```

构建索引时，将每个片段的标题和正文组合后生成 Embedding：

```text
威胁胆小守卫的结果：玩家威胁胆小守卫会降低信任并提高恐惧……
```

片段元数据保持不变：

```json
{
  "heading": "威胁胆小守卫的结果",
  "text": "玩家威胁胆小守卫会降低信任并提高恐惧……",
  "source": "docs/rag_setting.md"
}
```

检索结果、答案 Prompt 和玩家看到的正文继续使用原始 `text`，不会显示拼接后的索引文本。

## 修改范围

- `rag/embedding_service.py`
  - 新增 `build_embedding_text()`。
- `rag/build_index.py`
  - 使用标题与正文组合后的文本生成索引向量。
- `rag/tests/test_embedding_service.py`
  - 验证有标题和无标题两种组合结果。

不修改：

- 玩家问题的 Embedding 方式。
- NumPy 余弦相似度检索。
- Top K 与最低相似度。
- 答案正文和来源结构。
- 已确认游戏设定。

## 验收标准

- 新增单元测试先失败，再通过。
- 全部自动化测试通过。
- BGE 索引重新构建后仍为 512 维。
- 五题检索重新验收，重点检查：
  - `恐吓那个逃岗士兵，他会怎么指路？`
  - `如何让躲起来的士兵愿意帮忙？`
- 如果五题仍未全部通过，如实记录实际排名，不继续堆叠关键词或临时修改检索算法。
