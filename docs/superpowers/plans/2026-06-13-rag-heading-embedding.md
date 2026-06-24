# RAG 标题参与 Embedding 实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 构建索引时将片段标题与正文组合生成 Embedding，同时保持检索返回与展示结构不变。

**Architecture:** 在 `embedding_service.py` 中新增纯函数构建索引文本，`build_index.py` 调用该函数后生成向量。查询、检索和回答流程保持不变，并使用五题 BGE Top 3 结果验证效果。

**Tech Stack:** Python 3.13、unittest、sentence-transformers、`BAAI/bge-small-zh-v1.5`、NumPy

---

### Task 1: 测试并实现索引文本组合

**Files:**
- Modify: `rag/tests/test_embedding_service.py`
- Modify: `rag/embedding_service.py`

- [ ] 新增测试，验证有标题时返回 `标题：正文`，无标题时只返回正文。
- [ ] 运行聚焦测试并确认因函数不存在而失败。
- [ ] 实现 `build_embedding_text(chunk)`。
- [ ] 运行聚焦测试并确认通过。

### Task 2: 构建索引时使用标题与正文

**Files:**
- Modify: `rag/build_index.py`

- [ ] 导入 `build_embedding_text`。
- [ ] 将索引输入从 `chunk["text"]` 改为 `build_embedding_text(chunk)`。
- [ ] 运行全部自动化测试。
- [ ] 使用项目 `.venv` 和离线缓存重建 BGE 索引。
- [ ] 确认索引向量维度为 512。

### Task 3: 五题验收与文档更新

**Files:**
- Modify: `docs/rag.md`
- Modify: `docs/progress.md`
- Modify: `docs/tech_decision.md`
- Modify: `HANDOVER.md`

- [ ] 输出五题 Top 3 检索结果。
- [ ] 记录通过和未通过结果，不夸大效果。
- [ ] 更新阶段状态和下一步。
- [ ] 运行全部自动化测试与 `git diff --check`。
