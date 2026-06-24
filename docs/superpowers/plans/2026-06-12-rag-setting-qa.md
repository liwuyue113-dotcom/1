# RAG Setting Q&A Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a local command-line RAG prototype that answers questions about selected 《囚城营救》 setting documents and cites source files.

**Architecture:** Split selected Markdown files into source-aware chunks, encode them with a local Chinese embedding model, and store vectors in NumPy files. At query time, retrieve the top three chunks by cosine similarity and ask DeepSeek to answer only from those chunks, with a deterministic fallback when evidence or API access is unavailable.

**Tech Stack:** Python 3, unittest, NumPy, sentence-transformers with local fallback, DeepSeek API

---

### Task 1: Create the RAG project skeleton and chunking tests

**Files:**
- Create: `rag/requirements.txt`
- Create: `rag/rag_config.py`
- Create: `rag/document_loader.py`
- Create: `rag/tests/test_document_loader.py`

- [ ] **Step 1: Add dependencies**

Create `rag/requirements.txt`:

```text
numpy
requests
sentence-transformers
```

- [ ] **Step 2: Write failing chunking tests**

Test that Markdown headings are preserved as metadata, source paths are included, and empty or very short paragraphs are ignored.

- [ ] **Step 3: Run the focused test and verify it fails**

Run:

```powershell
python -m unittest rag.tests.test_document_loader -v
```

Expected: FAIL because `document_loader.py` has not implemented the required functions.

- [ ] **Step 4: Implement selected source configuration and Markdown chunking**

`rag_config.py` defines only:

```python
SOURCE_FILES = [
    "docs/game_design.md",
    "docs/project-knowledge.md",
]
```

`document_loader.py` returns chunks containing `text`, `source`, and `heading`.

- [ ] **Step 5: Run the focused test and verify it passes**

Expected: all document loader tests pass.

### Task 2: Build and test local vector retrieval

**Files:**
- Create: `rag/vector_store.py`
- Create: `rag/tests/test_vector_store.py`
- Create: `rag/build_index.py`

- [ ] **Step 1: Write failing cosine retrieval tests**

Use small fixed vectors to verify:

- top results are ordered by cosine similarity;
- the requested result count is respected;
- source metadata is preserved.

- [ ] **Step 2: Run the focused test and verify it fails**

Run:

```powershell
python -m unittest rag.tests.test_vector_store -v
```

Expected: FAIL because retrieval functions do not exist.

- [ ] **Step 3: Implement vector storage and cosine retrieval**

Store:

```text
rag/rag_data/chunks.json
rag/rag_data/embeddings.npy
```

Use `sentence-transformers` only in `build_index.py` and query orchestration. Keep cosine similarity as a small NumPy function that is independently testable.

- [ ] **Step 4: Run vector store tests**

Expected: all vector store tests pass.

- [ ] **Step 5: Build the real setting index**

Run:

```powershell
python rag/build_index.py
```

Expected: index files are created and the script prints the number of indexed chunks.

### Task 3: Add grounded answer generation

**Files:**
- Create: `rag/answer_service.py`
- Create: `rag/tests/test_answer_service.py`

- [ ] **Step 1: Write failing evidence boundary tests**

Verify:

- insufficient evidence returns `当前知识库没有足够信息`;
- source paths are deduplicated;
- the answer prompt explicitly forbids adding unsupported facts.

- [ ] **Step 2: Run the focused test and verify it fails**

Run:

```powershell
python -m unittest rag.tests.test_answer_service -v
```

Expected: FAIL because answer service functions do not exist.

- [ ] **Step 3: Implement minimal grounded answer service**

The service builds a prompt from retrieved chunks, calls DeepSeek using `DEEPSEEK_API_KEY`, and falls back to showing retrieved text and sources when the API call fails.

- [ ] **Step 4: Run answer service tests**

Expected: all answer service tests pass.

### Task 4: Add the command-line Q&A workflow

**Files:**
- Create: `rag/ask.py`
- Create: `rag/README.md`

- [ ] **Step 1: Implement the command-line loop**

Behavior:

```text
输入问题
-> retrieve top 3 chunks
-> reject if evidence is insufficient
-> generate grounded answer
-> print answer and sources
-> 输入“退出”结束
```

- [ ] **Step 2: Document setup and commands**

Document environment setup, index building, Q&A startup, and the three acceptance questions.

- [ ] **Step 3: Run all automated tests**

Run:

```powershell
python -m unittest discover -s rag/tests -v
```

Expected: all tests pass.

- [ ] **Step 4: Perform live acceptance**

Ask:

```text
胆小守卫提供的真实路线在哪里？
威胁胆小守卫可能得到什么情报？
玩家为什么要营救人质？
```

Expected: the first two answers cite correct setting documents; the third refuses to invent an answer.
