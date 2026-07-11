import os
import requests
import sys

webhook = os.environ.get("DISCORD_WEBHOOK")

print("Webhook exists:", webhook is not None)
print("Webhook starts with:", webhook[:25] if webhook else "None")

response = requests.post(
    webhook,
    json={"content": "✅ Test från GitHub Actions"}
)

print("Status:", response.status_code)
print("Body:", response.text)

response.raise_for_status()

sys.exit(0)
