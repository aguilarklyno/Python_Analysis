# pandas-datareader をちゃんと理解して使おう

# 自己紹介
慶應義塾大学 経済学部 3年生(2024/2/2時点)のアギラーです。
現在は「金融 x データ分析」を中心に学習中
これからゼミの研究での学習を備忘録としてまとめていきたいと思います。

# pandas-datareader とはなにか
pandas-datareaderとはpythonライブラリを用いて外部APIを叩いて様々なデータを取得できる便利な道具です。特に金融関係(株価・経済指標など)を取り扱う際は必ずと言っていいほどお世話になるライブラリです。
実はアップデート(もしくは自分のパソコンのバグ??)の都合でyfinanceでのデータ取得が出来なくなってしまったため、いっそのことpandas-datareaderの正しい使用方法を公式ドキュメントで学んでまとめようと思い、当記事を作成することにしました。

今回はこちらの[公式ドキュメント](https://pandas-datareader.readthedocs.io/en/latest/)の内容に沿って、ご紹介をしたいと思います。

# 使用方法
まずはライブラリを使用しているPython環境にインストールしましょう。

pipでインストールする場合
```terminal
pip install pandas-datareader
```

condaでインストールする場合
```terminal
conda install pandas-datareader
```

## 簡単な使用例
下記のコードではFREDというサイトからUS債券のデータを取得しています。
```python
import pandas_datareader as pdr
pdr.get_data_fred('GS10')
```

# どんなデータを取得できるのか
1. [Tiingo](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-tiingo)
2. [IEX](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-iex)
3. [Alpha Vantage](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-alphavantage)
4. [Econdb](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-econdb)
5. [Enigma](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-enigma)
6. [Quandl](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-quandl)
7. [St.Louis FED(FRED)](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-fred)
8. [Kenneeth French's data library](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-ff)
9. [World Bank](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-wb)
10. [OECD](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-oecd)
11. [Eurostat](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-eurostat)
12. [Thrift Savings Plan](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-tsp)
13. [Nasdaq Trader symbol definitions](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-nasdaq-symbols)
14. [Stooq](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-stooq)
15. [MOEX](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-moex)
16. [Yahoo Finance](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-naver)

# 実際にデータを取得してみる
## 1. Tiingo
[Tiingo](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-tiingo)とはTiingoは、株式、投資信託、ETFの過去の終値のデータAPIを提供するトレーシングプラットフォーム。APIキーの取得には無料登録が必要。無料アカウントはレートが制限されており、アクセスできるシンボル数も限られている（執筆時点では500）。

```python
import os
import pandas_datareader as pdr

df = pdr.get_data_tiingo('GOOG', api_key=os.getenv('TIINGO_API_KEY'))
df.head()
```

## 2. IEX
[インベスターズ証券取引所（IEX）](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-iex)は、APIを通じて幅広いデータを提供している。過去の株価は最大15年間までアクセス可能。データを取得するには、IEXクラウドコンソールからの公開可能なAPIキーが必要。

```python
import pandas_datareader.data as web
from datetime import datetime

start = datetime(2016, 9, 1)
end = datetime(2018, 9, 1)

f = web.DataReader('F', 'iex', start, end)
f.loc['2018-08-31']
```
## 3. Alpha Vantage
