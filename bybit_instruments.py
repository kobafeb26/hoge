import requests


def get_instruments(category="spot"):
    """Bybit APIから銘柄一覧を取得する"""
    url = "https://api.bybit.com/v5/market/instruments-info"
    params = {"category": category}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    if data["retCode"] != 0:
        raise RuntimeError(f"API error: {data['retMsg']}")

    return data["result"]["list"]


if __name__ == "__main__":
    instruments = get_instruments("spot")
    print(f"取得件数: {len(instruments)}")
    print("-" * 40)
    for inst in instruments[:20]:
        print(f"{inst['symbol']}: {inst['baseCoin']}/{inst['quoteCoin']}")
    if len(instruments) > 20:
        print(f"... 他 {len(instruments) - 20} 件")
