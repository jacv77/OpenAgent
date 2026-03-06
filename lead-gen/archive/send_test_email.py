#!/usr/bin/env python3
"""
Send a test email using AgentMail Python SDK
"""

import httpx
import json
from datetime import datetime

# Configuration
API_KEY = "am_us_ba71ac6140daeb3a04b3781992d0689b715a8c42c8ba19d8e833c6926f529bda"
INBOX = "noctil.agent@agentmail.to"
BASE_URL = "https://api.agentmail.to"

def send_test_email():
    """Send a test email via AgentMail API"""
    
    # URL encode the inbox address
    import urllib.parse
    inbox_encoded = urllib.parse.quote(INBOX, safe='')
    
    url = f"{BASE_URL}/v1/inboxes/{inbox_encoded}/messages"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    payload = {
        "to": ["noctil.agent@agentmail.to"],  # Sending to self for testing
        "subject": f"🧪 AgentMail Test - {timestamp}",
        "text": f"""Hello from OpenClaw Agent!

This is a test email sent at {timestamp} to verify AgentMail integration.

✓ AgentMail SDK: Installed
✓ API Key: Configured
✓ Inbox: {INBOX}
✓ Status: Working!

Your OpenClaw agent can now send and receive emails programmatically.

Best regards,
OpenClaw Agent
""",
        "html": f"""
<html>
<body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px;">
    <h1 style="color: #2563eb;">🧪 AgentMail Test</h1>
    <p><strong>Timestamp:</strong> {timestamp}</p>
    
    <div style="background-color: #f0f9ff; border-left: 4px solid #2563eb; padding: 15px; margin: 20px 0;">
        <h2 style="margin-top: 0; color: #1e40af;">Test Results</h2>
        <ul style="list-style: none; padding: 0;">
            <li>✓ AgentMail SDK: <strong>Installed</strong></li>
            <li>✓ API Key: <strong>Configured</strong></li>
            <li>✓ Inbox: <strong>{INBOX}</strong></li>
            <li>✓ Status: <strong>Working!</strong></li>
        </ul>
    </div>
    
    <p>Your OpenClaw agent can now send and receive emails programmatically.</p>
    
    <hr style="border: none; border-top: 1px solid #e5e7eb; margin: 30px 0;">
    
    <p style="color: #6b7280; font-size: 14px;">
        <strong>Best regards,</strong><br>
        OpenClaw Agent
    </p>
</body>
</html>
"""
    }
    
    print("=" * 60)
    print("Sending Test Email via AgentMail")
    print("=" * 60)
    print(f"From: {INBOX}")
    print(f"To: {INBOX} (self)")
    print(f"Subject: {payload['subject']}")
    print()
    
    try:
        response = httpx.post(url, json=payload, headers=headers, timeout=30.0)
        
        if response.status_code == 200:
            result = response.json()
            print("✓ Email sent successfully!")
            print(f"  Message ID: {result.get('message_id', 'N/A')}")
            print(f"  Thread ID: {result.get('thread_id', 'N/A')}")
            print()
            print("Check your inbox at: noctil.agent@agentmail.to")
            return True
        else:
            print(f"✗ Failed with status code: {response.status_code}")
            print(f"  Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"✗ Error sending email: {e}")
        return False

if __name__ == "__main__":
    success = send_test_email()
    print("=" * 60)
    exit(0 if success else 1)
