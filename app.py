import os
import requests

WEBHOOK = os.environ["DISCORD_WEBHOOK"]

response = requests.post(
    WEBHOOK,
    json={"content": "🚨 TEST FRÅN APP.PY"}
)

print(response.status_code)
print(response.text)
