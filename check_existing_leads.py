
import sys
from pathlib import Path

# Add the scripts directory to sys.path so we can import LeadsDatabase
sys.path.insert(0, str(Path.home() / '.openclaw' / 'skills' / 'lead-gen-pro' / 'scripts'))

from leads_database import LeadsDatabase

def main():
    try:
        db = LeadsDatabase()
        existing_companies = db.get_all_company_websites()
        print(f"DEBUG_EXISTING_COMPANIES_COUNT:{len(existing_companies)}")
        for company in existing_companies:
            print(f"EXISTING_COMPANY:{company}")
    except Exception as e:
        print(f"Error accessing database: {e}")

if __name__ == "__main__":
    main()
