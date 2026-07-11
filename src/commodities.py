import yfinance as yf


def get_commodities_report():

    assets = {
        "Gold": "GC=F",
        "Brent": "BZ=F",
    }

    report = []

    for name, ticker in assets.items():

        try:

            hist = yf.Ticker(ticker).history(period="5d")

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

        except Exception:
            report.append(f"⚠️ {name}")

    return "\n".join(report)
