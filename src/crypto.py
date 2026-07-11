import requests


def get_crypto_report():

    url = (
        "https://api.coingecko.com/api/v3/simple/price"
        "?ids=bitcoin,ethereum"
        "&vs_currencies=usd"
        "&include_24hr_change=true"
    )

    data = requests.get(url).json()

    report = []

    for coin in ["bitcoin", "ethereum"]:

        change = data[coin]["usd_24h_change"]

        emoji = "🟢" if change >= 0 else "🔴"

        report.append(
            f"{emoji} **{coin.title()}** {change:+.2f}%"
        )

    return "\n".join(report)
