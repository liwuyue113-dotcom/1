# 《囚城营救》核心剧情设定实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将已确认的《九州缥缈录》原创同人支线核心剧情写入策划文档和 RAG 专用设定，并完成剧情问答验收。

**Architecture:** 策划文档保存完整剧情与同人定位，RAG 文档保存单义已确认事实。保持现有 BGE、检索和回答流程不变，新增内容边界测试后重建索引并验收五个剧情问题。

**Tech Stack:** Markdown、Python 3.13、unittest、sentence-transformers、`BAAI/bge-small-zh-v1.5`、NumPy

---

### Task 1: 用测试锁定剧情事实

**Files:**
- Modify: `rag/tests/test_rag_acceptance.py`

- [ ] 新增测试，验证 RAG 设定包含主角、营救目标、敌方势力、限时原因、通关和失败条件。
- [ ] 运行聚焦测试并确认因剧情尚未写入而失败。

### Task 2: 同步核心剧情文档

**Files:**
- Modify: `docs/game_design.md`
- Modify: `docs/rag_setting.md`
- Modify: `docs/project_context.md`

- [ ] 明确项目为基于原著人物与世界观的原创同人支线。
- [ ] 写入已确认核心剧情与关卡条件。
- [ ] 将 RAG 剧情事实拆成单义片段。
- [ ] 运行全部自动化测试。

### Task 3: 重建索引并验收剧情问答

**Files:**
- Generated: `rag/rag_data/chunks.json`
- Generated: `rag/rag_data/embeddings.npy`

- [ ] 使用项目 `.venv` 重建 BGE 索引。
- [ ] 验收五个剧情问题的 Top 3 结果。
- [ ] 确认未包含护送逃离玩法。

### Task 4: 更新阶段记录

**Files:**
- Modify: `docs/rag.md`
- Modify: `docs/progress.md`
- Modify: `HANDOVER.md`

- [ ] 记录剧情设定、RAG 验收结果与同人边界。
- [ ] 运行全部自动化测试与 `git diff --check`。
