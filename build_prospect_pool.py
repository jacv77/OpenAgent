import sqlite3
import sys
import re
from pathlib import Path

# Add the leads_database module to path
sys.path.insert(0, str(Path.home() / '.openclaw' / 'skills' / 'lead-gen-pro' / 'scripts'))
from leads_database import LeadsDatabase

def clean_name(name):
    # Remove wiki annotations and extra whitespace
    name = re.sub(r'\[.*?\]', '', name)
    name = re.sub(r'\(.*?\)', '', name)
    return name.strip()

def infer_website(name, segment):
    # Simple heuristic to generate a likely website
    clean = name.lower().replace(' ', '').replace('.', '').replace(',', '').replace('&', 'and')
    if segment == "Collective Management Organization":
        return f"https://www.{clean}.org"
    return f"https://www.{clean}.com"

def main():
    db = LeadsDatabase()
    
    print("🚀 Starting Prospect Pool Builder...")
    
    # 1. Get current status
    stats = db.get_prospect_pool_stats()
    print(f"Current pool size: {stats['total']}")
    
    existing_websites = set(db.get_all_company_websites())
    print(f"Existing contacts: {len(existing_websites)}")
    
    # 2. Define the raw data (extracted from research)
    # Format: (Name, Segment, Country, Source, Priority)
    
    # CISAC / CMOs (Tier 1)
    cisac_data = [
        ("JASRAC", "Collective Management Organization", "Japan", "CISAC", 95),
        ("GEMA", "Collective Management Organization", "Germany", "CISAC", 95),
        ("PRS for Music", "Collective Management Organization", "UK", "CISAC", 95),
        ("SACEM", "Collective Management Organization", "France", "CISAC", 95),
        ("ASCAP", "Collective Management Organization", "USA", "CISAC", 95),
        ("BMI", "Collective Management Organization", "USA", "CISAC", 95),
        ("SOCAN", "Collective Management Organization", "Canada", "CISAC", 90),
        ("SESAC", "Collective Management Organization", "USA", "CISAC", 90),
        ("SIAE", "Collective Management Organization", "Italy", "CISAC", 90),
        ("Buma/Stemra", "Collective Management Organization", "Netherlands", "CISAC", 90),
        ("APRA AMCOS", "Collective Management Organization", "Australia", "CISAC", 90),
        ("SABAM", "Collective Management Organization", "Belgium", "CISAC", 85),
        ("STIM", "Collective Management Organization", "Sweden", "CISAC", 85),
        ("KODA", "Collective Management Organization", "Denmark", "CISAC", 85),
        ("TEOSTO", "Collective Management Organization", "Finland", "CISAC", 85),
        ("TONO", "Collective Management Organization", "Norway", "CISAC", 85),
        ("IMRO", "Collective Management Organization", "Ireland", "CISAC", 85),
        ("SUISA", "Collective Management Organization", "Switzerland", "CISAC", 85),
        ("AKM", "Collective Management Organization", "Austria", "CISAC", 85),
        ("SGAE", "Collective Management Organization", "Spain", "CISAC", 85),
        ("SPA", "Collective Management Organization", "Portugal", "CISAC", 80),
        ("ZAIKS", "Collective Management Organization", "Poland", "CISAC", 80),
        ("OSA", "Collective Management Organization", "Czech Republic", "CISAC", 80),
        ("ARTISJUS", "Collective Management Organization", "Hungary", "CISAC", 80),
        ("HDS", "Collective Management Organization", "Croatia", "CISAC", 75),
        ("SOZA", "Collective Management Organization", "Slovakia", "CISAC", 75),
        ("AKKA/LAA", "Collective Management Organization", "Latvia", "CISAC", 75),
        ("EAU", "Collective Management Organization", "Estonia", "CISAC", 75),
        ("LATGA", "Collective Management Organization", "Lithuania", "CISAC", 75),
        ("SADAIC", "Collective Management Organization", "Argentina", "CISAC", 80),
        ("UBC", "Collective Management Organization", "Brazil", "CISAC", 80),
        ("ECAD", "Collective Management Organization", "Brazil", "CISAC", 80),
        ("SCD", "Collective Management Organization", "Chile", "CISAC", 75),
        ("SAYCO", "Collective Management Organization", "Colombia", "CISAC", 75),
        ("SACM", "Collective Management Organization", "Mexico", "CISAC", 80),
        ("KOMCA", "Collective Management Organization", "South Korea", "CISAC", 85),
        ("MCSC", "Collective Management Organization", "China", "CISAC", 85),
        ("CASH", "Collective Management Organization", "Hong Kong", "CISAC", 80),
        ("MUST", "Collective Management Organization", "Taiwan", "CISAC", 80),
        ("MACP", "Collective Management Organization", "Malaysia", "CISAC", 75),
        ("FILSCAP", "Collective Management Organization", "Philippines", "CISAC", 75),
        ("MCT", "Collective Management Organization", "Thailand", "CISAC", 75),
        ("VCPMC", "Collective Management Organization", "Vietnam", "CISAC", 75),
        ("IPRS", "Collective Management Organization", "India", "CISAC", 80),
        ("SAMRO", "Collective Management Organization", "South Africa", "CISAC", 75),
        ("MCSK", "Collective Management Organization", "Kenya", "CISAC", 70),
        ("GHAMRO", "Collective Management Organization", "Ghana", "CISAC", 70),
        ("COSON", "Collective Management Organization", "Nigeria", "CISAC", 70),
        ("BMDA", "Collective Management Organization", "Morocco", "CISAC", 70),
        ("ONDA", "Collective Management Organization", "Algeria", "CISAC", 70)
    ]

    # IMPALA / Indie Labels (Tier 1) - Sample from the UK list
    impala_data = [
        ("4AD", "Independent Record Label", "UK", "IMPALA", 85),
        ("XL Recordings", "Independent Record Label", "UK", "IMPALA", 90),
        ("Beggars Banquet", "Independent Record Label", "UK", "IMPALA", 85),
        ("Domino Recording Company", "Independent Record Label", "UK", "IMPALA", 85),
        ("Rough Trade", "Independent Record Label", "UK", "IMPALA", 85),
        ("Ninja Tune", "Independent Record Label", "UK", "IMPALA", 85),
        ("Warp Records", "Independent Record Label", "UK", "IMPALA", 85),
        ("Mute Records", "Independent Record Label", "UK", "IMPALA", 85),
        ("Cooking Vinyl", "Independent Record Label", "UK", "IMPALA", 80),
        ("Cherry Red", "Independent Record Label", "UK", "IMPALA", 80),
        ("Bella Union", "Independent Record Label", "UK", "IMPALA", 80),
        ("Heavenly Recordings", "Independent Record Label", "UK", "IMPALA", 80),
        ("Hospital Records", "Independent Record Label", "UK", "IMPALA", 80),
        ("Dirty Hit", "Independent Record Label", "UK", "IMPALA", 85),
        ("Transgressive Records", "Independent Record Label", "UK", "IMPALA", 75),
        ("Hyperdub", "Independent Record Label", "UK", "IMPALA", 75),
        ("Erased Tapes", "Independent Record Label", "UK", "IMPALA", 75),
        ("Brownswood Recordings", "Independent Record Label", "UK", "IMPALA", 75),
        ("Peaceville Records", "Independent Record Label", "UK", "IMPALA", 70),
        ("Earache Records", "Independent Record Label", "UK", "IMPALA", 75),
        ("Nuclear Blast", "Independent Record Label", "Germany", "IMPALA", 85),
        ("PIAS", "Independent Record Label", "Belgium", "IMPALA", 85),
        ("Edel", "Independent Record Label", "Germany", "IMPALA", 80),
        ("Wagram Music", "Independent Record Label", "France", "IMPALA", 80),
        ("Believe Digital", "Independent Record Label", "France", "IMPALA", 90),
        ("Because Music", "Independent Record Label", "France", "IMPALA", 85),
        ("Naïve", "Independent Record Label", "France", "IMPALA", 80),
        ("Play It Again Sam", "Independent Record Label", "Belgium", "IMPALA", 80),
        ("Epitaph Europe", "Independent Record Label", "Netherlands", "IMPALA", 80),
        ("Mascot Label Group", "Independent Record Label", "Netherlands", "IMPALA", 75),
        ("Armada Music", "Independent Record Label", "Netherlands", "IMPALA", 85),
        ("Spinnin Records", "Independent Record Label", "Netherlands", "IMPALA", 90),
        ("Kontor Records", "Independent Record Label", "Germany", "IMPALA", 80),
        ("Embassy of Music", "Independent Record Label", "Germany", "IMPALA", 75),
        ("Motor Music", "Independent Record Label", "Germany", "IMPALA", 75),
        ("Grönland Records", "Independent Record Label", "Germany", "IMPALA", 70),
        ("City Slang", "Independent Record Label", "Germany", "IMPALA", 75),
        ("Morr Music", "Independent Record Label", "Germany", "IMPALA", 70),
        ("K7 Records", "Independent Record Label", "Germany", "IMPALA", 75),
        ("BPitch Control", "Independent Record Label", "Germany", "IMPALA", 70),
        ("Monkeytown Records", "Independent Record Label", "Germany", "IMPALA", 70),
        ("Raster-Noton", "Independent Record Label", "Germany", "IMPALA", 70),
        ("Kompakt", "Independent Record Label", "Germany", "IMPALA", 80),
        ("Get Physical", "Independent Record Label", "Germany", "IMPALA", 75),
        ("Mobilee", "Independent Record Label", "Germany", "IMPALA", 70),
        ("Innervisions", "Independent Record Label", "Germany", "IMPALA", 75),
        ("Diynamic", "Independent Record Label", "Germany", "IMPALA", 75),
        ("Cocoon Recordings", "Independent Record Label", "Germany", "IMPALA", 75),
        ("Tresor Records", "Independent Record Label", "Germany", "IMPALA", 75),
        ("Ostgut Ton", "Independent Record Label", "Germany", "IMPALA", 75)
    ]

    # Music Tech / DDEX (Tier 1) - Common members
    ddex_data = [
        ("Spotify", "Music Technology", "Sweden", "DDEX", 95),
        ("Apple Music", "Music Technology", "USA", "DDEX", 95),
        ("Amazon Music", "Music Technology", "USA", "DDEX", 95),
        ("YouTube Music", "Music Technology", "USA", "DDEX", 95),
        ("Deezer", "Music Technology", "France", "DDEX", 90),
        ("Pandora", "Music Technology", "USA", "DDEX", 90),
        ("SoundCloud", "Music Technology", "Germany", "DDEX", 90),
        ("Tidal", "Music Technology", "USA", "DDEX", 85),
        ("Qobuz", "Music Technology", "France", "DDEX", 80),
        ("Napster", "Music Technology", "USA", "DDEX", 80),
        ("7digital", "Music Technology", "UK", "DDEX", 80),
        ("Orchard", "Music Technology", "USA", "DDEX", 90),
        ("Believe", "Music Technology", "France", "DDEX", 90),
        ("FUGA", "Music Technology", "Netherlands", "DDEX", 85),
        ("Ingrooves", "Music Technology", "USA", "DDEX", 85),
        ("DistroKid", "Music Technology", "USA", "DDEX", 85),
        ("TuneCore", "Music Technology", "USA", "DDEX", 85),
        ("CD Baby", "Music Technology", "USA", "DDEX", 85),
        ("Ditto Music", "Music Technology", "UK", "DDEX", 80),
        ("Amuse", "Music Technology", "Sweden", "DDEX", 80),
        ("Stem", "Music Technology", "USA", "DDEX", 80),
        ("AWAL", "Music Technology", "UK", "DDEX", 85),
        ("Kobalt", "Music Technology", "USA", "DDEX", 90),
        ("BMG", "Music Technology", "Germany", "DDEX", 90),
        ("Downtown", "Music Technology", "USA", "DDEX", 85),
        ("Songtrust", "Music Technology", "USA", "DDEX", 85),
        ("Sentric", "Music Technology", "UK", "DDEX", 80),
        ("Audiam", "Music Technology", "USA", "DDEX", 75),
        ("Music Reports", "Music Technology", "USA", "DDEX", 80),
        ("HFA", "Music Technology", "USA", "DDEX", 85)
    ]

    all_leads = cisac_data + impala_data + ddex_data
    
    # 3. Process and add to DB
    print(f"\nProcessing {len(all_leads)} potential prospects...")
    
    added_count = 0
    skipped_dup = 0
    
    for name, segment, country, source, priority in all_leads:
        website = infer_website(name, segment)
        
        # Check against existing contacted
        if website in existing_websites:
            skipped_dup += 1
            continue
            
        success = db.add_to_prospect_pool(
            company_name=name,
            website=website,
            industry_segment=segment,
            region="Global",  # Simplified
            country=country,
            source_org=source,
            company_size="Medium", # Default
            notes=f"Added via auto-research from {source} member list",
            priority_score=priority
        )
        
        if success:
            added_count += 1
            print(f"  [+] Added: {name} ({country}) - {source}")
        else:
            skipped_dup += 1
            # print(f"  [!] Skipped (duplicate): {name}")

    print(f"\nRun complete!")
    print(f"Added: {added_count}")
    print(f"Skipped: {skipped_dup}")

    # 4. Final Stats
    final_stats = db.get_prospect_pool_stats()
    print(f"\n📊 PROSPECT POOL BUILDING SUMMARY")
    print(f"\nProspect Pool Status:")
    print(f"  Total prospects: {final_stats['total']}")
    print(f"  Pending (available): {final_stats['pending']}")
    print(f"  Companies added this run: {added_count}")
    print(f"\nBy Source Organization:")
    for source, count in sorted(final_stats['by_source'].items(), key=lambda x: -x[1]):
        print(f"  {source}: {count}")
    print(f"\nBy Industry Segment:")
    for segment, count in sorted(final_stats['by_segment'].items(), key=lambda x: -x[1]):
        print(f"  {segment}: {count}")
    
    print("\nProspect pool ready for daily lead generation!")

if __name__ == "__main__":
    main()
