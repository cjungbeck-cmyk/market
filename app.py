import os
import requests

from market import get_market_report

WEBHOOK = os.environ["DISCORD_WEBHOOK"]

message = f"""
# 📈 Market Close

{get_market_report()}
"""

requests.post(
    WEBHOOK,
    json={"content": message}
)
