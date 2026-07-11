import os
import requests

from market import get_market_report
from crypto import get_crypto_report

WEBHOOK = os.environ["DISCORD_WEBHOOK"]

embed = {
    "title": "📈 Market Close",
    "description":
    "## 📊 Index\n"
    + get_market_report()
    + "\n\n## 🪙 Crypto\n"
    + get_crypto_report(),
    "color": 3447003,
    "footer": {
        "text": "MarketBot • Powered by GitHub Actions"
    }
}

response = requests.post(
    WEBHOOK,
    json={
        "embeds": [embed]
    }
)

print("Discord status:", response.status_code)
print("Discord response:", response.text)

response.raise_for_status()
