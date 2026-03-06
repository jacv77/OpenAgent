# Lead Generation Scripts

## Active Scripts

### build_prospect_pool.py
Standalone script for building the prospect pool from trade organizations.
Can be run manually or via cron job.

### check_existing_leads.py
Utility script to check database status and existing leads.

## Production Scripts

The main production scripts are located in:
`~/.openclaw/skills/lead-gen-pro/scripts/`

- `leads_database.py` - Database management class
- `send_lead_email.py` - Email sending via AgentMail
- `build_prospect_pool.py` - Prospect pool builder
- `daily_lead_gen.py` - Legacy daily generation script

## Usage

All scripts should be run from the workspace directory or via cron jobs.
