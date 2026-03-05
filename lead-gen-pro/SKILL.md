---
name: lead-gen-pro
description: "Used for searching, identifying, and extracting professional leads from the web. Trigger this when the user asks to 'find leads', 'scrape contact info', or 'research companies' in a specific industry."
metadata: { "openclaw": { "emoji": "🎯", "requires": { "bins": ["chromium", "node"] } } }
---

# Lead Generation & Professional Research

This skill enables the agent to perform multi-step lead discovery using Brave Search for discovery and Playwright/Chromium for extraction.

## Workflow

1. **Search Discovery**: Use `brave-search` to find lists of companies or LinkedIn profiles matching the target criteria.

2. **Company Deep-Dive**: For each lead, navigate to the company "About Us" or "Contact" page.

3. **Data Extraction**:
   - Extract: Name, Title, LinkedIn URL, and Website.
   - Look for patterns like `mailto:` links or contact forms.

4. **Verification**: Cross-reference found data with a secondary search if a detail (like an email) is missing.

5. **Output**: Compile all findings into a structured format (CSV or JSON).

## Instruction Rules

- **Anti-Bot Navigation**: When visiting sites, wait for `networkidle` to ensure JS-heavy content (like contact info) is loaded.
- **Privacy Compliance**: Only extract publicly available data. Do not attempt to bypass login walls unless explicitly provided with credentials.
- **Data Integrity**: If a lead is a duplicate or missing a primary contact method, flag it as "Incomplete" rather than omitting it.

## Example Queries

- "Find 10 marketing agencies in London and get the CEO's LinkedIn."
- "Scrape the names and roles of the team at [URL]."
- "Search for SaaS startups founded in 2025 and find their head of sales."

## Allowed Tools

- `brave-search`: For initial lead discovery.
- `agent-browser`: For navigating and clicking on target sites.
- `fs-write`: To save the final lead list to the workspace.

## Implementation Guide

### Step 1: Search Discovery

Use web search to find target companies or profiles:

```bash
# Search for companies in target industry
# Use search results to identify company websites and LinkedIn profiles
```

### Step 2: Navigate to Target Sites

Use agent-browser to visit company websites:

```bash
agent-browser open https://example-company.com
agent-browser wait --load networkidle
agent-browser snapshot -i
```

### Step 3: Extract Contact Information

Look for common patterns:

- **Email addresses**: Look for `mailto:` links or email patterns
- **Contact pages**: Navigate to `/contact`, `/about`, `/team` pages
- **LinkedIn profiles**: Extract from "Team" or "About Us" sections
- **Phone numbers**: Look for tel: links or formatted phone patterns

```bash
# Navigate to contact page
agent-browser open https://example-company.com/contact
agent-browser wait --load networkidle
agent-browser snapshot -i

# Extract text content
agent-browser get text body > contact_info.txt
```

### Step 4: Data Structuring

Extract and structure the data:

```javascript
// Example data structure
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
  "industry": "SaaS",
  "location": "London, UK",
  "status": "Complete"
}
```

### Step 5: Save Results

Save the compiled leads to a file:

```bash
# Save as CSV
# Save as JSON for further processing
```

## Best Practices

### 1. Rate Limiting
- Add delays between requests to avoid being blocked
- Use `agent-browser wait 2000` between page loads

### 2. Error Handling
- If a page fails to load, mark the lead as "Incomplete"
- Continue with remaining leads rather than stopping

### 3. Data Validation
- Verify email format matches standard patterns
- Check that LinkedIn URLs are valid
- Ensure phone numbers are properly formatted

### 4. Privacy & Ethics
- Only collect publicly available information
- Respect robots.txt and site terms of service
- Do not attempt to bypass authentication
- Include opt-out information in any outreach

## Common Patterns

### Finding Company Contact Pages

```bash
# Try common contact page URLs
agent-browser open https://example.com/contact
agent-browser open https://example.com/about
agent-browser open https://example.com/team
agent-browser open https://example.com/about-us
```

### Extracting Email Addresses

```bash
# Get page content and search for email patterns
agent-browser get text body | grep -E "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
```

### Finding LinkedIn Profiles

```bash
# Look for LinkedIn links in page
agent-browser snapshot -i
# Search for links containing "linkedin.com/in/" or "linkedin.com/company/"
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
    "search_query": "SaaS companies in London",
    "generated_at": "2026-03-05T20:30:00Z"
  }
}
```

## Troubleshooting

### Issue: Bot Detection
**Solution**: Add longer waits, use `--headed` mode to debug, or try different user agents

### Issue: Missing Contact Info
**Solution**: Try alternative pages (About, Team, Press), or search for "[Company Name] contact email"

### Issue: Duplicate Leads
**Solution**: Maintain a set of seen company domains to filter duplicates

### Issue: Incomplete Data
**Solution**: Mark as "Incomplete" and flag which fields are missing for manual review

## Example Workflow

```bash
# 1. Search for target companies
# (Use web search to find "top 10 marketing agencies in London")

# 2. For each company found:
agent-browser open https://company1.com
agent-browser wait --load networkidle
agent-browser snapshot -i

# 3. Navigate to contact/about page
agent-browser click @e5  # Assuming @e5 is "Contact" link
agent-browser wait --load networkidle
agent-browser snapshot -i

# 4. Extract contact information
agent-browser get text body > company1_contact.txt

# 5. Parse and structure data
# (Extract emails, names, titles from the text)

# 6. Save to leads file
# (Append to CSV or JSON file)

# 7. Close browser session
agent-browser close
```

## Compliance Notes

This skill is designed for legitimate business development and research purposes. Users must:

- Comply with GDPR, CCPA, and other data protection regulations
- Only use collected data for lawful purposes
- Provide clear opt-out mechanisms in any outreach
- Respect website terms of service and robots.txt
- Not use the skill for spam or unsolicited bulk communications

## Integration with Other Skills

- **AgentMail**: Send personalized outreach emails to discovered leads
- **QMD Memory**: Store and query lead database for future reference
- **Agent-Browser**: Primary tool for web navigation and extraction
