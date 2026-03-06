# Lead Generation System - Quick Reference

## ✅ System Status

**Database**: Active at `~/.openclaw/workspace/leads.db`  
**Cron Job**: Active, runs daily at 9:00 AM UTC  
**Next Run**: In ~6 hours  
**Deduplication**: Enabled  

## Quick Commands

### Check Database Stats
```bash
python3 ~/.openclaw/skills/lead-gen-pro/scripts/leads_database.py
```

### Test Email Sending
```bash
python3 ~/.openclaw/skills/lead-gen-pro/scripts/send_lead_email.py
```

### View Cron Status
```bash
openclaw cron list
```

### Run Cron Job Now
```bash
openclaw cron run ae010a74-e6f1-470e-a467-f9609540a7c6
```

### Check Recent Leads
```bash
sqlite3 ~/.openclaw/workspace/leads.db "SELECT c.name, ct.name, ct.email, ls.email_sent_at FROM leads_sent ls JOIN companies c ON ls.company_id = c.id JOIN contacts ct ON ls.contact_id = ct.id ORDER BY ls.email_sent_at DESC LIMIT 10;"
```

### Export Database to JSON
```python
from leads_database import LeadsDatabase
db = LeadsDatabase()
db.export_to_json()
# Creates: ~/.openclaw/workspace/leads_export.json
```

### Check for Duplicates
```bash
openclaw logs | grep -i duplicate
```

## Deduplication Rules

✅ **Send** - New company  
✅ **Send** - Same company, different contact  
❌ **Skip** - Same company, same contact (duplicate)  

## What Happens Daily

1. Agent finds 10 music industry companies
2. For each lead:
   - Check database for duplicates
   - If new: send email + record in database
   - If duplicate: skip + log reason
3. You receive emails for NEW leads only
4. Database tracks everything

## Files

- Database: `~/.openclaw/workspace/leads.db`
- Scripts: `~/.openclaw/skills/lead-gen-pro/scripts/`
- Cron: `cron/jobs.json` (ID: ae010a74-e6f1-470e-a467-f9609540a7c6)

## Documentation

- Full setup: `workspace/DATABASE_INTEGRATION.md`
- Targeting: `skills/lead-gen-pro/references/MUSIC_INDUSTRY_TARGETING.md`
- Test results: `workspace/TEST_RUN_RESULTS.md`
