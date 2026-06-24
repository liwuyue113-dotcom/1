# RAG 专用设定索引范围实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 RAG 默认索引范围限制为专用已确认设定文档，减少完整策划案中的通用内容干扰。

**Architecture:** 使用现有 `SOURCE_FILES` 白名单控制索引范围，不修改加载器、Embedding 或检索算法。通过配置测试锁定默认范围，重建 BGE 索引后运行五题 Top 3 验收。

**Tech Stack:** Python 3.13、unittest、sentence-transformers、`BAAI/bge-small-zh-v1.5`、NumPy

---

### Task 1: 用测试锁定专用设定索引范围

**Files:**
- Modify: `rag/tests/test_rag_acceptance.py`
- Modify: `rag/rag_config.py`

- [ ] 新增测试，断言 `SOURCE_FILES == ["docs/rag_setting.md"]`。
- [ ] 运行聚焦测试并确认因当前仍包含 `docs/game_design.md` 而失败。
- [ ] 将默认索引范围改为只包含 `docs/rag_setting.md`。
- [ ] 运行全部自动化测试并确认通过。

### Task 2: 重建索引并完成五题验收

**Files:**
- Generated: `rag/rag_data/chunks.json`
- Generated: `rag/rag_data/embeddings.npy`

- [ ] 使用项目 `.venv` 和离线缓存重建 BGE 索引。
- [ ] 确认所有片段来源均为 `docs/rag_setting.md`，向量维度为 512。
- [ ] 输出五题 Top 3 检索结果。
- [ ] 验证五题全部达到设计标准。

### Task 3: 更新文档与最终验证

**Files:**
- Modify: `docs/rag.md`
- Modify: `docs/progress.md`
- Modify: `docs/tech_decision.md`
- Modify: `HANDOVER.md`
- Modify: `rag/README.md`

- [ ] 记录专用设定白名单决策与实际验收结果。
- [ ] 更新当前阶段和下一步。
- [ ] 运行全部自动化测试与 `git diff --check`。
