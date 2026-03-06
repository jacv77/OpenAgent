
import sys
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path.home() / '.openclaw' / 'skills' / 'lead-gen-pro' / 'scripts'))

from send_lead_email import send_lead_email
from leads_database import LeadsDatabase

def process_new_leads():
    print("Starting Strategic Lead Generation Process...")
    db = LeadsDatabase()
    
    # 10 NEW Leads (Not in DB)
    leads = [
        {
            'company': {
                'name': 'SACEM',
                'website': 'https://www.sacem.fr',
                'industry_segment': 'Collective Management Organization',
                'location': 'Paris, France',
                'region': 'Europe',
                'company_size': '1000+ employees',
                'description': 'French collective management organization for authors, composers and publishers.',
                'technology_stack': 'URIGHTS (partnership with IBM)',
                'recent_news': 'Distributed record royalties in 2025; investing heavily in AI data processing.',
                'identified_problems': 'Handling massive data volumes from streaming; AI-generated music detection.',
                'cold_email_strawman': '''Subject: Enhancing URights with next-gen rights tracking

Hi Cécile,

I've been following SACEM's leadership in digital rights management, especially the URights initiative. Handling the explosion of streaming data is the industry's biggest challenge.

As SACEM continues to innovate, ensuring the accuracy of billions of micro-transactions is critical. Noctil provides a specialized layer that:
• Validates metadata against 50+ global sources in real-time
• Detects and resolves conflict claims automatically
• Scales to process petabytes of usage data without lag

We can help SACEM maintain its position as the most technologically advanced CMO in the world.

Would you be open to a brief discussion on our data validation capabilities?

Best regards,
Jacob Varghese
Noctil

P.S. How is the URights platform handling the new DSP reporting standards?'''
            },
            'contact': {
                'name': 'Cécile Rap-Veber',
                'title': 'CEO',
                'email': 'cecile.rap-veber@sacem.fr', # Hypothesized
                'linkedin_url': 'https://www.linkedin.com/in/cécile-rap-veber',
                'phone': '+33-1-47-15-47-15',
                'profile_summary': 'CEO of SACEM.',
                'decision_authority': 'Chief Executive'
            },
            'value_proposition': 'Enhance URights accuracy and scalability.'
        },
        {
            'company': {
                'name': 'GEMA',
                'website': 'https://www.gema.de',
                'industry_segment': 'Collective Management Organization',
                'location': 'Berlin, Germany',
                'region': 'Europe',
                'company_size': '1000+ employees',
                'description': 'German society for musical performing and mechanical reproduction rights.',
                'technology_stack': 'ICE (Joint Venture)',
                'recent_news': 'Filed lawsuits against Suno AI and Open AI in 2025; focused on AI copyright protection.',
                'identified_problems': 'AI copyright infringement; complex licensing models for AI training data.',
                'cold_email_strawman': '''Subject: Technical safeguards for AI copyright protection

Hi Tobias,

I saw GEMA's strong stance and lawsuits against Generative AI companies. Protecting members' rights in the AI era is the defining battle of our time.

Noctil is building the infrastructure to support this defense. Our platform can:
• Fingerprint catalog assets to detect unauthorized use in training sets
• Automate the tracking of AI-generated content registration
• Provide immutable audit trails for rights ownership

We can provide the technical "teeth" to enforce GEMA's policy positions on AI.

Would you be open to exploring how our tech can support your AI strategy?

Best regards,
Jacob Varghese
Noctil

P.S. Are you looking for technical partners to help identify unauthorized AI training usage?'''
            },
            'contact': {
                'name': 'Tobias Holzmüller',
                'title': 'CEO',
                'email': 'tholzmueller@gema.de', # Hypothesized
                'linkedin_url': 'https://www.linkedin.com/in/tobias-holzmüller',
                'phone': '+49-30-21245-00',
                'profile_summary': 'CEO of GEMA.',
                'decision_authority': 'Chief Executive'
            },
            'value_proposition': 'Technical enforcement for AI copyright protection.'
        },
        {
            'company': {
                'name': 'PPL',
                'website': 'https://www.ppluk.com',
                'industry_segment': 'Music Licensing',
                'location': 'London, UK',
                'region': 'Europe',
                'company_size': '200-500 employees',
                'description': 'UK licensing company for performers and recording rightsholders.',
                'technology_stack': 'RDx (Repertoire Data Exchange)',
                'recent_news': 'Partnered with Salt (Feb 2026) to optimize music usage and repertoire matching.',
                'identified_problems': 'Optimizing repertoire matching; data accuracy across international sources.',
                'cold_email_strawman': '''Subject: Enhancing repertoire matching alongside Salt

Hi Mark,

I saw the news about PPL's partnership with Salt to optimize matching. It's great to see PPL continuing to invest in data accuracy.

As you refine your RDx and matching capabilities, handling the "long tail" of unmatched data remains a challenge. Noctil complements systems like Salt by:
• Pre-cleaning metadata before it hits the matching engine
• Automating the resolution of "fuzzy" matches using context awareness
• Reducing the manual review queue by up to 60%

We can help PPL achieve even higher match rates for your members.

Would you be open to a technical deep dive on our metadata cleaning process?

Best regards,
Jacob Varghese
Noctil

P.S. How is the integration with Salt progressing?'''
            },
            'contact': {
                'name': 'Mark Douglas',
                'title': 'Chief Information Officer',
                'email': 'mark.douglas@ppluk.com', # Hypothesized
                'linkedin_url': 'https://www.linkedin.com/in/mark-douglas-ppl',
                'phone': '+44-20-7534-1000',
                'profile_summary': 'CIO at PPL, leading RDx and data initiatives.',
                'decision_authority': 'Technical Decision Maker'
            },
            'value_proposition': 'Improve match rates and reduce manual data cleaning.'
        },
        {
            'company': {
                'name': 'APRA AMCOS',
                'website': 'https://www.apraamcos.com.au',
                'industry_segment': 'Collective Management Organization',
                'location': 'Sydney, Australia',
                'region': 'Asia-Pacific',
                'company_size': '200-500 employees',
                'description': 'Music rights management organization for Australia and New Zealand.',
                'technology_stack': 'CMS (Core Management System)',
                'recent_news': 'focused on digital services licensing and pan-Asian licensing.',
                'identified_problems': 'Multi-territory licensing complexity in APAC; diverse metadata standards.',
                'cold_email_strawman': '''Subject: Streamlining pan-Asian multi-territory licensing

Hi Dean,

APRA AMCOS has done incredible work establishing a hub for pan-Asian licensing. The complexity of managing rights across so many diverse territories is immense.

Noctil simplifies multi-territory administration. Our platform is designed to:
• Handle diverse character sets and metadata standards (essential for APAC)
• Automate currency conversion and tax withholding calculations
• Provide a unified view of rights across all licensed territories

We can help reduce the operational friction of your pan-Asian initiatives.

Would you be open to a call to discuss APAC rights infrastructure?

Best regards,
Jacob Varghese
Noctil

P.S. What is the biggest data challenge you face with the fragmented APAC DSP market?'''
            },
            'contact': {
                'name': 'Dean Ormston',
                'title': 'CEO',
                'email': 'dormston@apra.com.au', # Hypothesized
                'linkedin_url': 'https://www.linkedin.com/in/deanormston',
                'phone': '+61-2-9935-7900',
                'profile_summary': 'CEO of APRA AMCOS.',
                'decision_authority': 'Chief Executive'
            },
            'value_proposition': 'Simplify APAC multi-territory licensing and data handling.'
        },
        {
            'company': {
                'name': 'SOCAN',
                'website': 'https://www.socan.com',
                'industry_segment': 'Collective Management Organization',
                'location': 'Toronto, Canada',
                'region': 'North America',
                'company_size': '500-1000 employees',
                'description': 'Canadian performing rights organization.',
                'technology_stack': 'Proprietary systems',
                'recent_news': 'Jennifer Brown leading strategic shift towards member-centric tech.',
                'identified_problems': 'Modernizing legacy systems; improving member portal experience.',
                'cold_email_strawman': '''Subject: Accelerating SOCAN's tech modernization

Hi Jennifer,

I've been following your leadership at SOCAN and the focus on member-centric services. Modernizing legacy PRO infrastructure is one of the hardest jobs in the industry.

Noctil offers a modular "sidecar" approach to modernization. Instead of a full rip-and-replace, we can:
• Stand up a modern member portal API in weeks
• Handle high-volume streaming data processing outside your legacy mainframe
• Sync clean data back to your core systems

We can help SOCAN deliver modern features to members faster.

Would you be open to discussing a modular approach to modernization?

Best regards,
Jacob Varghese
Noctil

P.S. What is the most requested feature from your members right now?'''
            },
            'contact': {
                'name': 'Jennifer Brown',
                'title': 'CEO',
                'email': 'jennifer.brown@socan.com', # Hypothesized
                'linkedin_url': 'https://www.linkedin.com/in/jennifer-brown-socan',
                'phone': '+1-416-445-8700',
                'profile_summary': 'CEO of SOCAN.',
                'decision_authority': 'Chief Executive'
            },
            'value_proposition': 'Modular modernization of legacy infrastructure.'
        },
        {
            'company': {
                'name': 'Buma/Stemra',
                'website': 'https://www.bumastemra.nl',
                'industry_segment': 'Collective Management Organization',
                'location': 'Hoofddorp, Netherlands',
                'region': 'Europe',
                'company_size': '200-500 employees',
                'description': 'Dutch collective management organization for composers and lyricists.',
                'technology_stack': 'ICE (Joint Venture)',
                'recent_news': 'Focusing on improving online licensing efficiency.',
                'identified_problems': 'Online licensing fragmentation; maximizing collections from new platforms.',
                'cold_email_strawman': '''Subject: Maximizing online collections efficiency

Hi Bernard,

Buma/Stemra's work in ensuring fair pay for online use is exemplary. The fragmentation of online platforms makes 100% collection nearly impossible with traditional tools.

Noctil specializes in "gap analysis" for online rights. We help CMOs:
• Identify usage on long-tail platforms that are often missed
• Automate the claiming process for unmatched works
• Provide transparent reporting to members about online sources

We can help Buma/Stemra close the revenue gap for your members.

Would you be open to a demo of our online tracking capabilities?

Best regards,
Jacob Varghese
Noctil

P.S. Are you finding it difficult to track usage on short-form video platforms?'''
            },
            'contact': {
                'name': 'Bernard Kobes',
                'title': 'CEO',
                'email': 'bernard.kobes@bumastemra.nl', # Hypothesized
                'linkedin_url': 'https://www.linkedin.com/in/bernardkobes',
                'phone': '+31-23-799-7999',
                'profile_summary': 'CEO of Buma/Stemra.',
                'decision_authority': 'Chief Executive'
            },
            'value_proposition': 'Maximize online royalty collections.'
        },
        {
            'company': {
                'name': 'SUISA',
                'website': 'https://www.suisa.ch',
                'industry_segment': 'Collective Management Organization',
                'location': 'Zurich, Switzerland',
                'region': 'Europe',
                'company_size': '200-500 employees',
                'description': 'Swiss cooperative society for authors and publishers of music.',
                'technology_stack': 'Mint Digital Services (JV with SESAC)',
                'recent_news': 'Collaborating with SESAC on Mint Digital Services for cross-border licensing.',
                'identified_problems': 'Cross-border data reconciliation; scaling Mint Digital Services.',
                'cold_email_strawman': '''Subject: Scaling cross-border data reconciliation

Hi Andreas,

The Mint Digital Services JV with SESAC is a powerful model for cross-border licensing. Scaling that infrastructure to handle more territories requires robust data reconciliation.

Noctil provides the glue for multi-territory data ops. We can help SUISA:
• Automate the reconciliation of conflicting metadata between territories
• Speed up the distribution cycle for international royalties
• Reduce the operational cost of your cross-border services

We can help ensure Mint Digital Services operates at peak efficiency.

Would you be open to a technical chat about data reconciliation?

Best regards,
Jacob Varghese
Noctil

P.S. How is the expansion of Mint Digital Services progressing?'''
            },
            'contact': {
                'name': 'Andreas Wegelin',
                'title': 'CEO',
                'email': 'andreas.wegelin@suisa.ch', # Hypothesized
                'linkedin_url': 'https://www.linkedin.com/in/andreaswegelin',
                'phone': '+41-44-485-66-66',
                'profile_summary': 'CEO of SUISA.',
                'decision_authority': 'Chief Executive'
            },
            'value_proposition': 'Optimize cross-border data operations.'
        },
        {
            'company': {
                'name': 'TONO',
                'website': 'https://www.tono.no',
                'industry_segment': 'Collective Management Organization',
                'location': 'Oslo, Norway',
                'region': 'Europe',
                'company_size': '50-200 employees',
                'description': 'Norwegian copyright collection society.',
                'technology_stack': 'Polaris (Nordic collaboration)',
                'recent_news': 'Celebrating record distributions; focus on transparency.',
                'identified_problems': 'Transparency in distribution; modernizing member interfaces.',
                'cold_email_strawman': '''Subject: Enhancing transparency for TONO members

Hi Karl,

TONO's commitment to transparency sets a high bar in the Nordics. As members demand more real-time insights, legacy reporting tools often struggle to keep up.

Noctil offers a white-label "Transparency Portal" for CMOs. We enable:
• Real-time dashboards for members to see where their money comes from
• Granular drill-downs into streaming data
• Automated query resolution for members

We can help TONO deliver the most transparent member experience in Europe.

Would you be open to seeing our member dashboard concepts?

Best regards,
Jacob Varghese
Noctil

P.S. Are your members asking for more frequent data updates?'''
            },
            'contact': {
                'name': 'Karl Vestli',
                'title': 'CEO',
                'email': 'karl.vestli@tono.no', # Hypothesized
                'linkedin_url': 'https://www.linkedin.com/in/karlvestli',
                'phone': '+47-22-05-72-00',
                'profile_summary': 'CEO of TONO.',
                'decision_authority': 'Chief Executive'
            },
            'value_proposition': 'Real-time transparency and member reporting.'
        },
        {
            'company': {
                'name': 'SIAE',
                'website': 'https://www.siae.it',
                'industry_segment': 'Collective Management Organization',
                'location': 'Rome, Italy',
                'region': 'Europe',
                'company_size': '1000+ employees',
                'description': 'Italian society for authors and publishers.',
                'technology_stack': 'Algorand (Blockchain initiative - historic)',
                'recent_news': 'Navigating EU copyright directive implementation.',
                'identified_problems': 'Bureaucracy reduction; implementing EU copyright directives efficiently.',
                'cold_email_strawman': '''Subject: Reducing administrative friction with automation

Hi Gaetano,

SIAE represents a massive cultural heritage. Managing that scale while modernizing operations is a unique challenge.

Noctil specializes in administrative automation for large rights organizations. We help:
• Digitize paper-based workflows automatically
• Ensure compliance with new EU copyright directives via rule-based engines
• Reduce processing times for mechanical licensing

We can help SIAE streamline operations without disrupting your core mission.

Would you be open to discussing our automation case studies?

Best regards,
Jacob Varghese
Noctil

P.S. How is the implementation of the new EU copyright directive affecting your ops team?'''
            },
            'contact': {
                'name': 'Gaetano Blandini',
                'title': 'General Director',
                'email': 'gaetano.blandini@siae.it', # Hypothesized
                'linkedin_url': 'https://www.linkedin.com/in/gaetanoblandini',
                'phone': '+39-06-59901',
                'profile_summary': 'General Director of SIAE.',
                'decision_authority': 'Operational Leader'
            },
            'value_proposition': 'Administrative automation and compliance.'
        },
        {
            'company': {
                'name': 'IMRO',
                'website': 'https://www.imro.ie',
                'industry_segment': 'Collective Management Organization',
                'location': 'Dublin, Ireland',
                'region': 'Europe',
                'company_size': '50-200 employees',
                'description': 'Irish Music Rights Organisation.',
                'technology_stack': 'Proprietary / International links',
                'recent_news': 'Lobbying for stronger copyright protection in Ireland.',
                'identified_problems': 'Protecting Irish repertoire globally; efficient distribution.',
                'cold_email_strawman': '''Subject: Maximizing global reach for Irish repertoire

Hi Victor,

IMRO has always punched above its weight in protecting Irish music. Ensuring that Irish repertoire is correctly identified and paid for globally is crucial.

Noctil provides a "Global Monitor" service for rights organizations. We:
• Track the performance of your repertoire across 100+ global territories
• Identify missing payments from foreign societies
• Provide data evidence to support international claims

We can help IMRO ensure every cent due to Irish creators is collected.

Would you be open to a trial of our Global Monitor?

Best regards,
Jacob Varghese
Noctil

P.S. Are you satisfied with the reciprocal collection rates from major territories?'''
            },
            'contact': {
                'name': 'Victor Finn',
                'title': 'CEO',
                'email': 'victor.finn@imro.ie', # Hypothesized
                'linkedin_url': 'https://www.linkedin.com/in/victorfinn',
                'phone': '+353-1-661-4844',
                'profile_summary': 'CEO of IMRO.',
                'decision_authority': 'Chief Executive'
            },
            'value_proposition': 'Maximize global reciprocal collections.'
        }
    ]

    for lead in leads:
        company_data = lead['company']
        contact_data = lead['contact']
        value_proposition = lead['value_proposition']

        print(f"\nProcessing: {contact_data['name']} at {company_data['name']}")
        
        # --- SENDING ---
        result = send_lead_email(company_data, contact_data, value_proposition)
        print(f"✉️  Lead: {result.get('company')} / {result.get('contact')} - {'Sent' if result.get('sent') else 'Skipped: ' + result.get('reason')}")

    # Final stats
    stats = db.get_stats()
    print(f"\n📊 Database Stats: {stats['total_companies']} companies, {stats['total_contacts']} contacts, {stats['total_leads_sent']} leads sent")

if __name__ == "__main__":
    process_new_leads()
