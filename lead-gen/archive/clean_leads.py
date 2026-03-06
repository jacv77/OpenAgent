import csv
import re
import sys

def clean_website(html_link):
    if not html_link: return ""
    import html
    decoded = html.unescape(html_link)
    # Extract href from <a href="...">...</a>
    match = re.search(r'href=["\'](.*?)["\']', decoded)
    if match:
        return match.group(1)
    return html_link

input_file = 'leads.tsv'
output_file = 'leads.csv'

try:
    with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', newline='', encoding='utf-8') as f_out:
        # It looks like a TSV based on the head output
        reader = csv.reader(f_in, delimiter='\t')
        writer = csv.writer(f_out)
        
        # Header
        headers = next(reader)
        # We want: Society, Country, Website, Type, Status, Contact Name, Email, Draft, Notes (Phone)
        writer.writerow(['Organization', 'Country', 'Website', 'Type', 'Status', 'Contact Name', 'Email', 'Draft', 'Notes'])
        
        # Map indices (based on head output):
        # 0: Society
        # 1: Society contact phone
        # 2: Country
        # 6: Website
        # 10: Membership status
        # 11: Rightsholder represented
        
        for row in reader:
            if len(row) < 12: continue # Skip malformed rows
            
            society = row[0]
            phone = row[1]
            country = row[2]
            website = clean_website(row[6])
            
            # Combine Status + Rightsholder into Type/Notes
            org_type = row[11] # e.g. "Multi-rightholder CMO"
            
            notes = f"Phone: {phone}"
            
            draft = ""
            if society == "ABRAMUS":
                draft = f"Subject: Automating rights collection for ABRAMUS\n\nHi [Name],\n\nI noticed ABRAMUS represents a significant roster of performers in Brazil. Managing rights collection across borders can be complex...\n\nAt Noctil, we specialize in helping rights holders like ABRAMUS streamline this process..."

            writer.writerow([society, country, website, org_type, 'New', '', '', draft, notes])
            
    print(f"Successfully processed {input_file} to {output_file}")
    
except Exception as e:
    print(f"Error: {e}")
