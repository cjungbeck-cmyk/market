import requests


def get_forex_report():

    url = "https://open.er-api.com/v6/latest/USD"

    data = requests.get(url).json()

    usdsek = data["rates"]["SEK"]

    eursek = usdsek / data["rates"]["EUR"]

    return (
        f"💵 **USD/SEK** {usdsek:.2f}\n"
        f"💶 **EUR/SEK** {eursek:.2f}"
    )
