import os
import requests

from market import get_market_report
from crypto import get_crypto_report
from forex import get_forex_report
from commodities import get_commodities_report
from ai import generate_summary

WEBHOOK = os.environ["DISCORD_WEBHOOK"]

# Hämta data
market_report = get_market_report()
crypto_report = get_crypto_report()
forex_report = get_forex_report()
commodities_report = get_commodities_report()

# AI-sammanfattning
full_report = f"""
Index
{market_report}

Crypto
{crypto_report}

Forex
{forex_report}

Commodities
{commodities_report}
"""

summary = generate_summary(full_report)

# Discord Embed med Fields
embed = {
    "title": "📈 Market Close",
    "color": 3447003,
    "fields": [
        {
            "name": "📊 Index",
            "value": market_report,
            "inline": False
        },
        {
            "name": "🪙 Crypto",
            "value": crypto_report,
            "inline": False
        },
        {
            "name": "💵 Valutor",
            "value": forex_report,
            "inline": False
        },
        {
            "name": "🛢 Råvaror",
            "value": commodities_report,
            "inline": False
        },
        {
            "name": "🤖 AI Market Summary",
            "value": summary,
            "inline": False
        }
    ],
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
