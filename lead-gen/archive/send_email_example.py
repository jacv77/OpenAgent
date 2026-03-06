#!/usr/bin/env python3
"""
AgentMail - Send Email Example using REST API
"""

import httpx

# Configuration
API_KEY = "am_us_ba71ac6140daeb3a04b3781992d0689b715a8c42c8ba19d8e833c6926f529bda"
INBOX = "noctil.agent@agentmail.to"
POD_ID = "496ae11e-52c2-49c7-bf32-252856e0d799"

# AgentMail API endpoint
BASE_URL = "https://api.agentmail.to"

def send_email(to_address, subject, body_text, body_html=None):
    """Send an email using AgentMail REST API"""
    
    # URL encode the inbox address
    import urllib.parse
    inbox_encoded = urllib.parse.quote(INBOX, safe='')
    
    # Correct endpoint: /v1/inboxes/{inbox_id}/messages
    url = f"{BASE_URL}/v1/inboxes/{inbox_encoded}/messages"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "to": [to_address] if isinstance(to_address, str) else to_address,
        "subject": subject,
        "text": body_text
    }
    
    if body_html:
        payload["html"] = body_html
    
    try:
        response = httpx.post(url, json=payload, headers=headers, timeout=30.0)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        print(f"HTTP Error: {e.response.status_code}")
        print(f"Response: {e.response.text}")
        raise
    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == "__main__":
    print("=" * 60)
    print("AgentMail - Send Email Example")
    print("=" * 60)
    print()
    
    # Example: Send a test email
    print("Sending test email...")
    try:
        result = send_email(
            to_address="noctil.agent@agentmail.to",  # Sending to self
            subject="Test Email from OpenClaw Agent",
            body_text="This is a test email sent via AgentMail REST API from OpenClaw.",
            body_html="<h1>Test Email</h1><p>This is a test email sent via <strong>AgentMail REST API</strong> from OpenClaw.</p>"
        )
        
        print("✓ Email sent successfully!")
        print(f"  Message ID: {result.get('message_id', 'N/A')}")
        print(f"  Thread ID: {result.get('thread_id', 'N/A')}")
        print()
    except Exception as e:
        print(f"✗ Failed to send email: {e}")
        print()
    
    print("=" * 60)
