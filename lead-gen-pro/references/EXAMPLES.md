# Lead Generation Examples

## Example 1: Find Marketing Agencies

**Query**: "Find 10 marketing agencies in London and get the CEO's LinkedIn"

### Workflow

1. **Search Phase**
```
Search: "top marketing agencies London"
Extract: Company names and websites from results
```

2. **Extraction Phase**
```bash
for each company:
  agent-browser open {company_website}
  agent-browser wait --load networkidle
  agent-browser snapshot -i
  
  # Look for About/Team page
  agent-browser click @e_about_link
  agent-browser wait --load networkidle
  agent-browser snapshot -i
  
  # Extract CEO information
  agent-browser get text body > company_team.txt
  
  # Parse for CEO name and LinkedIn
  # Save to leads.csv
```

3. **Output**
```csv
Company,Website,CEO Name,CEO LinkedIn,Status
Agency One,https://agencyone.com,Jane Smith,https://linkedin.com/in/janesmith,Complete
Agency Two,https://agencytwo.com,John Doe,https://linkedin.com/in/johndoe,Complete
```

## Example 2: SaaS Startup Research

**Query**: "Search for SaaS startups founded in 2025 and find their head of sales"

### Workflow

1. **Search Phase**
```
Search: "SaaS startups founded 2025"
Filter: Companies with clear websites
```

2. **Extraction Phase**
```bash
agent-browser open {startup_website}
agent-browser wait --load networkidle

# Navigate to team page
agent-browser find text "Team" click
agent-browser wait --load networkidle
agent-browser snapshot -i

# Extract sales leadership
agent-browser get text body | grep -i "head of sales\|VP sales\|sales director"
```

3. **Output**
```json
{
  "leads": [
    {
      "company": "StartupXYZ",
      "website": "https://startupxyz.com",
      "founded": "2025",
      "contacts": [
        {
          "name": "Sarah Johnson",
          "title": "Head of Sales",
          "linkedin": "https://linkedin.com/in/sarahjohnson",
          "email": "sarah@startupxyz.com"
        }
      ],
      "status": "Complete"
    }
  ]
}
```

## Example 3: Team Scraping from URL

**Query**: "Scrape the names and roles of the team at https://example.com"

### Workflow

```bash
# Open target website
agent-browser open https://example.com
agent-browser wait --load networkidle
agent-browser snapshot -i

# Find team page
agent-browser find text "Team" click
# OR try common URLs
agent-browser open https://example.com/team
agent-browser open https://example.com/about/team

agent-browser wait --load networkidle
agent-browser snapshot -i

# Extract team member cards/sections
agent-browser get text body > team_page.txt

# Parse for patterns:
# - Name followed by title
# - LinkedIn profile links
# - Email addresses
```

### Output
```csv
Name,Title,LinkedIn,Email,Status
Alice Brown,CEO,https://linkedin.com/in/alicebrown,alice@example.com,Complete
Bob Wilson,CTO,https://linkedin.com/in/bobwilson,bob@example.com,Complete
Carol Davis,Head of Marketing,https://linkedin.com/in/caroldavis,carol@example.com,Complete
```

## Example 4: Industry-Specific Lead Generation

**Query**: "Find 20 fintech companies in New York with their CFO contacts"

### Workflow

1. **Search Phase**
```
Search: "fintech companies New York"
Search: "financial technology startups NYC"
Combine and deduplicate results
```

2. **Extraction Phase**
```bash
for each company:
  # Visit company website
  agent-browser open {company_url}
  agent-browser wait --load networkidle
  
  # Try multiple approaches to find CFO
  # Approach 1: Team page
  agent-browser find text "Team" click
  agent-browser wait --load networkidle
  agent-browser get text body | grep -i "CFO\|Chief Financial Officer"
  
  # Approach 2: Leadership page
  agent-browser open {company_url}/leadership
  agent-browser wait --load networkidle
  agent-browser snapshot -i
  
  # Approach 3: About page
  agent-browser open {company_url}/about
  agent-browser wait --load networkidle
  agent-browser snapshot -i
  
  # Extract CFO details
  # Save to leads database
```

3. **Output**
```json
{
  "leads": [
    {
      "company": "FinTech Corp",
      "website": "https://fintechcorp.com",
      "industry": "Financial Technology",
      "location": "New York, NY",
      "contacts": [
        {
          "name": "Michael Chen",
          "title": "CFO",
          "linkedin": "https://linkedin.com/in/michaelchen",
          "email": "michael.chen@fintechcorp.com",
          "phone": "+1-212-555-0100"
        }
      ],
      "company_size": "50-200 employees",
      "status": "Complete"
    }
  ]
}
```

## Example 5: Conference Attendee Research

**Query**: "Find speakers at TechConf 2026 and get their contact information"

### Workflow

```bash
# Visit conference website
agent-browser open https://techconf2026.com/speakers
agent-browser wait --load networkidle
agent-browser snapshot -i

# Extract speaker list
agent-browser get text body > speakers.txt

# For each speaker:
for speaker in speakers:
  # Search for their LinkedIn
  # Search: "{speaker_name} {company} LinkedIn"
  
  # Visit their company website
  agent-browser open {company_website}
  agent-browser wait --load networkidle
  
  # Look for contact information
  agent-browser find text "Contact" click
  agent-browser wait --load networkidle
  agent-browser get text body > contact.txt
  
  # Extract email if available
  # Save to leads file
```

## Example 6: Competitor Analysis

**Query**: "Find all employees at CompetitorXYZ who work in sales"

### Workflow

```bash
# Search for company employees
# Search: "CompetitorXYZ sales team"
# Search: "CompetitorXYZ employees LinkedIn"

# Visit company website
agent-browser open https://competitorxyz.com/team
agent-browser wait --load networkidle
agent-browser snapshot -i

# Extract team members with "sales" in title
agent-browser get text body | grep -i "sales\|business development\|account"

# For each sales person found:
# - Extract name and title
# - Find LinkedIn profile
# - Look for contact information
```

## Tips for Better Results

### 1. Use Multiple Search Queries
```
Primary: "marketing agencies London"
Secondary: "top marketing firms UK"
Tertiary: "London advertising agencies"
```

### 2. Try Multiple Page Patterns
```
/team
/about
/about-us
/our-team
/leadership
/management
/contact
/company
```

### 3. Handle Dynamic Content
```bash
# Wait for JavaScript to load
agent-browser wait --load networkidle

# Wait for specific elements
agent-browser wait ".team-member"

# Scroll to load lazy content
agent-browser scroll down 1000
agent-browser wait 2000
agent-browser scroll down 1000
```

### 4. Extract Structured Data
```bash
# Look for JSON-LD structured data
agent-browser eval 'document.querySelector("script[type=\"application/ld+json\"]")?.textContent'

# Extract meta tags
agent-browser eval 'document.querySelector("meta[property=\"og:title\"]")?.content'
```

## Error Handling Examples

### Handle Missing Pages
```bash
agent-browser open https://example.com/team
if [ $? -ne 0 ]; then
  # Try alternative URL
  agent-browser open https://example.com/about
fi
```

### Handle Bot Detection
```bash
# Add delays
agent-browser wait 3000

# Use headed mode for debugging
agent-browser --headed open https://example.com

# Check for CAPTCHA
agent-browser snapshot -i | grep -i "captcha\|verify you are human"
```

### Handle Incomplete Data
```json
{
  "company": "Example Corp",
  "website": "https://example.com",
  "contacts": [],
  "status": "Incomplete",
  "missing_fields": ["email", "linkedin"],
  "notes": "Contact page not found"
}
```
