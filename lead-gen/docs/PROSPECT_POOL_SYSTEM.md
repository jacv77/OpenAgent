# ✅ Prospect Pool System - Two-Step Process

**Date**: March 6, 2026  
**Status**: Implemented  
**Approach**: Separate pool building from daily lead generation

## Overview

The lead generation system now uses a two-step process:

1. **Weekly**: Build prospect pool from trade organizations (100-200 companies)
2. **Daily**: Select 10 prospects from pool for deep research and outreach

## The Two-Step System

### Step 1: Prospect Pool Builder (Weekly)

**Cron Job**: `prospect-pool-builder`  
**Schedule**: Every Sunday at 8:00 AM UTC  
**Duration**: ~30-60 minutes  
**Goal**: Add 100-200 companies to prospect pool  

**Process**:
1. Research trade organization member directories
2. Extract company names, websites, segments, regions
3. Cross-check against existing database
4. Add NEW companies to prospect_pool table
5. Assign priority scores (30-100)

**Trade Organizations Researched**:
- CISAC (230+ CMOs)
- IMPALA (5,000+ labels)
- DDEX (tech companies)
- NMPA (US publishers)
- A2IM (US independents)
- WIN, ICMP, DiMA, Merlin, UK Music
- Regional: RIAJ, KOMCA, BVMI, ABMI, CAPIF

**Output**: 100-200 companies added to prospect pool

### Step 2: Daily Lead Generation (Daily)

**Cron Job**: `ae010a74-e6f1-470e-a467-f9609540a7c6`  
**Schedule**: Every day at 9:00 AM UTC  
**Duration**: ~10-15 minutes  
**Goal**: Generate 10 leads from prospect pool  

**Process**:
1. Get top 10 prospects from pool (by priority score)
2. Mark prospects as "selected"
3. Deep research on each company
4. Find decision-maker contacts
5. Validate leads
6. Create problem-solution emails
7. Send emails
8. Mark prospects as "researched"

**Output**: 10 validated leads with personalized emails

## Database Schema

### New Table: prospect_pool

```sql
CREATE TABLE prospect_pool (
    id INTEGER PRIMARY KEY,
    company_name TEXT NOT NULL,
    website TEXT UNIQUE NOT NULL,
    industry_segment TEXT,
    region TEXT,
    country TEXT,
    source_organization TEXT,
    company_size TEXT,
    notes TEXT,
    priority_score INTEGER DEFAULT 50,
    status TEXT DEFAULT 'pending',  -- pending, selected, researched
    added_at TIMESTAMP,
    researched_at TIMESTAMP,
    selected_at TIMESTAMP
);
```

### Status Flow

```
pending → selected → researched
   ↓         ↓           ↓
 (pool)  (in progress) (completed)
```

## New Database Methods

### Add to Prospect Pool
```python
db.add_to_prospect_pool(
    company_name="ASCAP",
    website="https://www.ascap.com",
    industry_segment="Performance Rights Organization",
    region="North America",
    country="USA",
    source_org="CISAC",
    company_size="Large",
    notes="Major US PRO",
    priority_score=95
)
```

### Get Prospect Pool Stats
```python
stats = db.get_prospect_pool_stats()
# Returns: total, pending, selected, researched, by_source, by_segment
```

### Get Top Prospects
```python
prospects = db.get_top_prospects(limit=10)
# Returns top 10 pending prospects (excludes already contacted)
```

### Mark Prospect Status
```python
db.mark_prospect_selected(prospect_id)
db.mark_prospect_researched(prospect_id)
```

## Priority Scoring

**90-100**: Major organizations
- ASCAP, BMI, GEMA, SACEM
- Sony, Universal, Warner
- Spotify, Apple Music

**70-89**: Large companies
- Major independents (Beggars, Ninja Tune)
- Established tech companies
- Regional leaders

**50-69**: Medium companies
- Regional players
- Growing companies
- Mid-size publishers/labels

**30-49**: Small companies
- Local organizations
- Niche players
- Startups

## Benefits

### 1. Separation of Concerns
- **Pool building**: Research-intensive, done weekly
- **Lead generation**: Execution-focused, done daily

### 2. Consistent Daily Output
- Always 10 leads per day
- No time spent searching
- Pre-qualified prospects

### 3. Strategic Coverage
- Systematic coverage of trade organizations
- Balanced across segments and regions
- Priority-based selection

### 4. Efficiency
- Weekly research vs daily research
- Faster daily execution
- Better time management

### 5. Quality Control
- Pre-vetted prospects
- Priority scoring
- Source tracking

## Workflow

### Week 1: Sunday
**Prospect Pool Builder runs**:
- Researches CISAC, IMPALA, DDEX
- Adds 150 companies to pool
- Pool status: 150 pending

### Week 1: Monday-Sunday (7 days)
**Daily Lead Generation runs**:
- Day 1: Selects top 10, sends emails (140 pending)
- Day 2: Selects top 10, sends emails (130 pending)
- Day 3: Selects top 10, sends emails (120 pending)
- ...
- Day 7: Selects top 10, sends emails (80 pending)

### Week 2: Sunday
**Prospect Pool Builder runs**:
- Researches NMPA, A2IM, WIN
- Adds 120 companies to pool
- Pool status: 200 pending (80 + 120)

### Continues...

## Monitoring

### Check Prospect Pool Status

```bash
python3 ~/.openclaw/skills/lead-gen-pro/scripts/build_prospect_pool.py status
```

Output:
```
PROSPECT POOL STATUS

Overall:
  Total prospects: 250
  Pending (available): 180
  Selected (in progress): 10
  Researched (completed): 60

By Source Organization:
  CISAC: 80
  IMPALA: 60
  DDEX: 40
  NMPA: 35
  A2IM: 35

By Industry Segment:
  Collective Management Organization: 90
  Independent Record Label: 70
  Music Publisher: 45
  Music Technology: 30
  Digital Music Service: 15

Top 10 Available Prospects:
  1. ASCAP (USA) - https://www.ascap.com
     Segment: Performance Rights Organization
     Source: CISAC, Priority: 95
  ...
```

### Check Daily Lead Generation

```bash
openclaw cron runs --id ae010a74-e6f1-470e-a467-f9609540a7c6 | head -50
```

### Database Queries

```bash
# Check prospect pool size
sqlite3 ~/.openclaw/workspace/leads.db "SELECT COUNT(*) FROM prospect_pool WHERE status='pending';"

# Check by source
sqlite3 ~/.openclaw/workspace/leads.db "SELECT source_organization, COUNT(*) FROM prospect_pool GROUP BY source_organization;"

# Check by segment
sqlite3 ~/.openclaw/workspace/leads.db "SELECT industry_segment, COUNT(*) FROM prospect_pool GROUP BY industry_segment;"

# Check top priorities
sqlite3 ~/.openclaw/workspace/leads.db "SELECT company_name, priority_score, source_organization FROM prospect_pool WHERE status='pending' ORDER BY priority_score DESC LIMIT 10;"
```

## Cron Jobs

### 1. Prospect Pool Builder
- **ID**: `prospect-pool-builder`
- **Schedule**: `0 8 * * 0` (Sunday 8 AM UTC)
- **Purpose**: Build prospect pool from trade organizations
- **Output**: 100-200 companies added

### 2. Daily Lead Generation
- **ID**: `ae010a74-e6f1-470e-a467-f9609540a7c6`
- **Schedule**: `0 9 * * *` (Daily 9 AM UTC)
- **Purpose**: Generate 10 leads from prospect pool
- **Output**: 10 validated leads with emails

## Running Manually

### Build Prospect Pool Now
```bash
openclaw cron run prospect-pool-builder
```

### Generate Daily Leads Now
```bash
openclaw cron run ae010a74-e6f1-470e-a467-f9609540a7c6
```

### Check Pool Status
```bash
python3 ~/.openclaw/skills/lead-gen-pro/scripts/build_prospect_pool.py status
```

## Expected Results

### Prospect Pool Growth
- **Week 1**: 150 companies added
- **Week 2**: +120 companies (270 total, 80 pending)
- **Week 3**: +100 companies (370 total, 110 pending)
- **Week 4**: +130 companies (500 total, 170 pending)

### Daily Lead Generation
- **Daily**: 10 leads sent
- **Weekly**: 70 leads sent
- **Monthly**: ~300 leads sent

### Pool Sustainability
- **Consumption**: 70 companies/week (10/day × 7 days)
- **Replenishment**: 100-150 companies/week
- **Net growth**: +30-80 companies/week
- **Sustainable**: Yes, pool grows over time

## Files

### Scripts
- `skills/lead-gen-pro/scripts/leads_database.py` - Database with prospect pool methods
- `skills/lead-gen-pro/scripts/build_prospect_pool.py` - Pool builder script

### Configuration
- `cron/jobs.json` - Two cron jobs (pool builder + daily leads)

### Documentation
- `skills/lead-gen-pro/references/TRADE_ORGANIZATIONS.md` - Trade org list
- `workspace/PROSPECT_POOL_SYSTEM.md` - This file

## Summary

✅ **Two-step process** - Weekly pool building + daily lead generation  
✅ **Prospect pool table** - Stores 100-200 pre-qualified companies  
✅ **Priority scoring** - 30-100 scale for strategic selection  
✅ **Status tracking** - pending → selected → researched  
✅ **Trade org sources** - 40+ organizations for comprehensive coverage  
✅ **Sustainable system** - Pool grows faster than consumption  
✅ **Efficient execution** - Daily job runs in 10-15 minutes  
✅ **Quality control** - Pre-vetted, prioritized prospects  

The prospect pool system ensures consistent daily output with strategic, systematic coverage of the entire music industry!

## Next Steps

1. **Run pool builder** - First time to populate pool
2. **Verify pool status** - Check companies added
3. **Run daily leads** - Test with pool prospects
4. **Monitor growth** - Track pool sustainability
5. **Optimize priorities** - Adjust scoring based on results

The system is ready for automated operation!
