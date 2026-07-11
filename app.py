import os
import requests

WEBHOOK = os.environ["DISCORD_WEBHOOK"]
FINNHUB = os.environ["FINNHUB_API_KEY"]

url = "https://finnhub.io/api/v1/quote"

params = {
    "symbol": "SPY",
    "token": FINNHUB
}

response = requests.get(url, params=params)
data = response.json()

price = data["c"]
previous = data["pc"]

change = ((price - previous) / previous) * 100

emoji = "🟢" if change >= 0 else "🔴"

message = f"""
📈 **Market Test**

{emoji} S&P 500
Pris: {price:.2f}
Förändring: {change:.2f}%
"""

requests.post(
    WEBHOOK,
    json={"content": message}
)
