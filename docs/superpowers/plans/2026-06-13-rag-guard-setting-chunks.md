# 胆小守卫 RAG 设定片段优化实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将已确认的胆小守卫设定拆成按玩家问题组织的单义片段，使五个同义改写问题能够稳定检索到直接答案或未确认设定。

**Architecture:** 保持现有 Markdown 加载器、BGE Embedding 和 NumPy 检索流程不变，只优化 `docs/rag_setting.md` 的标题与段落边界。先新增针对真实设定文档的验收测试并确认失败，再重写设定、重建索引、运行自动化测试和 BGE Top 3 人工验收。

**Tech Stack:** Markdown、Python 3.13、unittest、sentence-transformers、`BAAI/bge-small-zh-v1.5`、NumPy

---

## 文件结构

- Modify: `docs/rag_setting.md`
  - 将已确认事实拆为按玩家问题组织的单义设定片段。
- Modify: `rag/tests/test_rag_acceptance.py`
  - 增加不依赖在线模型的内容边界测试，确保设定文档包含直接回答片段且未新增未确认剧情。
- Modify: `docs/rag.md`
  - 记录本阶段的五题检索验收结果和剩余限制。
- Modify: `docs/progress.md`
  - 更新当前阶段、验收状态和下一步。
- Modify: `HANDOVER.md`
  - 更新下一位 AI 的接手任务。
- Generated and ignored: `rag/rag_data/chunks.json`
- Generated and ignored: `rag/rag_data/embeddings.npy`

### Task 1: 用验收测试锁定单义设定边界

**Files:**
- Modify: `rag/tests/test_rag_acceptance.py`
- Read: `docs/rag_setting.md`

- [ ] **Step 1: 在验收测试中增加设定片段结构测试**

在 `RagAcceptanceTests` 中增加以下测试。测试通过标题和正文验证计划中的直接答案片段，不依赖 BGE 下载或在线服务：

```python
    def test_guard_setting_contains_single_purpose_answer_chunks(self):
        chunks_by_heading = {
            chunk["heading"]: chunk["text"]
            for chunk in self.chunks
            if chunk["source"] == "docs/rag_setting.md"
        }

        expected_facts = {
            "安抚胆小守卫的结果": ["安抚", "提高信任", "降低恐惧"],
            "威胁胆小守卫的结果": ["威胁", "降低信任", "提高恐惧"],
            "获得真实路线的条件": ["信任大于等于 50", "提供真实路线"],
            "获得虚假路线的条件": ["恐惧大于等于信任加 30", "提供虚假路线"],
            "真实安全路线": ["第二个口子", "暗道", "几乎无人镇守"],
            "虚假危险路线": ["往上走最安全", "虚假"],
        }

        for heading, facts in expected_facts.items():
            self.assertIn(heading, chunks_by_heading)
            for fact in facts:
                self.assertIn(fact, chunks_by_heading[heading])
```

- [ ] **Step 2: 增加未确认剧情边界测试**

在同一测试类中增加：

```python
    def test_guard_setting_keeps_unconfirmed_story_unknown(self):
        chunks_by_heading = {
            chunk["heading"]: chunk["text"]
            for chunk in self.chunks
            if chunk["source"] == "docs/rag_setting.md"
        }

        self.assertEqual(
            chunks_by_heading["未确认设定"],
            "姬野为什么要营救人质，目前尚未确认。",
        )
```

- [ ] **Step 3: 运行测试并确认正确失败**

Run:

```powershell
D:\develop\pythons\.venv\Scripts\python.exe -m unittest rag.tests.test_rag_acceptance -v
```

Expected:

- 新增的 `test_guard_setting_contains_single_purpose_answer_chunks` 失败。
- 失败原因是当前 `docs/rag_setting.md` 尚未包含计划中的单义标题，而不是导入或语法错误。
- `test_guard_setting_keeps_unconfirmed_story_unknown` 通过。

- [ ] **Step 4: 提交验收测试**

```powershell
git add rag/tests/test_rag_acceptance.py
git commit -m "test: define guard setting chunk boundaries"
```

### Task 2: 将胆小守卫设定改写为单义片段

**Files:**
- Modify: `docs/rag_setting.md`
- Test: `rag/tests/test_rag_acceptance.py`

- [ ] **Step 1: 使用已确认事实重写设定文档**

将 `docs/rag_setting.md` 改为以下内容：

```markdown
# 《囚城营救》RAG 已确认设定

## 游戏目标

玩家扮演姬野，需要在倒计时结束前穿过城堡、应对守卫并完成人质营救。

## 胆小守卫的身份与位置

胆小守卫听见外面的砍杀声后擅自离开岗位，躲在 Level1 深处。他认为玩家可能是杀人魔，因此非常害怕玩家。

## 安抚胆小守卫的结果

玩家安抚胆小守卫会提高信任并降低恐惧。持续安抚可以让胆小守卫更愿意帮助玩家。

## 威胁胆小守卫的结果

玩家威胁胆小守卫会降低信任并提高恐惧。胆小守卫可能为了自保提供虚假路线。

## 获得真实路线的条件

当胆小守卫的信任大于等于 50，并且信任大于等于恐惧时，胆小守卫会提供真实路线。

## 获得虚假路线的条件

当胆小守卫的恐惧大于等于信任加 30 时，胆小守卫会提供虚假路线。其他情况会拒绝透露路线。

## 真实安全路线

胆小守卫提供的真实安全路线是：往前第二个口子跳下去有一条暗道，几乎无人镇守。这条路线可以帮助玩家绕过守卫巡逻。

## 虚假危险路线

胆小守卫提供的虚假危险路线是：他谎称往上走最安全。玩家威胁胆小守卫后可能得到这条虚假路线。

## AI 与规则系统职责

DeepSeek 负责理解玩家意图并生成符合胆小守卫性格的台词。Python 规则系统负责信任、恐惧和真假路线。Unity 负责显示对话、情绪、倒计时奖励和路线提示。

AI 不能直接修改真实路线，也不能直接操作 Unity 游戏对象。

## 未确认设定

姬野为什么要营救人质，目前尚未确认。
```

- [ ] **Step 2: 运行聚焦验收测试并确认通过**

Run:

```powershell
D:\develop\pythons\.venv\Scripts\python.exe -m unittest rag.tests.test_rag_acceptance -v
```

Expected: `RagAcceptanceTests` 全部通过。

- [ ] **Step 3: 运行全部自动化测试**

Run:

```powershell
D:\develop\pythons\.venv\Scripts\python.exe -m unittest discover -s rag/tests -v
```

Expected: 原有 14 项测试加新增 2 项测试，共 16 项全部通过。

- [ ] **Step 4: 提交设定片段优化**

```powershell
git add docs/rag_setting.md
git commit -m "docs: split guard setting into answer chunks"
```

### Task 3: 重建 BGE 索引并完成五题检索验收

**Files:**
- Generated: `rag/rag_data/chunks.json`
- Generated: `rag/rag_data/embeddings.npy`
- Read: `docs/superpowers/specs/2026-06-13-rag-guard-setting-chunks-design.md`

- [ ] **Step 1: 使用项目虚拟环境和离线缓存重建索引**

Run:

```powershell
$env:HF_HUB_OFFLINE="1"
D:\develop\pythons\.venv\Scripts\python.exe -m rag.build_index
```

Expected:

```text
索引构建完成，共写入 30 个设定片段。
```

片段总数可能因 Markdown 加载器的段落边界产生小幅差异，但索引向量维度必须为 512。

- [ ] **Step 2: 确认索引使用 BGE 向量维度**

Run:

```powershell
D:\develop\pythons\.venv\Scripts\python.exe -c "from rag.rag_config import CHUNKS_PATH, EMBEDDINGS_PATH; from rag.vector_store import load_index; chunks, embeddings = load_index(CHUNKS_PATH, EMBEDDINGS_PATH); print(len(chunks), embeddings.shape)"
```

Expected: 输出的向量形状第二维为 `512`。

- [ ] **Step 3: 输出五题 Top 3 检索结果**

使用项目虚拟环境运行一个临时验收脚本，问题固定为：

```python
questions = [
    "有什么近路能绕过看守？",
    "恐吓那个逃岗士兵，他会怎么指路？",
    "如何让躲起来的士兵愿意帮忙？",
    "不想碰上巡逻兵，该从哪里走？",
    "主角为什么要营救人质？",
]
```

脚本对每个问题打印 Top 3 的 `score`、`heading` 和 `text`。不要将临时脚本保存进仓库。

- [ ] **Step 4: 按规格逐项判断验收结果**

Expected:

- “有什么近路能绕过看守？”：`真实安全路线` 为 Top 1。
- “恐吓那个逃岗士兵，他会怎么指路？”：`威胁胆小守卫的结果` 或 `虚假危险路线` 进入 Top 3。
- “如何让躲起来的士兵愿意帮忙？”：`安抚胆小守卫的结果` 或 `获得真实路线的条件` 进入 Top 3。
- “不想碰上巡逻兵，该从哪里走？”：`真实安全路线` 进入 Top 3。
- “主角为什么要营救人质？”：`未确认设定` 进入 Top 3，并由 `answer_question()` 返回 `当前知识库没有足够信息。`

如果某一项未通过，记录实际排名并停止本阶段验收。不要修改加载器、相似度阈值或检索算法；先向用户说明高质量设定文本仍不足以解决的问题。

### Task 4: 更新阶段文档并完成最终验证

**Files:**
- Modify: `docs/rag.md`
- Modify: `docs/progress.md`
- Modify: `HANDOVER.md`
- Test: `rag/tests/`

- [ ] **Step 1: 更新 RAG 说明**

在 `docs/rag.md` 记录：

- 胆小守卫设定已按玩家问题拆成单义片段。
- 五题 Top 3 的实际验收结果。
- 未通过问题的实际排名与原因，不夸大效果。

- [ ] **Step 2: 更新项目进度**

在 `docs/progress.md` 中：

- 将“优化设定内容与切片质量”标记为完成或保留为开发中，取决于五题验收结果。
- 新增日期为 `2026-06-13` 的阶段验收记录。
- 将下一步更新为真实 DeepSeek 回答验收或继续优化设定数据。

- [ ] **Step 3: 更新交接文档**

在 `HANDOVER.md` 中记录：

- 新的设定片段结构。
- 五题验收结果。
- 下一位 AI 应执行的具体任务。

- [ ] **Step 4: 运行最终验证**

Run:

```powershell
D:\develop\pythons\.venv\Scripts\python.exe -m unittest discover -s rag/tests -v
git diff --check
```

Expected:

- 16 项自动化测试全部通过。
- `git diff --check` 无输出。

- [ ] **Step 5: 提交文档与阶段结果**

```powershell
git add docs/rag.md docs/progress.md HANDOVER.md
git commit -m "docs: record guard setting retrieval results"
```
