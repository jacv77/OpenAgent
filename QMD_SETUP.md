# QMD Setup for OpenClaw Memory Backend

## Installation Complete ✓

### 1. Prerequisites Installed

**Bun Runtime** ✓
- Version: 1.3.10
- Location: `~/.bun/bin/bun`
- Added to PATH in `~/.bashrc`

**SQLite with Extension Support** ✓
- Version: 3.51.2
- Location: `/home/linuxbrew/.linuxbrew/bin/sqlite3`
- Extension loading: Enabled

**QMD CLI** ✓
- Version: 1.1.0
- Installed via: `bun install -g https://github.com/tobi/qmd`
- Location: `~/.bun/install/global/node_modules/@tobilu/qmd`
- Wrapper script: `/usr/local/bin/qmd`

### 2. Verification

```bash
# Check installations
bun --version          # 1.3.10
sqlite3 --version      # 3.51.2
qmd --version          # 1.1.0

# Test QMD
qmd --help
qmd status
```

### 3. Next Steps

To complete the QMD memory backend setup:

1. **Configure OpenClaw** - Set `memory.backend = "qmd"` in `openclaw.json`

2. **Add Memory Collections** - Index your workspace memory files:
   ```bash
   qmd collection add ~/.openclaw/workspace/memory --name memory-root
   ```

3. **Run Initial Embed** - Download models and build the index:
   ```bash
   qmd update
   qmd embed
   ```

4. **Test Query** - Verify it works:
   ```bash
   qmd query "test search"
   ```

### QMD Commands Reference

**Collections:**
```bash
qmd collection list                    # List all collections
qmd collection add <path> --name NAME  # Add a collection
qmd collection remove <name>           # Remove a collection
qmd collection show <name>             # Show collection details
```

**Indexing:**
```bash
qmd update          # Re-index collections
qmd embed           # Generate vector embeddings
qmd status          # View index health
```

**Search:**
```bash
qmd query <query>   # Hybrid search (recommended)
qmd search <query>  # BM25 keyword search
qmd vsearch <query> # Vector similarity only
```

**Maintenance:**
```bash
qmd cleanup         # Clear caches, vacuum DB
qmd ls              # List indexed files
```

### How QMD Works with OpenClaw

When `memory.backend = "qmd"` is set:

1. OpenClaw writes a self-contained QMD home under `~/.openclaw/agents/<agentId>/qmd/`
2. Collections are created from `memory.qmd.paths` plus default workspace memory files
3. `qmd update` and `qmd embed` run on boot and on a configurable interval
4. Searches run via `qmd search --json` (or `vsearch`/`query` depending on config)
5. If QMD fails, OpenClaw automatically falls back to builtin SQLite manager

### QMD Features

- **Hybrid Search**: Combines BM25 (keyword) + vector similarity + reranking
- **Local-First**: Runs fully locally via Bun + node-llama-cpp
- **Auto-Download**: GGUF models download from HuggingFace on first use
- **No Cloud**: No separate Ollama daemon required
- **Fast**: Uses SQLite with vector extensions for efficient search

### Configuration Location

- **QMD Index**: `~/.cache/qmd/index.sqlite`
- **QMD Config**: Set via XDG_CONFIG_HOME when OpenClaw runs it
- **OpenClaw QMD State**: `~/.openclaw/agents/main/qmd/`

### Troubleshooting

**If qmd command not found:**
```bash
export PATH="$HOME/.bun/bin:$PATH"
source ~/.bashrc
```

**If models don't download:**
- First search may be slow (downloading models)
- Check internet connection
- Models cache in `~/.cache/qmd/` or XDG_CACHE_HOME

**If extension loading fails:**
- Verify SQLite version: `sqlite3 --version`
- Check extension support: `sqlite3 :memory: ".load test" 2>&1`

---

**Status**: ✓ QMD CLI installed and ready for OpenClaw integration

**Next**: Configure `openclaw.json` with `memory.backend = "qmd"`
