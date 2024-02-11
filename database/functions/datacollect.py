import yfinance as yf

def get_yfinanceInfo(tickers_list):
    """
    複数のティッカーコードに対応するyfinance.Tickerオブジェクトを取得する。
    :param ticker_codes: ティッカーコードのリスト
    :return: 各ティッカーコードに対応するyfinance.Tickerオブジェクトの辞書
    """
    tickers = {}
    for code in tickers_list:
        tickers[code] = yf.Ticker(code)
    return tickers