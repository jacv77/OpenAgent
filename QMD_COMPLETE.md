# QMD Memory Backend Setup - COMPLETE ✅

## All Steps Completed Successfully!

### Step 1: Install QMD CLI ✓
- **Bun Runtime**: 1.3.10
- **QMD CLI**: 1.1.0
- **Wrapper**: `/usr/local/bin/qmd`

### Step 2: Install SQLite with Extension Support ✓
- **SQLite Version**: 3.51.2 (via Linuxbrew)
- **Extension Loading**: Enabled
- **Location**: `/home/linuxbrew/.linuxbrew/bin/sqlite3`

### Step 3: Configure memory.backend = "qmd" ✓
Updated `openclaw.json` with:
```json
{
  "memory": {
    "backend": "qmd",
    "citations": "auto",
    "qmd": {
      "includeDefaultMemory": true,
      "update": {
        "interval": "5m",
        "debounceMs": 15000,
        "waitForBootSync": false
      },
      "limits": {
        "maxResults": 6,
        "timeoutMs": 4000
      },
      "scope": {
        "default": "allow",
        "rules": [
          {
            "action": "allow",
            "match": {
              "chatType": "direct"
            }
          }
        ]
      }
    }
  }
}
```

### Step 4: Add Workspace Memory Files as QMD Collection ✓
Created two collections:

**memory-root**
- Path: `~/.openclaw/workspace/memory`
- Pattern: `**/*.md`
- Files: 2 (daily logs)

**workspace-docs**
- Path: `~/.openclaw/workspace`
- Pattern: `*.md`
- Files: 17 (documentation, setup guides, etc.)

### Step 5: Run Initial Embed ✓
- **Embedding Model Downloaded**: embeddinggemma-300M-Q8_0.gguf (314MB)
- **Vectors Generated**: 35 embeddings
- **Index Size**: 3.3 MB
- **Status**: All documents embedded successfully

### Step 6: Test with a Query ✓

**BM25 Keyword Search Test:**
```bash
qmd search "AgentMail" --json
```
Result: ✓ Found 7 relevant documents with scores 0.49-0.52

**Vector Similarity Search Test:**
```bash
qmd vsearch "how to send emails" -n 3
```
Result: ✓ Found 3 relevant documents with scores 62-64%
- Downloaded query expansion model (1.28GB)
- Semantic search working correctly

---

## QMD Status Summary

```
Index: /home/rocco/.cache/qmd/index.sqlite
Size:  3.3 MB

Documents
  Total:    19 files indexed
  Vectors:  35 embedded
  Updated:  Recently

Collections
  memory-root (qmd://memory-root/)
    Pattern:  **/*.md
    Files:    2
  workspace-docs (qmd://workspace-docs/)
    Pattern:  **/*.md
    Files:    17

Device
  GPU:      none (running on CPU)
  CPU:      1 math cores
```

---

## Models Downloaded

1. **Embedding Model** (314MB)
   - `hf_ggml-org_embeddinggemma-300M-Q8_0.gguf`
   - Used for: Vector embeddings

2. **Query Expansion Model** (1.28GB)
   - `hf_tobil_qmd-query-expansion-1.7B-q4_k_m.gguf`
   - Used for: Query expansion in hybrid search

3. **Reranking Model** (Not yet downloaded)
   - Will download on first use
   - Used for: Result reranking

---

## How OpenClaw Will Use QMD

When OpenClaw starts with `memory.backend = "qmd"`:

1. **Initialization**
   - Creates QMD home at `~/.openclaw/agents/main/qmd/`
   - Sets XDG_CONFIG_HOME and XDG_CACHE_HOME
   - Runs `qmd update` in background

2. **Memory Search**
   - Agent calls `memory_search` tool
   - OpenClaw runs `qmd search --json <query>`
   - Returns snippets with file paths and line numbers

3. **Memory Get**
   - Agent calls `memory_get` tool with path
   - OpenClaw reads the file content
   - Returns specific file or line range

4. **Auto-Update**
   - Runs `qmd update` every 5 minutes
   - Debounces file changes (15 seconds)
   - Keeps index fresh automatically

5. **Fallback**
   - If QMD fails, automatically falls back to builtin SQLite manager
   - Memory tools continue working seamlessly

---

## Search Modes Available

OpenClaw can use different QMD search modes via `memory.qmd.searchMode`:

- **`search`** (default): BM25 keyword search - fast, exact matches
- **`vsearch`**: Vector similarity - semantic, handles paraphrasing
- **`query`**: Hybrid search - combines BM25 + vectors + reranking (best quality, slower)

---

## Testing Commands

```bash
# Check status
qmd status

# List collections
qmd collection list

# Search (keyword)
qmd search "AgentMail setup"

# Search (vector)
qmd vsearch "how to configure email"

# Search (hybrid - best)
qmd query "email configuration guide"

# Get a specific file
qmd get qmd://workspace-docs/AGENTMAIL_SETUP.md

# List files in collection
qmd ls workspace-docs

# Update index
qmd update

# Re-generate embeddings
qmd embed
```

---

## Performance Notes

- **CPU-Only**: Running on CPU (no GPU acceleration)
- **First Query**: May be slow (downloading models)
- **Subsequent Queries**: Fast (models cached)
- **Embedding Speed**: ~2-3 seconds for 19 documents
- **Search Speed**: <1 second for keyword, 2-3 seconds for vector

To improve performance:
- Install CUDA toolkit for GPU acceleration
- Use `search` mode instead of `query` for faster results
- Increase `memory.qmd.limits.timeoutMs` if needed

---

## Troubleshooting

**If searches are slow:**
- First run downloads models (normal)
- CPU-only mode is slower than GPU
- Use `qmd search` instead of `qmd query` for speed

**If OpenClaw doesn't use QMD:**
- Check `openclaw.json` has `memory.backend = "qmd"`
- Verify `qmd --version` works
- Check OpenClaw logs for QMD errors
- QMD will auto-fallback to builtin if it fails

**If models don't download:**
- Check internet connection
- Models cache in `~/.cache/qmd/models/`
- Manually download: `qmd vsearch "test"` (triggers download)

---

## Next Steps

1. **Restart OpenClaw** to activate QMD backend
2. **Test memory_search** via OpenClaw agent
3. **Monitor performance** and adjust timeouts if needed
4. **Add more collections** as your knowledge base grows

---

**Status**: ✅ QMD Memory Backend Fully Configured and Tested

**OpenClaw Config**: `~/.openclaw/openclaw.json`  
**QMD Index**: `~/.cache/qmd/index.sqlite`  
**Models Cache**: `~/.cache/qmd/models/`

Ready for production use!
