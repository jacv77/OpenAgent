#!/usr/bin/env python3
"""
Send a test email using AgentMail Python SDK - Correct Method
"""

from agentmail import AgentMail
from datetime import datetime

# Configuration
API_KEY = "am_us_ba71ac6140daeb3a04b3781992d0689b715a8c42c8ba19d8e833c6926f529bda"
INBOX_ID = "noctil.agent@agentmail.to"

# Initialize client
client = AgentMail(api_key=API_KEY)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("=" * 60)
print("Sending Test Email via AgentMail SDK")
print("=" * 60)
print(f"From: {INBOX_ID}")
print(f"To: {INBOX_ID} (self)")
print(f"Time: {timestamp}")
print()

try:
    # Send message using the correct SDK method
    result = client.inboxes.messages.send(
        inbox_id=INBOX_ID,
        to=["noctil.agent@agentmail.to"],
        subject=f"🧪 AgentMail Test - {timestamp}",
        text=f"""Hello from OpenClaw Agent!

This is a test email sent at {timestamp} to verify AgentMail integration.

✓ AgentMail SDK: Installed
✓ API Key: Configured  
✓ Inbox: {INBOX_ID}
✓ Status: Working!

Your OpenClaw agent can now send and receive emails programmatically.

Best regards,
OpenClaw Agent
""",
        html=f"""
<html>
<head>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }}
        h1 {{ color: #2563eb; }}
        .info-box {{ background-color: #f0f9ff; border-left: 4px solid #2563eb; padding: 15px; margin: 20px 0; }}
        .info-box h2 {{ margin-top: 0; color: #1e40af; }}
        .info-box ul {{ list-style: none; padding: 0; }}
        .footer {{ color: #6b7280; font-size: 14px; border-top: 1px solid #e5e7eb; margin-top: 30px; padding-top: 20px; }}
    </style>
</head>
<body>
    <h1>🧪 AgentMail Test</h1>
    <p><strong>Timestamp:</strong> {timestamp}</p>
    
    <div class="info-box">
        <h2>Test Results</h2>
        <ul>
            <li>✓ AgentMail SDK: <strong>Installed</strong></li>
            <li>✓ API Key: <strong>Configured</strong></li>
            <li>✓ Inbox: <strong>{INBOX_ID}</strong></li>
            <li>✓ Status: <strong>Working!</strong></li>
        </ul>
    </div>
    
    <p>Your OpenClaw agent can now send and receive emails programmatically.</p>
    
    <div class="footer">
        <strong>Best regards,</strong><br>
        OpenClaw Agent
    </div>
</body>
</html>
"""
    )
    
    print("✓ Email sent successfully!")
    print(f"  Message ID: {result.message_id}")
    print(f"  Thread ID: {result.thread_id}")
    print()
    print("Check your inbox at: https://agentmail.to")
    print()
    
except Exception as e:
    print(f"✗ Failed to send email: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

print("=" * 60)
print("Test Complete!")
print("=" * 60)
