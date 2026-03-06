import os
from agentmail import AgentMail

# Use the provided API key directly as requested in the prompt
API_KEY = 'am_us_ba71ac6140daeb3a04b3781992d0689b715a8c42c8ba19d8e833c6926f529bda'
TARGET_EMAIL = 'noctil.agent@agentmail.to'

client = AgentMail(api_key=API_KEY)

leads = [
    {
        "company": "Kobalt Music Group",
        "website": "kobaltmusic.com",
        "industry": "Music Publishing / Rights Tech",
        "location": "New York / London",
        "size": "500-1000 employees",
        "contact_name": "Laurent Hubert",
        "contact_title": "CEO",
        "contact_email": "laurent.hubert@kobaltmusic.com", # Placeholder pattern
        "summary": "Kobalt is a leading independent music services company, offering music publishing, label services, and neighboring rights. They are known for their technology platform, AWAL (though sold to Sony, Kobalt remains tech-forward). Focus is on transparency and efficiency for artists.",
        "profile": "Laurent oversees global operations. As CEO, he is the key decision-maker for strategic tech partnerships and operational efficiency tools.",
        "value_prop": "Noctil.com can further streamline Kobalt's high-volume rights administration, offering next-gen tools for complex metadata matching and royalty processing to maintain their competitive edge in tech-driven publishing."
    },
    {
        "company": "Downtown Music Holdings",
        "website": "downtownmusic.com",
        "industry": "Music Publishing / Rights Management",
        "location": "New York, NY",
        "size": "200-500 employees",
        "contact_name": "Pieter van Rijn",
        "contact_title": "CEO",
        "contact_email": "pieter.vanrijn@downtownmusic.com",
        "summary": "Downtown manages millions of music copyrights. They focus on technology-driven rights management for businesses and creators. They acquired CD Baby and Songtrust.",
        "profile": "Pieter leads the company's strategic direction. He would be interested in scalable solutions that integrate across their diverse portfolio of services (publishing, distribution, monetization).",
        "value_prop": "Noctil.com's robust API-first approach to rights management aligns perfectly with Downtown's ecosystem, potentially consolidating disjointed workflows across their various acquisitions."
    },
    {
        "company": "Sentric Music Group",
        "website": "sentricmusic.com",
        "industry": "Independent Music Publishing",
        "location": "Liverpool, UK",
        "size": "50-200 employees",
        "contact_name": "Chris Meehan",
        "contact_title": "Founder & CEO",
        "contact_email": "chris.meehan@sentricmusic.com",
        "summary": "Sentric provides music publishing solutions for over 100,000 songwriters. They emphasize technology to simplify royalty collection globally.",
        "profile": "As Founder, Chris drives the vision of simplifying publishing. He values automation and global reach for independent artists.",
        "value_prop": "Noctil.com offers automated registration and tracking capabilities that could reduce manual overhead for Sentric's massive catalog of independent works, improving speed-to-payment for their writers."
    },
    {
        "company": "Songtradr",
        "website": "songtradr.com",
        "industry": "B2B Music Licensing Marketplace",
        "location": "Santa Monica, CA",
        "size": "200-500 employees",
        "contact_name": "Paul Wiltshire",
        "contact_title": "CEO",
        "contact_email": "paul.wiltshire@songtradr.com",
        "summary": "Songtradr is the world's largest B2B music licensing marketplace. They connect artists with brands, TV, and film. They also own Bandcamp (partially) and 7digital.",
        "profile": "Paul is focused on scaling the licensing ecosystem. He needs efficient ways to manage rights clearance and metadata for millions of tracks.",
        "value_prop": "Noctil.com can enhance Songtradr's licensing engine by ensuring pristine metadata accuracy and automated rights clearance verification, reducing friction in high-volume licensing deals."
    },
    {
        "company": "BMG Rights Management",
        "website": "bmg.com",
        "industry": "Music Publishing & Recordings",
        "location": "Berlin, Germany / Global",
        "size": "1000+ employees",
        "contact_name": "Thomas Coesfeld",
        "contact_title": "CEO",
        "contact_email": "thomas.coesfeld@bmg.com",
        "summary": "BMG represents a new model of music company, integrating publishing and recordings under one roof. They prioritize fairness and transparency.",
        "profile": "Thomas is the top executive, driving the company's modern approach. He would be interested in enterprise-grade solutions that unify their dual publishing/recording data streams.",
        "value_prop": "Noctil.com's unified rights platform can support BMG's integrated model, bridging the gap between master and composition rights management for more accurate and faster royalty distribution."
    },
    {
        "company": "PPL (Phonographic Performance Limited)",
        "website": "ppluk.com",
        "industry": "Collective Management Organization (CMO)",
        "location": "London, UK",
        "size": "200-500 employees",
        "contact_name": "Peter Leathem",
        "contact_title": "CEO",
        "contact_email": "peter.leathem@ppluk.com",
        "summary": "PPL licenses recorded music played in public and broadcast in the UK. They distribute royalties to performers and recording rightsholders.",
        "profile": "Peter leads the organization's strategic initiatives. CMOs are constantly under pressure to improve distribution accuracy and reduce operating costs.",
        "value_prop": "Noctil.com offers advanced matching algorithms that can help PPL identify unallocated usage data with higher precision, ensuring more money reaches the correct rightsholders."
    },
    {
        "company": "SoundExchange",
        "website": "soundexchange.com",
        "industry": "Performance Rights Organization (Digital)",
        "location": "Washington, DC",
        "size": "100-300 employees",
        "contact_name": "Michael Huppe",
        "contact_title": "President & CEO",
        "contact_email": "mhuppe@soundexchange.com",
        "summary": "SoundExchange collects and distributes digital performance royalties for sound recordings in the US (e.g., SiriusXM, Pandora, webcasters).",
        "profile": "Michael is a key figure in US music rights. He focuses on technology and advocacy to ensure fair pay for creators in the digital age.",
        "value_prop": "Noctil.com can partner with SoundExchange to provide supplementary data cleaning and conflict resolution tools, helping to resolve ownership disputes faster and release held royalties."
    },
    {
        "company": "Believe",
        "website": "believe.com",
        "industry": "Digital Music Distribution / Artist Services",
        "location": "Paris, France",
        "size": "1000+ employees",
        "contact_name": "Denis Ladegaillerie",
        "contact_title": "Founder & CEO",
        "contact_email": "denis.ladegaillerie@believe.com",
        "summary": "Believe helps independent artists and labels distribute and promote their music. They own TuneCore and have a strong presence in digital markets.",
        "profile": "Denis drives the company's global expansion and digital strategy. Efficiency in handling millions of micro-transactions is crucial.",
        "value_prop": "Noctil.com's scalable infrastructure is ideal for Believe's high-volume distribution model, offering automated royalty splitting and reporting that scales with their rapid catalog growth."
    },
    {
        "company": "Peermusic",
        "website": "peermusic.com",
        "industry": "Independent Music Publishing",
        "location": "Global / Los Angeles",
        "size": "200-500 employees",
        "contact_name": "Mary Megan Peer",
        "contact_title": "CEO",
        "contact_email": "mmpeer@peermusic.com",
        "summary": "Peermusic is one of the largest independent music publishers in the world, with a vast catalog of standards and contemporary hits.",
        "profile": "Mary Megan leads the family-owned business. She balances tradition with modern rights administration needs.",
        "value_prop": "Noctil.com can help Peermusic modernize legacy catalog management, digitizing and organizing decades of rights data for better monetization in the streaming era."
    },
    {
        "company": "Audiam",
        "website": "audiam.com",
        "industry": "Digital Rights Administration / Reproduction Rights",
        "location": "New York, NY",
        "size": "11-50 employees",
        "contact_name": "Jeff Price",
        "contact_title": "Founder (Consultant/Strategic)",
        "contact_email": "jeff@audiam.com",
        "summary": "Audiam (now part of SESAC) specializes in recovering mechanical royalties for songwriters from digital services like Spotify and YouTube.",
        "profile": "Jeff (or current leadership) focuses on finding unpaid royalties. Accuracy in matching composition data to sound recordings is their core business.",
        "value_prop": "Noctil.com's precision auditing tools can assist Audiam in identifying gaps in mechanical licensing payments, maximizing recovery rates for their publisher clients."
    }
]

print(f"Sending {len(leads)} emails...")

for lead in leads:
    subject = f"New Lead: {lead['company']} - {lead['contact_title']}"
    
    body = f"""
Company Details:
- Name: {lead['company']}
- Website: {lead['website']}
- Industry: {lead['industry']}
- Location: {lead['location']}
- Size: {lead['size']}

Contact Information:
- Name: {lead['contact_name']}
- Title: {lead['contact_title']}
- Email: {lead['contact_email']} (Note: Email pattern inferred, verify before outreach)
- LinkedIn: Search for "{lead['contact_name']} {lead['company']}"

Company Summary:
{lead['summary']}

Profile Summary:
{lead['profile']}

Noctil.com Value Proposition:
{lead['value_prop']}
"""
    
    try:
        # Using client.inboxes.messages.send for sending
        # Note: The prompt example uses 'to' parameter directly in send method
        # The library signature might be send(inbox_id, to, subject, text, html)
        # We'll use text for the plain text body.
        
        # Constructing the message payload based on typical usage or the prompt's example
        # The prompt implies: client.inboxes.messages.send(inbox_id=..., to=..., subject=..., text=..., html=...)
        
        response = client.inboxes.messages.send(
            inbox_id="noctil.agent@agentmail.to",
            to="noctil.agent@agentmail.to",
            subject=subject,
            text=body,
            html=body.replace("\n", "<br>") # Simple HTML conversion
        )
        print(f"Sent email for {lead['company']}")
        
    except Exception as e:
        print(f"Failed to send email for {lead['company']}: {str(e)}")

print("Done.")
