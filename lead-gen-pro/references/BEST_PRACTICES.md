# Lead Generation Best Practices

## Ethical Guidelines

### 1. Respect Privacy
- Only collect publicly available information
- Do not attempt to bypass authentication or paywalls
- Respect robots.txt and site terms of service
- Include opt-out mechanisms in any outreach

### 2. Data Protection Compliance
- **GDPR**: Ensure lawful basis for processing (legitimate interest)
- **CCPA**: Provide clear privacy notices
- **CAN-SPAM**: Include unsubscribe options in emails
- Store data securely and delete when no longer needed

### 3. Rate Limiting
- Add delays between requests (2-5 seconds minimum)
- Limit concurrent requests to same domain
- Respect server load and bandwidth

## Technical Best Practices

### 1. Anti-Bot Detection

```bash
# Wait for full page load
agent-browser wait --load networkidle

# Add human-like delays
agent-browser wait 2000

# Use realistic viewport sizes
agent-browser set viewport 1920 1080

# Avoid patterns that look automated
# - Don't request pages too quickly
# - Vary timing between actions
# - Don't follow exact same path every time
```

### 2. Data Quality

```bash
# Validate email format
echo "test@example.com" | grep -E "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# Verify LinkedIn URL format
echo "https://linkedin.com/in/username" | grep -E "linkedin.com/(in|company)/"

# Check phone number format
echo "+1-555-0100" | grep -E "^\+?[0-9]{1,3}[-. ]?(\([0-9]{3}\)|[0-9]{3})[-. ]?[0-9]{3}[-. ]?[0-9]{4}$"
```

### 3. Error Handling

```bash
# Retry on failure
MAX_RETRIES=3
RETRY_COUNT=0

while [ $RETRY_COUNT -lt $MAX_RETRIES ]; do
  agent-browser open https://example.com
  if [ $? -eq 0 ]; then
    break
  fi
  RETRY_COUNT=$((RETRY_COUNT + 1))
  agent-browser wait 5000
done
```

### 4. Deduplication

```json
{
  "seen_domains": ["example.com", "test.com"],
  "seen_emails": ["john@example.com"],
  "seen_linkedin": ["https://linkedin.com/in/johndoe"]
}
```

## Search Strategy

### 1. Use Multiple Sources

```
Primary: Company website
Secondary: LinkedIn company page
Tertiary: Crunchbase, AngelList
Quaternary: News articles, press releases
```

### 2. Search Query Optimization

```
Good: "SaaS companies London 2025"
Better: "B2B SaaS startups London founded 2025"
Best: "enterprise software companies London Series A 2025"
```

### 3. Boolean Search

```
"marketing agency" AND London AND (CEO OR founder)
"fintech" AND "New York" AND (CFO OR "Chief Financial Officer")
site:linkedin.com "Head of Sales" "SaaS" "San Francisco"
```

## Data Extraction Patterns

### 1. Email Patterns

```regex
# Standard email
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}

# Common obfuscation
name [at] domain [dot] com
name(at)domain(dot)com
```

### 2. Phone Patterns

```regex
# US format
\+?1?[-. ]?\(?[0-9]{3}\)?[-. ]?[0-9]{3}[-. ]?[0-9]{4}

# International
\+[0-9]{1,3}[-. ]?[0-9]{1,4}[-. ]?[0-9]{1,4}[-. ]?[0-9]{1,9}
```

### 3. LinkedIn Patterns

```regex
# Personal profile
linkedin\.com/in/[a-zA-Z0-9-]+

# Company page
linkedin\.com/company/[a-zA-Z0-9-]+
```

## Output Formatting

### CSV Best Practices

```csv
# Include header row
Company,Website,Name,Title,Email,LinkedIn,Phone,Status,Notes,Extracted_Date

# Escape commas in fields
"Example, Inc.",https://example.com,John Doe,CEO,john@example.com,...

# Use consistent date format
...,Complete,,2026-03-05T20:30:00Z

# Include status field
...,Complete,...
...,Incomplete,...
...,Verification_Needed,...
```

### JSON Best Practices

```json
{
  "metadata": {
    "version": "1.0",
    "generated_at": "2026-03-05T20:30:00Z",
    "query": "SaaS companies London",
    "total_leads": 50,
    "complete": 45,
    "incomplete": 5
  },
  "leads": [
    {
      "id": "lead_001",
      "company": {
        "name": "Example Corp",
        "website": "https://example.com",
        "industry": "SaaS",
        "location": "London, UK",
        "size": "50-200"
      },
      "contacts": [
        {
          "name": "John Doe",
          "title": "CEO",
          "email": "john@example.com",
          "linkedin": "https://linkedin.com/in/johndoe",
          "phone": "+44-20-1234-5678",
          "verified": true
        }
      ],
      "status": "Complete",
      "extracted_at": "2026-03-05T20:30:00Z",
      "source_url": "https://example.com/team"
    }
  ]
}
```

## Performance Optimization

### 1. Parallel Processing

```bash
# Process multiple leads concurrently
# Use separate browser sessions
agent-browser --session lead1 open https://company1.com &
agent-browser --session lead2 open https://company2.com &
agent-browser --session lead3 open https://company3.com &
wait
```

### 2. Caching

```bash
# Cache company websites to avoid re-fetching
if [ -f "cache/example.com.html" ]; then
  # Use cached version
else
  # Fetch and cache
  agent-browser open https://example.com
  agent-browser get html body > cache/example.com.html
fi
```

### 3. Incremental Saves

```bash
# Save after each lead instead of at the end
# Prevents data loss if process is interrupted
echo "$lead_data" >> leads.csv
```

## Quality Assurance

### 1. Validation Checklist

- [ ] Email format is valid
- [ ] LinkedIn URL is accessible
- [ ] Phone number is properly formatted
- [ ] Company website is reachable
- [ ] No duplicate entries
- [ ] All required fields present

### 2. Verification Steps

```bash
# Verify email deliverability (basic check)
host -t MX example.com

# Verify LinkedIn profile exists
agent-browser open https://linkedin.com/in/username
agent-browser get title | grep -v "Page Not Found"

# Verify company website is active
curl -I https://example.com | grep "200 OK"
```

### 3. Data Enrichment

```bash
# Add company size from LinkedIn
agent-browser open https://linkedin.com/company/example
agent-browser get text body | grep -i "employees"

# Add industry classification
# Search for company on Crunchbase or similar

# Add funding information
# Search for company on AngelList or PitchBook
```

## Compliance Checklist

- [ ] Only collecting publicly available data
- [ ] Not bypassing authentication
- [ ] Respecting robots.txt
- [ ] Including opt-out mechanism
- [ ] Storing data securely
- [ ] Have lawful basis for processing
- [ ] Providing privacy notice
- [ ] Implementing data retention policy
- [ ] Enabling data deletion on request
- [ ] Not using for spam or unsolicited bulk email

## Common Pitfalls to Avoid

### 1. Over-Automation
❌ Requesting 1000 pages in 5 minutes
✅ Spread requests over time with delays

### 2. Ignoring Errors
❌ Continuing when pages fail to load
✅ Log errors and mark leads as incomplete

### 3. Poor Data Quality
❌ Saving invalid emails or broken links
✅ Validate all data before saving

### 4. No Deduplication
❌ Same lead appears multiple times
✅ Check for duplicates before adding

### 5. Missing Context
❌ Just name and email with no other info
✅ Include company, title, source URL, date

## Monitoring and Logging

```bash
# Log all actions
echo "[$(date)] Opening https://example.com" >> lead_gen.log

# Track success rate
echo "Total: 100, Complete: 85, Incomplete: 15" >> stats.log

# Monitor for errors
if [ $? -ne 0 ]; then
  echo "[ERROR] Failed to load page" >> errors.log
fi
```

## Documentation

Always document:
- Search queries used
- Date of extraction
- Source URLs
- Any manual verification performed
- Known limitations or missing data
- Compliance measures taken
