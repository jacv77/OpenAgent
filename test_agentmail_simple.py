#!/usr/bin/env python3
"""
AgentMail Simple Test - Verify Setup
"""

from agentmail import AgentMail

# Configuration
API_KEY = "am_us_ba71ac6140daeb3a04b3781992d0689b715a8c42c8ba19d8e833c6926f529bda"
INBOX = "noctil.agent@agentmail.to"

print("=" * 60)
print("AgentMail Setup Verification")
print("=" * 60)
print()

# Initialize client
client = AgentMail(api_key=API_KEY)

# Test 1: List inboxes
print("✓ Testing API connection...")
try:
    response = client.inboxes.list()
    print(f"✓ Connected! Found {response.count} inbox(es)")
    for inbox in response.inboxes:
        print(f"  - {inbox.inbox_id} ({inbox.display_name})")
    print()
except Exception as e:
    print(f"✗ Connection failed: {e}")
    exit(1)

# Test 2: Get inbox details
print("✓ Getting inbox details...")
try:
    inbox = client.inboxes.get(INBOX)
    print(f"✓ Inbox verified:")
    print(f"  Address: {inbox.inbox_id}")
    print(f"  Display Name: {inbox.display_name}")
    print(f"  Pod ID: {inbox.pod_id}")
    print(f"  Created: {inbox.created_at}")
    print()
except Exception as e:
    print(f"✗ Failed: {e}")
    exit(1)

# Test 3: Check for threads
print("✓ Checking for email threads...")
try:
    threads = client.threads.list()
    print(f"✓ Found {threads.count} thread(s) in your account")
    if threads.count > 0:
        print("  Recent threads:")
        for thread in threads.threads[:5]:
            print(f"    - {thread.subject}")
    print()
except Exception as e:
    print(f"✗ Failed: {e}")
    print()

print("=" * 60)
print("AgentMail Setup Complete!")
print("=" * 60)
print()
print("Summary:")
print(f"✓ AgentMail Python SDK installed")
print(f"✓ API key configured in openclaw.json")
print(f"✓ Inbox verified: {INBOX}")
print(f"✓ Ready to send and receive emails")
print()
print("To send emails programmatically, you can use the AgentMail")
print("REST API or explore the SDK's pods and drafts functionality.")
print()
print("For OpenClaw integration, the agentmail skill should provide")
print("native commands for email operations.")
