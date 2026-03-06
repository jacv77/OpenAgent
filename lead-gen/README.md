# Lead Generation System

Complete lead generation system for music industry companies targeting noctil.com.

## Directory Structure

```
lead-gen/
├── docs/              # All documentation and setup guides
├── scripts/           # Active Python scripts
├── tests/             # Test results and summaries
└── archive/           # Old/deprecated scripts
```

## Key Documentation

### Setup & Configuration
- `docs/LEAD_GEN_SKILL_SETUP.md` - Initial skill setup
- `docs/DAILY_LEAD_GEN_SETUP.md` - Daily automation setup
- `docs/DATABASE_INTEGRATION.md` - Database configuration
- `docs/CRON_UPDATED.md` - Cron job configuration

### System Design
- `docs/PROSPECT_POOL_SYSTEM.md` - Two-step prospect pool system
- `docs/STRATEGIC_LEAD_GEN_V2.md` - Strategic approach documentation
- `docs/TRADE_ORG_INTEGRATION.md` - Trade organization research
- `docs/MUSIC_INDUSTRY_LEAD_GEN.md` - Music industry targeting

### Features & Fixes
- `docs/COLD_EMAIL_FIX.md` - Cold email strawman enforcement
- `docs/VALIDATION_ADDED.md` - Lead validation system
- `docs/DUPLICATE_PREVENTION_COMPLETE.md` - Deduplication logic
- `docs/TARGET_ROLES_UPDATED.md` - Expanded target roles
- `docs/CC_EMAIL_ADDED.md` - CC email configuration
- `docs/COLD_EMAIL_STRAWMAN_ADDED.md` - Cold email template

### Summaries
- `docs/SYSTEM_COMPLETE.md` - Complete system overview
- `docs/LEAD_GEN_V2_SUMMARY.md` - V2 system summary

## Active Scripts

### Production Scripts (in ~/.openclaw/skills/lead-gen-pro/scripts/)
- `leads_database.py` - Database management
- `send_lead_email.py` - Email sending via AgentMail
- `daily_lead_gen.py` - Daily lead generation (legacy)
- `build_prospect_pool.py` - Prospect pool builder

### Utility Scripts (in lead-gen/scripts/)
- `build_prospect_pool.py` - Standalone pool builder
- `check_existing_leads.py` - Check database status

## Test Results

- `tests/STRATEGIC_V2_TEST_RESULTS.md` - Strategic V2 test run
- `tests/VALIDATION_TEST_RESULTS.md` - Validation system test
- `tests/TEST_RUN_RESULTS.md` - General test results
- `tests/lead_gen_summary.txt` - Summary output

## System Overview

### Two-Step Process

1. **Prospect Pool Building** (Weekly - Sundays 8 AM UTC)
   - Research trade organizations
   - Add 100-200 companies to prospect pool
   - Priority scoring (30-100)
   - Source tracking

2. **Daily Lead Generation** (Daily - 9 AM UTC)
   - Pull 10 prospects from pool
   - Deep research on each company
   - Validate company and contacts
   - Create personalized cold emails
   - Send emails with CC to jacob.varghese@noctil.com

### Database

Location: `~/.openclaw/workspace/leads.db`

Tables:
- `prospect_pool` - Companies to research
- `companies` - Researched companies
- `contacts` - Contact information
- `leads_sent` - Sent lead tracking

### Email Configuration

- To: noctil.agent@agentmail.to
- CC: jacob.varghese@noctil.com
- API: AgentMail (am_us_ba71ac6140daeb3a04b3781992d0689b715a8c42c8ba19d8e833c6926f529bda)

### Target Audience

Music and audiovisual industry companies:
- Music Publishers
- Record Labels
- Performance Rights Organizations (PROs)
- Collective Management Organizations (CMOs)
- Music Technology Companies
- Rights Administration Companies
- Music Licensing Companies
- Distribution Companies

### Target Roles

- CEO, President, Managing Director
- CTO, CIO, VP Technology
- VP/Head of Rights Management
- VP/Head of Operations
- VP/Head of Metadata
- Director of Rights Administration
- Senior Managers with decision authority

### Deduplication Rules

- Same company + same contact = duplicate (skip)
- Same company + different contact = allowed (send)
- Different company = allowed (send)

### Validation Requirements

1. Company website accessible and active
2. LinkedIn profile exists and is real
3. Current employment verified
4. Cold email strawman populated (REQUIRED)

## Cron Jobs

### Prospect Pool Builder
- ID: `prospect-pool-builder`
- Schedule: `0 8 * * 0` (Sundays 8 AM UTC)
- Purpose: Build prospect pool from trade organizations

### Daily Lead Generation
- ID: `ae010a74-e6f1-470e-a467-f9609540a7c6`
- Schedule: `0 9 * * *` (Daily 9 AM UTC)
- Purpose: Generate 10 new leads from prospect pool

## Recent Updates

- ✅ Cold email strawman enforcement (2026-03-06)
- ✅ Prospect pool system (2026-03-06)
- ✅ Trade organization integration (2026-03-06)
- ✅ Strategic problem-solution approach (2026-03-05)
- ✅ Expanded target roles (2026-03-05)
- ✅ Lead validation system (2026-03-05)

## Support

For issues or questions, refer to the documentation in the `docs/` folder.
