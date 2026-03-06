# Lead-Gen-Pro Skill Setup

## Installation Summary

Successfully created the lead-gen-pro skill for OpenClaw agent.

**Date**: March 5, 2026  
**Skill Location**: `~/.openclaw/skills/lead-gen-pro/`  
**Status**: ✅ Created (requires chromium installation)

## What Was Installed

### 1. Main Skill File
- `skills/lead-gen-pro/SKILL.md` - Complete lead generation documentation
  - Multi-step workflow for lead discovery
  - Search, extraction, and verification processes
  - Data structuring and output formats
  - Privacy and compliance guidelines

### 2. Metadata
- `skills/lead-gen-pro/_meta.json` - Skill configuration
  - Version: 1.0.0
  - Requires: agent-browser skill, chromium, node
  - Tags: lead-generation, research, scraping, business-development

### 3. Reference Documentation
- `skills/lead-gen-pro/references/BEST_PRACTICES.md` - Comprehensive best practices
  - Ethical guidelines and privacy compliance
  - Technical implementation patterns
  - Data quality and validation
  - Performance optimization
  - Compliance checklist

- `skills/lead-gen-pro/references/EXAMPLES.md` - Real-world examples
  - Marketing agency research
  - SaaS startup discovery
  - Team member extraction
  - Industry-specific lead generation
  - Conference attendee research
  - Competitor analysis

## Skill Capabilities

The lead-gen-pro skill enables your OpenClaw agent to:

1. **Search Discovery**: Find companies and professionals matching target criteria
2. **Company Deep-Dive**: Navigate to company websites and extract information
3. **Data Extraction**: Extract names, titles, LinkedIn URLs, emails, phone numbers
4. **Verification**: Cross-reference and validate collected data
5. **Output**: Generate structured CSV or JSON lead lists

## Workflow

```
1. Search Discovery (Brave Search)
   ↓
2. Navigate to Company Website (agent-browser)
   ↓
3. Extract Contact Information
   ↓
4. Verify and Validate Data
   ↓
5. Save to Structured Format (CSV/JSON)
```

## Requirements

### Required Tools
- ✅ **agent-browser**: Installed and configured
- ✅ **node**: Available at `/usr/bin/node`
- ⚠️ **chromium**: Needs installation (via Playwright)

### Install Chromium

The skill requires Chromium browser for web automation. Install via Playwright:

```bash
# Install Playwright browsers (includes Chromium)
npx playwright install chromium

# Or install all browsers
npx playwright install
```

After installation, verify:
```bash
openclaw skills list | grep lead-gen-pro
# Should show "✓ ready" instead of "✗ missing"
```

## Configuration

The skill is enabled in `openclaw.json`:

```json
{
  "skills": {
    "entries": {
      "lead-gen-pro": {
        "enabled": true
      }
    }
  }
}
```

## Example Usage

### Find Marketing Agencies
```
User: "Find 10 marketing agencies in London and get the CEO's LinkedIn"

Agent will:
1. Search for "top marketing agencies London"
2. Visit each company website
3. Navigate to About/Team pages
4. Extract CEO name and LinkedIn profile
5. Save results to CSV file
```

### Research SaaS Startups
```
User: "Search for SaaS startups founded in 2025 and find their head of sales"

Agent will:
1. Search for "SaaS startups founded 2025"
2. Visit startup websites
3. Find team/leadership pages
4. Extract sales leadership contacts
5. Generate JSON output with structured data
```

### Scrape Team Information
```
User: "Scrape the names and roles of the team at https://example.com"

Agent will:
1. Navigate to the specified URL
2. Find the team page
3. Extract all team member information
4. Save to CSV with names, titles, and contact info
```

## Output Formats

### CSV Format
```csv
Company,Website,Name,Title,Email,LinkedIn,Phone,Status
Example Corp,https://example.com,John Doe,CEO,john@example.com,https://linkedin.com/in/johndoe,+1-555-0100,Complete
```

### JSON Format
```json
{
  "leads": [
    {
      "company": "Example Corp",
      "website": "https://example.com",
      "contacts": [
        {
          "name": "John Doe",
          "title": "CEO",
          "email": "john@example.com",
          "linkedin": "https://linkedin.com/in/johndoe",
          "phone": "+1-555-0100"
        }
      ],
      "status": "Complete",
      "extracted_at": "2026-03-05T20:30:00Z"
    }
  ],
  "metadata": {
    "total_leads": 1,
    "complete": 1,
    "incomplete": 0,
    "generated_at": "2026-03-05T20:30:00Z"
  }
}
```

## Privacy & Compliance

The skill is designed with privacy and compliance in mind:

- ✅ Only collects publicly available information
- ✅ Respects robots.txt and site terms of service
- ✅ Does not bypass authentication
- ✅ Includes rate limiting to avoid server overload
- ✅ Marks incomplete data rather than guessing
- ✅ Provides compliance guidelines for GDPR, CCPA, CAN-SPAM

### Compliance Checklist

When using this skill, ensure you:
- [ ] Have lawful basis for processing data
- [ ] Provide privacy notices
- [ ] Include opt-out mechanisms in outreach
- [ ] Store data securely
- [ ] Implement data retention policies
- [ ] Enable data deletion on request
- [ ] Do not use for spam or unsolicited bulk email

## Best Practices

### 1. Rate Limiting
- Add 2-5 second delays between requests
- Use `agent-browser wait 2000` between page loads
- Avoid overwhelming target servers

### 2. Data Quality
- Validate email formats
- Verify LinkedIn URLs are accessible
- Check phone number formatting
- Remove duplicates

### 3. Error Handling
- Mark leads as "Incomplete" if data is missing
- Continue processing remaining leads on errors
- Log all errors for review

### 4. Anti-Bot Detection
- Wait for `networkidle` to ensure full page load
- Use realistic viewport sizes
- Add human-like delays between actions

## Integration with Other Skills

### AgentMail Integration
Use lead-gen-pro to find leads, then use AgentMail to send personalized outreach:

```
1. Generate leads with lead-gen-pro
2. Review and filter leads
3. Use AgentMail to send personalized emails
4. Track responses
```

### QMD Memory Integration
Store leads in QMD memory for future reference:

```
1. Generate leads with lead-gen-pro
2. Save to QMD memory backend
3. Query leads later: "Show me all SaaS leads from London"
4. Update lead status as you engage
```

## Troubleshooting

### Issue: Skill shows as "missing"
**Solution**: Install Chromium via `npx playwright install chromium`

### Issue: Bot detection / CAPTCHA
**Solution**: 
- Add longer delays between requests
- Use `--headed` mode to debug
- Respect rate limits

### Issue: Missing contact information
**Solution**:
- Try alternative pages (About, Team, Press)
- Search for "[Company Name] contact email"
- Mark as "Incomplete" and flag missing fields

### Issue: Duplicate leads
**Solution**: Implement deduplication by checking company domains before adding

## Next Steps

1. **Install Chromium**: Run `npx playwright install chromium`
2. **Verify Installation**: Run `openclaw skills list | grep lead-gen-pro`
3. **Test the Skill**: Ask your agent to "Find 5 tech companies in San Francisco"
4. **Review Output**: Check the generated CSV or JSON file
5. **Refine Queries**: Adjust search terms for better results

## Documentation

- Main skill: `~/.openclaw/skills/lead-gen-pro/SKILL.md`
- Best practices: `~/.openclaw/skills/lead-gen-pro/references/BEST_PRACTICES.md`
- Examples: `~/.openclaw/skills/lead-gen-pro/references/EXAMPLES.md`
- Metadata: `~/.openclaw/skills/lead-gen-pro/_meta.json`

## Support

For issues or questions:
- Check the troubleshooting section above
- Review the examples in `references/EXAMPLES.md`
- Consult best practices in `references/BEST_PRACTICES.md`
- Check OpenClaw docs: https://docs.openclaw.ai/tools/skills
