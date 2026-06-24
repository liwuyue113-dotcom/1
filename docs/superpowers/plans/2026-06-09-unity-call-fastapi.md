# Unity Call FastAPI Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Let Unity send one Chinese player message to the local FastAPI `/npc/chat` endpoint and print the guard reply and intel result in the Console.

**Architecture:** Add one focused `AIGuardApiClient` MonoBehaviour. It builds and parses the agreed JSON format, while a coroutine performs the non-blocking HTTP POST with a timeout. A Context Menu test entry sends a fixed Chinese message without requiring the phase 6 dialogue UI.

**Tech Stack:** Unity 2022.3.62f3, C#, `UnityWebRequest`, `JsonUtility`, Unity EditMode tests

---

### Task 1: Define and test the JSON boundary

**Files:**
- Create: `D:/UnityProjects/project03/Assets/Editor/Tests/AIGuardApiClientTests.cs`
- Create: `D:/UnityProjects/project03/Assets/scripts/AI/AIGuardApiClient.cs`

- [ ] **Step 1: Write the failing EditMode tests**

Test that `BuildRequestJson("我不会伤害你")` preserves the Chinese player message and that `ParseResponse` reads `reply`, `emotion`, and `intel_result`.

- [ ] **Step 2: Run the focused EditMode test and verify it fails**

Run Unity EditMode tests filtered to `AIGuardApiClientTests`.

Expected: FAIL because `AIGuardApiClient` does not exist.

- [ ] **Step 3: Implement the minimal JSON boundary**

Add serializable request and response data classes plus `BuildRequestJson` and `ParseResponse`.

- [ ] **Step 4: Run the focused EditMode test and verify it passes**

Expected: both JSON boundary tests pass.

### Task 2: Add the non-blocking HTTP call

**Files:**
- Modify: `D:/UnityProjects/project03/Assets/scripts/AI/AIGuardApiClient.cs`

- [ ] **Step 1: Add a Context Menu entry**

Add `Send Test Message` so the developer can trigger one request from the Inspector without building phase 6 UI.

- [ ] **Step 2: POST JSON with a timeout**

Use `UnityWebRequest`, set `Content-Type: application/json`, and yield the request so Unity remains responsive.

- [ ] **Step 3: Log success and failure**

On success, print the guard reply, emotion, and intel result. On failure, print a clear error without changing game state.

- [ ] **Step 4: Compile and run all EditMode tests**

Expected: zero compile errors and all existing EditMode tests pass.

### Task 3: Perform the live phase check

**Files:**
- No source changes required

- [ ] **Step 1: Start FastAPI**

Run from `D:/develop/pythons`:

```powershell
.\.venv\Scripts\python.exe -m uvicorn api:app --host 127.0.0.1 --port 8000
```

- [ ] **Step 2: Add the component in a test scene**

Attach `AIGuardApiClient` to an empty GameObject and invoke `Send Test Message`.

- [ ] **Step 3: Verify the Console**

Expected: Chinese guard reply, emotion, and `intel_result` are printed. Stopping FastAPI and retrying prints an error while Unity remains responsive.
