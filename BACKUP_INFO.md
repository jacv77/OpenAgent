# OpenClaw Configuration Backup

## Branch: openclaw-full-backup

This branch contains a backup of the OpenClaw configuration from `~/.openclaw/`.

### What's Included ✓

- **AgentMail Skill** - Complete skill with scripts and documentation
  - `skills/agentmail/SKILL.md` - Skill documentation
  - `skills/agentmail/scripts/` - Python scripts for email operations
  - `skills/agentmail/references/` - API and webhook documentation

- **Shell Completions** - Auto-completion for various shells
  - `completions/openclaw.bash`
  - `completions/openclaw.zsh`
  - `completions/openclaw.fish`
  - `completions/openclaw.ps1`

- **Configuration Files**
  - `canvas/index.html` - Canvas UI
  - `cron/jobs.json` - Scheduled jobs
  - `devices/pending.json` - Device pairing queue
  - `exec-approvals.json` - Execution approvals
  - `identity/device.json` - Device identity (non-sensitive)
  - `logs/config-audit.jsonl` - Configuration audit log
  - `update-check.json` - Update check status
  - `.clawhub/lock.json` - ClawHub package lock

### What's Excluded (Security) 🔒

For security reasons, the following files are NOT included in this backup:

- **API Keys & Credentials**
  - `agents/main/agent/auth-profiles.json` - Contains Anthropic API keys
  - `credentials/` - Telegram and other service credentials
  - `identity/device-auth.json` - Device authentication tokens
  - `openclaw.json` - Main config with API keys and bot tokens
  - `openclaw.json.bak*` - Config backups

- **Session Data**
  - `agents/main/sessions/` - Agent conversation sessions

- **Database Files**
  - `memory/main.sqlite` - Memory database

- **Media Files**
  - `media/inbound/*.ogg` - Voice message recordings

- **Telegram State**
  - `telegram/` - Bot state and command hashes

- **Device Pairing**
  - `devices/paired.json` - Paired device information

### Restoring from Backup

To restore these files:

1. Clone the repository and checkout this branch:
   ```bash
   git clone https://github.com/jacv77/OpenAgent.git
   cd OpenAgent
   git checkout openclaw-full-backup
   ```

2. Copy files to `~/.openclaw/`:
   ```bash
   cp -r * ~/.openclaw/
   ```

3. **Important:** You'll need to manually restore sensitive files:
   - Reconfigure API keys in `openclaw.json`
   - Set up Telegram bot credentials
   - Re-pair devices if needed
   - Restore session data if available from separate backup

### .gitignore

A `.gitignore` file has been added to prevent accidentally committing sensitive data:

```gitignore
# Sensitive configuration files
agents/main/agent/auth-profiles.json
credentials/
identity/device-auth.json
openclaw.json
openclaw.json.bak*
telegram/

# Session data
agents/main/sessions/

# Database files
*.sqlite
*.db

# Media files
media/

# Device pairing
devices/paired.json
```

### Repository Structure

```
OpenAgent/
├── .gitignore
├── AGENTMAIL_SETUP.md
├── AGENTMAIL_TEST_RESULTS.md
├── BACKUP_INFO.md (this file)
├── .clawhub/
│   └── lock.json
├── canvas/
│   └── index.html
├── completions/
│   ├── openclaw.bash
│   ├── openclaw.fish
│   ├── openclaw.ps1
│   └── openclaw.zsh
├── cron/
│   └── jobs.json
├── devices/
│   └── pending.json
├── exec-approvals.json
├── identity/
│   └── device.json
├── logs/
│   └── config-audit.jsonl
├── skills/
│   └── agentmail/
│       ├── SKILL.md
│       ├── _meta.json
│       ├── references/
│       │   ├── API.md
│       │   ├── EXAMPLES.md
│       │   └── WEBHOOKS.md
│       └── scripts/
│           ├── check_inbox.py
│           ├── send_email.py
│           └── setup_webhook.py
├── update-check.json
└── [AgentMail test scripts and documentation]
```

### Notes

- This backup was created on: 2026-03-05
- OpenClaw version: 2026.3.2
- Repository: https://github.com/jacv77/OpenAgent.git
- Branch: `openclaw-full-backup`
- Main branch: `master` (contains AgentMail test scripts only)

### Security Reminder

⚠️ **Never commit sensitive data to public repositories!**

Always review files before committing to ensure no API keys, tokens, or credentials are included.

---

*For questions or issues, refer to the OpenClaw documentation or AgentMail setup guides in this repository.*
