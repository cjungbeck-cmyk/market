import yfinance as yf

markets = {
    "S&P 500": "^GSPC",
    "Nasdaq": "^IXIC",
    "Dow Jones": "^DJI",
    "OMXS30": "^OMXS30",
    "DAX": "^GDAXI",
}

def get_market_report():

    report = []

    for name, ticker in markets.items():

        data = yf.download(
            ticker,
            period="2d",
            progress=False,
            auto_adjust=False
        )

        if len(data) < 2:
            continue

        close = float(data["Close"].iloc[-1])
        previous = float(data["Close"].iloc[-2])

        change = ((close-previous)/previous)*100

        emoji = "🟢" if change >= 0 else "🔴"

        report.append(
            f"{emoji} **{name}** {change:.2f}%"
        )

    return "\n".join(report)
