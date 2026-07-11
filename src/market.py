import yfinance as yf

markets = {
    "S&P 500": "^GSPC",
    "Nasdaq": "^IXIC",
    "Dow Jones": "^DJI",
    "DAX": "^GDAXI",
}


def get_market_report():

    report = []

    for name, ticker in markets.items():

        try:

            ticker_obj = yf.Ticker(ticker)
            hist = ticker_obj.history(period="5d")

            if hist.empty or len(hist) < 2:
                report.append(f"⚪ {name} Ingen data")
                continue

            close = hist["Close"].iloc[-1]
            previous = hist["Close"].iloc[-2]

            change = ((close - previous) / previous) * 100

            emoji = "🟢" if change >= 0 else "🔴"

            report.append(
                f"{emoji} **{name}** {change:+.2f}%"
            )

        except Exception as e:
            report.append(f"⚠️ {name}: {e}")

    return "\n".join(report)
