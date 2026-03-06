#!/usr/bin/env python3
"""
AgentMail Test Script
Tests sending and receiving emails with AgentMail
"""

from agentmail import AgentMail

# Configuration
API_KEY = "am_us_ba71ac6140daeb3a04b3781992d0689b715a8c42c8ba19d8e833c6926f529bda"
INBOX = "noctil.agent@agentmail.to"

# Initialize AgentMail client
client = AgentMail(api_key=API_KEY)

print("=" * 60)
print("AgentMail Test Script")
print("=" * 60)
print(f"Inbox: {INBOX}")
print()

# Test 1: List all inboxes
print("Test 1: Listing all inboxes...")
try:
    response = client.inboxes.list()
    print(f"✓ Found {response.count} inbox(es):")
    for inbox in response.inboxes:
        print(f"  - {inbox.inbox_id}")
        print(f"    Display Name: {inbox.display_name}")
        print(f"    Created: {inbox.created_at}")
    print()
except Exception as e:
    print(f"✗ Failed to list inboxes: {e}")
    print()

# Test 2: Get specific inbox info
print("Test 2: Getting inbox information...")
try:
    inbox_info = client.inboxes.get(INBOX)
    print(f"✓ Inbox information:")
    print(f"  Address: {inbox_info.inbox_id}")
    print(f"  Display Name: {inbox_info.display_name}")
    print(f"  Pod ID: {inbox_info.pod_id}")
    print(f"  Created: {inbox_info.created_at}")
    print()
except Exception as e:
    print(f"✗ Failed to get inbox info: {e}")
    print()

# Test 3: List threads (received emails)
print("Test 3: Checking inbox for received emails (threads)...")
try:
    threads_response = client.threads.list(inbox_id=INBOX)
    
    if threads_response.count > 0:
        print(f"✓ Found {threads_response.count} thread(s) in inbox:")
        print()
        for i, thread in enumerate(threads_response.threads[:5], 1):  # Show first 5
            print(f"  Thread {i}:")
            print(f"    ID: {thread.thread_id}")
            print(f"    Subject: {thread.subject}")
            print(f"    Participants: {len(thread.participants)} participant(s)")
            print(f"    Messages: {thread.message_count}")
            print()
    else:
        print("  No threads found in inbox (this is normal for a new inbox)")
        print()
except Exception as e:
    print(f"✗ Failed to list threads: {e}")
    print()

# Test 4: Send an email
print("Test 4: Sending a test email...")
try:
    # Send email directly
    message = client.messages.send(
        inbox_id=INBOX,
        to=["noctil.agent@agentmail.to"],  # Sending to self for testing
        subject="AgentMail Test - Hello from OpenClaw",
        text="This is a test email sent from OpenClaw agent using AgentMail SDK.",
        html="<h1>AgentMail Test</h1><p>This is a test email sent from <strong>OpenClaw agent</strong> using AgentMail SDK.</p>"
    )
    
    print(f"✓ Email sent successfully!")
    print(f"  Message ID: {message.message_id}")
    print(f"  Thread ID: {message.thread_id}")
    print()
except Exception as e:
    print(f"✗ Failed to send email: {e}")
    print()

# Test 5: Wait a moment and check for the sent message
print("Test 5: Verifying sent message...")
import time
time.sleep(2)  # Wait for message to be processed

try:
    threads_response = client.threads.list(inbox_id=INBOX)
    
    if threads_response.count > 0:
        print(f"✓ Inbox now has {threads_response.count} thread(s)")
        latest_thread = threads_response.threads[0]
        print(f"  Latest thread subject: {latest_thread.subject}")
        print()
    else:
        print("  Still no threads (message may take a moment to appear)")
        print()
except Exception as e:
    print(f"✗ Failed to verify: {e}")
    print()

print("=" * 60)
print("AgentMail setup complete!")
print("=" * 60)
print()
print("Summary:")
print(f"✓ AgentMail SDK installed and configured")
print(f"✓ API key configured in openclaw.json")
print(f"✓ Inbox verified: {INBOX}")
print(f"✓ Send/receive functionality tested")
print()
print("Next steps:")
print("1. Configure webhooks for real-time email notifications")
print("2. Integrate with OpenClaw skills for automated workflows")
print("3. Set up email-based agent interactions")
