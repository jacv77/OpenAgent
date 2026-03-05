# Agent-Browser Skill Installation

## Installation Summary

Successfully installed the agent-browser skill for OpenClaw agent.

**Date**: March 5, 2026  
**Skill Location**: `~/.openclaw/skills/agent-browser/`  
**Status**: ✅ Complete

## What Was Installed

### 1. Main Skill File
- `skills/agent-browser/SKILL.md` (19.7 KB)
  - Complete browser automation documentation
  - Core workflow patterns
  - Command reference
  - Security features
  - Common usage patterns

### 2. Reference Documentation
- `skills/agent-browser/references/authentication.md` (5.0 KB)
  - Login flows and session persistence
  - OAuth/SSO patterns
  - 2FA handling
  - Security best practices

- `skills/agent-browser/references/commands.md` (9.8 KB)
  - Complete command reference
  - All navigation, interaction, and debugging commands
  - Environment variables
  - Global options

- `skills/agent-browser/references/snapshot-refs.md` (4.3 KB)
  - Element reference system
  - Ref lifecycle management
  - Best practices
  - Troubleshooting

## Agent-Browser CLI

**Version**: 0.16.3  
**Location**: `/home/rocco/.npm-global/bin/agent-browser`  
**Usage**: `agent-browser <command>` or `npx agent-browser <command>`

## Core Workflow

The agent-browser skill enables browser automation through a simple pattern:

1. **Navigate**: `agent-browser open <url>`
2. **Snapshot**: `agent-browser snapshot -i` (get element refs like @e1, @e2)
3. **Interact**: Use refs to click, fill, select
4. **Re-snapshot**: After navigation or DOM changes, get fresh refs

## Example Usage

```bash
# Open a website
agent-browser open https://example.com

# Get interactive elements
agent-browser snapshot -i

# Interact with elements using refs
agent-browser fill @e1 "user@example.com"
agent-browser click @e2

# Take a screenshot
agent-browser screenshot page.png

# Close browser
agent-browser close
```

## Key Features

- **Element References**: Compact @ref notation reduces token usage
- **Session Management**: Persistent sessions with state saving
- **Authentication**: Built-in auth vault and state persistence
- **Screenshots & PDFs**: Capture page content
- **Form Automation**: Fill forms, click buttons, select options
- **Data Extraction**: Get text, HTML, attributes
- **Security**: Content boundaries, domain allowlists, action policies

## When to Use

The OpenClaw agent should use agent-browser whenever it needs to:
- Access websites or web pages
- Fill out forms
- Click buttons or links
- Take screenshots
- Extract data from web pages
- Test web applications
- Automate browser interactions
- Login to websites

## Browser Installation

Before first use, install the Playwright browsers:

```bash
npx playwright install
```

This downloads the required Chromium browser for agent-browser to use.

## Verification

To verify the skill is available to your agent:

```bash
# Check if agent-browser is installed
agent-browser --version

# Install browsers (first time only)
npx playwright install

# Test basic functionality
agent-browser open https://example.com
agent-browser snapshot -i
agent-browser close

# List available skills (should show agent-browser)
openclaw skills list
```

## Next Steps

The agent-browser skill is now available to all OpenClaw agents. The agent will automatically use it when web browsing or automation tasks are needed.

## Documentation

- Main skill: `~/.openclaw/skills/agent-browser/SKILL.md`
- References: `~/.openclaw/skills/agent-browser/references/`
- Official repo: https://github.com/vercel-labs/agent-browser
