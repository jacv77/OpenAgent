# Database Integration Complete

## ✅ SQLite Database Added for Lead Tracking

**Date**: March 6, 2026  
**Status**: ✅ Integrated with Cron Job  
**Database**: `~/.openclaw/workspace/leads.db`

## What's New

The daily lead generation system now includes a SQLite database that:

1. **Stores all lead data** - companies, contacts, and sent emails
2. **Prevents duplicates** - automatically skips leads already sent
3. **Allows multiple contacts** - different contacts from same company are allowed
4. **Tracks email delivery** - records message IDs and thread IDs
5. **Provides statistics** - total companies, contacts, and leads sent

## Database Schema

### Companies Table
Stores company information:
- name, website (unique), industry_segment
- location, company_size, description
- technology_stack, recent_news
- created_at, updated_at timestamps

### Contacts Table
Stores contact information:
- company_id (foreign key)
- name, title, email, linkedin_url, phone
- profile_summary, decision_authority
- created_at timestamp
- Unique constraint: (company_id, email)

### Leads Sent Table
Tracks sent emails:
- company_id, contact_id (foreign keys)
- email_subject, email_sent_at
- message_id, thread_id (from AgentMail)
- status (default: 'sent')

## Deduplication Rules

The system follows these rules:

✅ **ALLOWED** - Different company = always send  
✅ **ALLOWED** - Same company + different contact email = send  
❌ **BLOCKED** - Same company + same contact email = duplicate (skip)

### Examples

```
Company A + contact1@companyA.com → ✅ Send (first time)
Company A + contact1@companyA.com → ❌ Skip (duplicate)
Company A + contact2@companyA.com → ✅ Send (different contact)
Company B + contact1@companyB.com → ✅ Send (different company)
```

## How It Works

### 1. Lead Discovery
Agent searches for music industry companies and finds decision-makers.

### 2. Duplicate Check
Before sending, the system checks:
- Does this company exist in database? (by website)
- Does this contact exist for this company? (by email)
- Was this exact lead already sent?

### 3. Email Sending
If not a duplicate:
- Add company to database (or update if exists)
- Add contact to database (or update if exists)
- Send email via AgentMail
- Record in leads_sent table with message_id and thread_id

### 4. Statistics
After each run, the agent reports:
- Total companies in database
- Total contacts in database
- Total leads sent
- Companies contacted

## Updated Cron Job

The cron job now uses the database-backed system:

```python
# Import the database-backed sending function
import sys
from pathlib import Path
sys.path.insert(0, str(Path.home() / '.openclaw' / 'skills' / 'lead-gen-pro' / 'scripts'))

from send_lead_email import send_lead_email
from leads_database import LeadsDatabase

# For each lead found
result = send_lead_email(company_data, contact_data, value_proposition)

# Result contains:
# - sent: True/False
# - reason: Why it was sent or skipped
# - company: Company name
# - contact: Contact name
# - message_id: AgentMail message ID (if sent)
# - thread_id: AgentMail thread ID (if sent)
```

## Database Scripts

### leads_database.py
Core database management:
- `LeadsDatabase()` - Initialize database
- `is_duplicate_lead()` - Check if lead is duplicate
- `add_company()` - Add or update company
- `add_contact()` - Add or update contact
- `record_lead_sent()` - Record sent email
- `get_stats()` - Get database statistics
- `get_recent_leads()` - Get recently sent leads
- `export_to_json()` - Export all data to JSON

### send_lead_email.py
Email sending with database integration:
- `send_lead_email()` - Send email and track in database
- Automatically checks for duplicates
- Formats professional HTML and text emails
- Records message_id and thread_id
- Returns detailed result

## Database Location

```
~/.openclaw/workspace/leads.db
```

The database is created automatically on first use.

## Checking Database Stats

### From Python

```python
from leads_database import LeadsDatabase

db = LeadsDatabase()
stats = db.get_stats()

print(f"Total companies: {stats['total_companies']}")
print(f"Total contacts: {stats['total_contacts']}")
print(f"Total leads sent: {stats['total_leads_sent']}")
print(f"Companies contacted: {stats['companies_contacted']}")
```

### Recent Leads

```python
db = LeadsDatabase()
recent = db.get_recent_leads(10)

for lead in recent:
    print(f"{lead['company_name']} / {lead['contact_name']}")
    print(f"  Email: {lead['email']}")
    print(f"  Sent: {lead['email_sent_at']}")
    print(f"  Status: {lead['status']}")
```

### Export to JSON

```python
db = LeadsDatabase()
output_file = db.export_to_json()
print(f"Exported to: {output_file}")
```

This creates `~/.openclaw/workspace/leads_export.json` with:
- All companies with their contacts
- All sent leads with timestamps
- Database statistics

## Testing the System

### Test with Example Lead

```bash
cd ~/.openclaw/skills/lead-gen-pro/scripts
python3 send_lead_email.py
```

This sends a test lead and shows:
- Whether it was sent or skipped
- Reason (new lead, duplicate, etc.)
- Message ID and Thread ID
- Database statistics

### Check Database

```bash
cd ~/.openclaw/skills/lead-gen-pro/scripts
python3 leads_database.py
```

This shows:
- Database location
- Current statistics
- Recent leads

### Query Database Directly

```bash
sqlite3 ~/.openclaw/workspace/leads.db

# Show all companies
SELECT name, website, industry_segment FROM companies;

# Show all contacts
SELECT c.name as company, ct.name as contact, ct.email, ct.title 
FROM contacts ct 
JOIN companies c ON ct.company_id = c.id;

# Show sent leads
SELECT c.name as company, ct.name as contact, ls.email_sent_at 
FROM leads_sent ls 
JOIN companies c ON ls.company_id = c.id 
JOIN contacts ct ON ls.contact_id = ct.id 
ORDER BY ls.email_sent_at DESC;

# Count by industry segment
SELECT industry_segment, COUNT(*) 
FROM companies 
GROUP BY industry_segment;
```

## What Happens Tomorrow

When the cron job runs at 9:00 AM UTC:

1. **Agent searches** for 10 music industry companies
2. **For each lead found**:
   - Check if it's a duplicate
   - If duplicate: skip and log reason
   - If new: send email and record in database
3. **Agent reports**:
   - How many leads were sent
   - How many were skipped as duplicates
   - Database statistics
4. **You receive**:
   - Individual emails for each NEW lead
   - No duplicate emails
   - Different contacts from same company are allowed

## Benefits

### No More Duplicates
You won't receive the same lead twice (same company + same contact).

### Multiple Contacts Allowed
If the agent finds different contacts at the same company, they'll all be sent.

### Complete History
All leads are stored in the database with full details.

### Easy Tracking
Query the database to see:
- Which companies have been contacted
- Which contacts have been reached
- When leads were sent
- Email delivery status

### Export Capability
Export all data to JSON for:
- CRM import
- Spreadsheet analysis
- Backup
- Reporting

## Monitoring

### Check Database Growth

```bash
# Database file size
ls -lh ~/.openclaw/workspace/leads.db

# Record counts
sqlite3 ~/.openclaw/workspace/leads.db "SELECT 
  (SELECT COUNT(*) FROM companies) as companies,
  (SELECT COUNT(*) FROM contacts) as contacts,
  (SELECT COUNT(*) FROM leads_sent) as sent;"
```

### Check for Duplicates Prevented

```bash
# Check agent logs for "Duplicate" messages
openclaw logs | grep -i duplicate

# Or check the cron run output
openclaw cron runs | grep -A 20 "ae010a74"
```

### Export and Analyze

```python
from leads_database import LeadsDatabase
import json

db = LeadsDatabase()

# Export to JSON
output_file = db.export_to_json()

# Load and analyze
with open(output_file) as f:
    data = json.load(f)

print(f"Total companies: {len(data['companies'])}")
print(f"Total leads sent: {data['stats']['total_leads_sent']}")

# Companies by segment
segments = {}
for company in data['companies']:
    seg = company['industry_segment']
    segments[seg] = segments.get(seg, 0) + 1

print("\nCompanies by segment:")
for seg, count in sorted(segments.items(), key=lambda x: -x[1]):
    print(f"  {seg}: {count}")
```

## Troubleshooting

### Database Not Created

If the database doesn't exist after a run:
1. Check agent logs for errors
2. Verify Python path is correct
3. Test manually: `python3 ~/.openclaw/skills/lead-gen-pro/scripts/leads_database.py`

### Duplicates Still Being Sent

If you receive duplicate leads:
1. Check if the website URL is exactly the same
2. Check if the contact email is exactly the same
3. Query database to verify: `sqlite3 ~/.openclaw/workspace/leads.db "SELECT * FROM leads_sent;"`

### Database Locked

If you get "database is locked" errors:
1. Close any open SQLite connections
2. Check for other processes accessing the database
3. Restart the OpenClaw gateway

### Reset Database

To start fresh (WARNING: deletes all data):

```bash
rm ~/.openclaw/workspace/leads.db
```

The database will be recreated on next run.

## Files

### Database Scripts
- `~/.openclaw/skills/lead-gen-pro/scripts/leads_database.py`
- `~/.openclaw/skills/lead-gen-pro/scripts/send_lead_email.py`

### Database File
- `~/.openclaw/workspace/leads.db`

### Cron Job
- ID: `ae010a74-e6f1-470e-a467-f9609540a7c6`
- Config: `cron/jobs.json`

### Documentation
- This file: `workspace/DATABASE_INTEGRATION.md`
- Setup: `workspace/DAILY_LEAD_GEN_SETUP.md`
- Targeting: `skills/lead-gen-pro/references/MUSIC_INDUSTRY_TARGETING.md`

## Summary

✅ SQLite database integrated with lead generation  
✅ Automatic duplicate prevention  
✅ Multiple contacts per company allowed  
✅ Complete lead history tracking  
✅ Email delivery tracking (message_id, thread_id)  
✅ Statistics and reporting  
✅ JSON export capability  
✅ Cron job updated to use database system  

Your lead generation system now has intelligent deduplication and complete tracking!
