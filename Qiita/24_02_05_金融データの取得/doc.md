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
8. [Kenneth French's data library](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-ff)
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
[Alpha Vantage](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-alphavantage)は、リアルタイムの株式と為替データを提供します。APIキーの取得には無料登録が必要です。
### 3.1 時系列データの取得
Alpha Vantageの様々なAPIのエンドポイントを提供しています。個々の株式および為替レートの時系列データを取得することができます。日足、週足、月足については、20年以上の時系列データが利用可能です。
【提供しているAPIエンドポイント】
- av-intraday - Intraday Time Series
- av-daily - Daily Time Series
- av-daily-adjusted - Daily Time Series (Adjusted)
- av-weekly - Weekly Time Series
- av-weekly-adjusted - Weekly Time Series (Adjusted)
- av-monthly - Monthly Time Series
- av-monthly-adjusted - Monthly Time Series (Adjusted)
- av-forex-daily - Daily Time Series

```python:ipynb
import os
from datetime import datetime
import pandas_datareader.data as web

f = web.DataReader("AAPL", "av-daily",
                    start=datetime(2017, 2, 9),
                    end=datetime(2017, 5, 24),
                    api_key=os.getenv('ALPHAVANTAGE_API_KEY')
                  )

f.loc["2017-02-09"]
```



## 4. Econdb
[Econdb](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-econdb)は90以上の公的統計機関の経済データを提供しています。無料のAPIを使用してアクセスできます。米国のRGDPのような1列のデータを読み込むには、URLパスからティッカーを取得して（https://www.econdb.com/series/RGDPUS/ のRGDPUS）

```python:ipynb
import os
import pandas_datareader.data as web

f = web.DataReader('ticker=RGDPUS', 'econdb')
f.head()
```
データセット全体、またはフィルタリングされたサブセットをエクスポートするためのコードスニペットは、EurostatのGDPや主成分など、利用可能な多くのデータセットのいずれかにExport -> Pandas Python3機能を使用して生成することができます。

```python: ipynb
import os
import pandas_datareader.data as web

df = web.DataReader('dataset=NAMQ_10_GDP&v=Geopolitical entity (reporting)&h=TIME&from=2018-05-01&to=2021-01-01&GEO=[AL,AT,BE,BA,BG,HR,CY,CZ,DK,EE,EA19,FI,FR,DE,EL,HU,IS,IE,IT,XK,LV,LT,LU,MT,ME,NL,MK,NO,PL,PT,RO,RS,SK,SI,ES,SE,CH,TR,UK]&NA_ITEM=[B1GQ]&S_ADJ=[SCA]&UNIT=[CLV10_MNAC]', 'econdb')
df.columns
```
データセットは、Econdbの検索エンジンで探すこともでき、さらに利用可能な統計ソースのツリーを探索して発見することもできます。


## 5. Enigma
[Enigma](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-enigma)は個人的に一番名前が好きなやつ。
公共データの世界最大のリポジトリであるEnigmaからデータセットにアクセスします。リリース0.6.0から、古いAPIが廃止されたため、エニグマのURLがapp.enigma.ioから変更されたことにご注意を。データセットは、データセットのウェブアドレスの末尾にあるuuid4によって一意に識別されます。
次のコードは USDA Food Recalls 1996 Data からダウンロードします。
```python: ipynb
import os
import pandas_datareader as pdr

df = pdr.get_data_enigma('292129b0-1275-44c8-a6a3-2a0881f24fe1', os.getenv('ENIGMA_API_KEY'))

df.columns

#Index(['case_number', 'recall_notification_report_number',
#       'recall_notification_report_url', 'date_opened', 'date_closed',
#       'recall_class', 'press_release', 'domestic_est_number', 'company_name',
#       'imported_product', 'foreign_estab_number', 'city', 'state', 'country',
#       'product', 'problem', 'description', 'total_pounds_recalled',
#       'pounds_recovered'],
#      dtype='object')
```

## 6. Quandl
[Quandl](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-quandl)は日次金融データ（株式、ETFなどの価格）を取得できます。
シンボル名は2つの部分で構成されています：DB名とシンボル名です。DB名は、Quandlのウェブサイトに掲載されている無料のものをすべて使用できます。シンボル名はDB名によって異なり、WIKI（米国株）の場合は一般的なティッカーシンボルですが、その他の場合（FSEなど）は少し奇妙なものになります。
- 現在、BE, CN, DE, FR, IN, JP, NL, PT, UK, USで利用可能。
注意：2017年6月現在、各DBは異なるデータ・スキーマを持っているため、取得可能期間が短いことがあり、データの質は必ずしも良いとは言えないです。
```python:ipynb
import pandas_datareader.data as web
symbol = 'WIKI/AAPL'  # or 'AAPL.US'

df = web.DataReader(symbol, 'quandl', '2015-01-01', '2015-01-05')
df.loc['2015-01-02']

#              Open    High     Low   Close      Volume  ...     AdjOpen     AdjHigh      AdjLow    AdjClose   AdjVolume
# Date                                                    ...
# 2015-01-02  111.39  111.44  107.35  109.33  53204626.0  ...  105.820966  105.868466  101.982949  103.863957  53204626.0
```


## 7. St.Louis FED(FRED)
[St.Louis FED(FRED)](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-fred)はアメリカの経済指標やコモディティの先物価格などを取得でき、データの種類が豊富でおすすめです。なので株価以外の経済指標はここから取得することが多いです。
```python:ipynb
import pandas_datareader.data as web
import datetime

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2013, 1, 27)
gdp = web.DataReader('GDP', 'fred', start, end)
gdp.loc['2013-01-01']
 
# GDP    16569.591
# Name: 2013-01-01 00:00:00, dtype: float64

# Multiple series:
inflation = web.DataReader(['CPIAUCSL', 'CPILFESL'], 'fred', start, end)
inflation.head()

#            CPIAUCSL  CPILFESL
# DATE                          
# 2010-01-01   217.488   220.633
# 2010-02-01   217.281   220.731
# 2010-03-01   217.353   220.783
# 2010-04-01   217.403   220.822
# 2010-05-01   217.290   220.962
```

## 8. Kenneth French's data library
[Kenneth French's data library](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-ff)は基本的にCAPM理論を応用した3因子モデルや5因子モデルで使用するデータが格納されています。Fama/French Data Library のデータセットにアクセスすることができ、get_available_datasets関数は、利用可能なすべてのデータセットのリストを返します。

```python:ipynb
from pandas_datareader.famafrench import get_available_datasets
import pandas_datareader.data as web

len(get_available_datasets())
#output: 297

ds = web.DataReader('5_Industry_Portfolios', 'famafrench')
print(ds['DESCR'])
# 5 Industry Portfolios
# ---------------------
# This file was created by CMPT_IND_RETS using the 202105 CRSP database. It contains value- and equal-weighted returns for 5 industry portfolios. The portfolios are constructed at the end of June. The annual returns are from January to December. Missing data are indicated by -99.99 or -999. Copyright 2021 Kenneth R. French
#  0 : Average Value Weighted Returns -- Monthly (59 rows x 5 cols)
#  1 : Average Equal Weighted Returns -- Monthly (59 rows x 5 cols)
#  2 : Average Value Weighted Returns -- Annual (5 rows x 5 cols)
#  3 : Average Equal Weighted Returns -- Annual (5 rows x 5 cols)
#  4 : Number of Firms in Portfolios (59 rows x 5 cols)
#  5 : Average Firm Size (59 rows x 5 cols)
#  6 : Sum of BE / Sum of ME (5 rows x 5 cols)
#  7 : Value-Weighted Average of BE/ME (5 rows x 5 cols)

ds[4].head()

#         Cnsmr  Manuf  HiTec  Hlth   Other
# Date                                      
# 2016-07    539    622    719    620   1109
# 2016-08    536    621    713    614   1099
# 2016-09    534    615    705    609   1090
# 2016-10    530    613    699    604   1087
# 2016-11    529    611    688    600   1084
```

## 9. World Bank
[World Bank](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-wb)pandasユーザーは、wb I/O関数を使用することで、世界銀行の世界開発指標から何千ものパネルデータシリーズに簡単にアクセスすることができます。

### 指標
世界銀行のサイト内を探索するか、検索機能を使用することで、すべての世界銀行指標にアクセスすることができます。
例えば、北米の一人当たり国内総生産（恒常ドル）を比較したい場合は、検索機能を使用します：
```python: ipynb
from pandas_datareader import wb
matches = wb.search('gdp.*capita.*const')
```
そして、ダウンロード機能を使って世界銀行のサーバーからデータを取得する：
```python: ipynb
dat = wb.download(indicator='NY.GDP.PCAP.KD', country=['US', 'CA', 'MX'], start=2005, end=2008)
print(dat)

#                      NY.GDP.PCAP.KD
# country       year
# Canada        2008  36005.5004978584
#               2007  36182.9138439757
#               2006  35785.9698172849
#               2005  35087.8925933298
# Mexico        2008  8113.10219480083
#               2007  8119.21298908649
#               2006  7961.96818458178
#               2005  7666.69796097264
# United States 2008  43069.5819857208
#               2007  43635.5852068142
#               2006   43228.111147107
#               2005  42516.3934699993
```
出来上がったデータセットは、階層インデックスを持つ適切にフォーマットされたDataFrameなので、.groupby変換を適用するのがオススメです：
```python: ipynb
dat['NY.GDP.PCAP.KD'].groupby(level=0).mean()

# country
# Canada           35765.569188
# Mexico            7965.245332
# United States    43112.417952
# dtype: float64
```
こんな感じでさまざまな国のデータを取得できます。
もしデータ分析系のレポートがあれば、上記のデータベースから適当に取得し分析すればすぐに終わりますね。

## 10.OECD
[OECD](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-oecd)はDataReader経由で入手できます。取得する場合はOECDのデータセットコードを指定する必要があります。データセットコードの確認は、each data -> Export -> SDMX Query.で行います。
以下の例は、セットコードが「TUD」である「労働組合密度」データをダウンロードする例です。
```python: ipynb
import pandas_datareader.data as web
import datetime

df = web.DataReader('TUD', 'oecd')

df.columns

# MultiIndex([(      'Australia', 'Annual', 'Percentage of employees'),
#             (        'Austria', 'Annual', 'Percentage of employees'),
#             (        'Belgium', 'Annual', 'Percentage of employees'),
#             (         'Canada', 'Annual', 'Percentage of employees'),
#             ( 'Czech Republic', 'Annual', 'Percentage of employees'),
#             (        'Denmark', 'Annual', 'Percentage of employees'),
#             (        'Finland', 'Annual', 'Percentage of employees'),
#             (         'France', 'Annual', 'Percentage of employees'),
#             (        'Germany', 'Annual', 'Percentage of employees'),
#             (         'Greece', 'Annual', 'Percentage of employees'),
#             (        'Hungary', 'Annual', 'Percentage of employees'),
#             (        'Iceland', 'Annual', 'Percentage of employees'),
#             (        'Ireland', 'Annual', 'Percentage of employees'),
#             (          'Italy', 'Annual', 'Percentage of employees'),
#             (          'Japan', 'Annual', 'Percentage of employees'),
#             (          'Korea', 'Annual', 'Percentage of employees'),
#             (     'Luxembourg', 'Annual', 'Percentage of employees'),
#             (         'Mexico', 'Annual', 'Percentage of employees'),
#             (    'Netherlands', 'Annual', 'Percentage of employees'),
#             (    'New Zealand', 'Annual', 'Percentage of employees'),
#             (         'Norway', 'Annual', 'Percentage of employees'),
#             (         'Poland', 'Annual', 'Percentage of employees'),
#             (       'Portugal', 'Annual', 'Percentage of employees'),
#             ('Slovak Republic', 'Annual', 'Percentage of employees'),
#             (          'Spain', 'Annual', 'Percentage of employees'),
#             (         'Sweden', 'Annual', 'Percentage of employees'),
#             (    'Switzerland', 'Annual', 'Percentage of employees'),
#             (         'Turkey', 'Annual', 'Percentage of employees'),
#             ( 'United Kingdom', 'Annual', 'Percentage of employees'),
#             (  'United States', 'Annual', 'Percentage of employees'),
#             (   'OECD - Total', 'Annual', 'Percentage of employees'),
#             (          'Chile', 'Annual', 'Percentage of employees'),
#             (       'Colombia', 'Annual', 'Percentage of employees'),
#             (     'Costa Rica', 'Annual', 'Percentage of employees'),
#             (        'Estonia', 'Annual', 'Percentage of employees'),
#             (         'Israel', 'Annual', 'Percentage of employees'),
#             (         'Latvia', 'Annual', 'Percentage of employees'),
#             (      'Lithuania', 'Annual', 'Percentage of employees'),
#             (       'Slovenia', 'Annual', 'Percentage of employees')],
#            names=['Country', 'Frequency', 'Measure'])
# 
# In [19]: df[['Japan', 'United States']]
# Out[19]: 
# Country                      Japan           United States
# Frequency                   Annual                  Annual
# Measure    Percentage of employees Percentage of employees
# Time                                                      
# 2017-01-01               17.500000                    10.6
# 2018-01-01               17.200001                    10.3
# 2019-01-01               16.799999                     9.9
# 2020-01-01                     NaN                    10.3
```

## 11. Eurostat
[Eurostat](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-eurostat)はDataReaderを通じてアクセス可能です。

具体例として、鉄道事故の事故種別（ERAデータ）データを取得してみます。
結果は、DatetimeIndexをインデックス、属性または国のMultiIndexをカラムとするDataFrameとなります。
対象URLは以下の通り：
- http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=tran_sf_railac&lang=en

データセットIDに'tran_sf_railac'を指定すると、DataReader経由で対応するデータを取得することができます。
```python: ipynb
import pandas_datareader.data as web
df = web.DataReader('tran_sf_railac', 'eurostat')
df

# UNIT                                                                                      Number  ...               
# ACCIDENT    Collisions of trains, including collisions with obstacles within the clearance gauge  ...        Unknown
# GEO                                                                                      Austria  ... United Kingdom
# FREQ                                                                                      Annual  ...         Annual
# TIME_PERIOD                                                                                       ...               
# 2017-01-01                                                 7.0                                    ...            NaN
# 2018-01-01                                                 4.0                                    ...            NaN
# 2019-01-01                                                 1.0                                    ...            NaN
# [3 rows x 264 columns]
```

## 12. Thrift Savings Plan
[Thrift Savings Plan](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-tsp)ではThrift Savings Plan (TSP)の投資信託インデックス価格をダウンロードすることができます。
```python: ipynb
# import pandas_datareader.tsp as tsp
# tspreader = tsp.TSPReader(start='2015-10-1', end='2015-12-31')
# tspreader.read()

#            L Income  L 2025   L 2030  ...   C Fund   S Fund   I Fund
# Date                                   ...                           
# 2015-12-31   17.7733     NaN  25.0635  ...  27.5622  35.2356  24.0952
# 2015-12-30   17.8066     NaN  25.2267  ...  27.8239  35.5126  24.4184
# 2015-12-29   17.8270     NaN  25.3226  ...  28.0236  35.8047  24.4757
# 2015-12-28   17.7950     NaN  25.1691  ...  27.7230  35.4625  24.2816
# 2015-12-24   17.7991     NaN  25.2052  ...  27.7831  35.6084  24.3272
# ...              ...     ...      ...  ...      ...      ...      ...
# 2015-10-07   17.6639     NaN  24.8629  ...  26.7751  35.6035  24.3671
# 2015-10-06   17.6338     NaN  24.7268  ...  26.5513  35.1320  24.2294
# 2015-10-05   17.6395     NaN  24.7571  ...  26.6467  35.3565  24.1475
# 2015-10-02   17.5707     NaN  24.4472  ...  26.1669  34.6504  23.6367
# 2015-10-01   17.5164     NaN  24.2159  ...  25.7953  34.0993  23.3202
# [62 rows x 15 columns]
```

## 13. Nasdaq Trader symbol definitions
[Nasdaq Trader symbol definitions](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-nasdaq-symbols)はナスダックから最新のシンボルをダウンロードすることができます。

## 14. Stooq
[Stooq](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-stooq)。グーグルファイナンスは一般的な指数データのダウンロードを提供していないため、Stooqサイトを経由してデータをダウンロードできます。
```python: ipynb
import pandas_datareader.data as web
f = web.DataReader('^DJI', 'stooq')
f[:10]

#                 Open      High       Low     Close     Volume
# Date                                                         
# 2021-07-12  34836.75  35014.90  34730.15  34996.18  344606907
# 2021-07-09  34457.51  34893.72  34457.51  34870.16  340542786
# 2021-07-08  34569.01  34569.01  34145.59  34421.93  374853414
# 2021-07-07  34604.17  34708.78  34435.59  34681.79  340215866
# 2021-07-06  34790.16  34814.20  34358.42  34577.37  390545107
# 2021-07-02  34642.42  34821.93  34613.49  34786.35  332517041
# 2021-07-01  34507.32  34640.28  34498.85  34633.53  309690314
# 2021-06-30  34290.74  34553.16  34245.48  34502.51  333493947
# 2021-06-29  34338.89  34469.83  34266.83  34292.29  321388212
# 2021-06-28  34428.10  34449.65  34186.13  34283.27  320257590
```



## 15. MOEX
[MOEX](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-moex)はモスクワ取引所（MOEX）がヒストリカルデータを提供しているものです。
pandas_datareader.get_data_moex(*args)はpandas_datareader.moex.MoexReader(*args).read()と同じです。
```python:ipynb
import pandas_datareader as pdr
f = pdr.get_data_moex(['USD000UTSTOM', 'MAGN'], '2020-07-02', '2020-07-07')
f.head()

#             ADMITTEDQUOTE  ADMITTEDVALUE  ...  YIELDLASTCOUPON  YIELDTOOFFER
# TRADEDATE                                 ...                               
# 2020-07-02            NaN            NaN  ...              NaN           NaN
# 2020-07-03            NaN            NaN  ...              NaN           NaN
# 2020-07-06            NaN            NaN  ...              NaN           NaN
# 2020-07-07            NaN            NaN  ...              NaN           NaN
# 2020-07-02         37.605    670695507.0  ...              NaN           NaN
#
# [5 rows x 66 columns]

f = pdr.moex.MoexReader('SBER', '2020-07-02', '2020-07-03').read()
f.head()

#             ADMITTEDQUOTE  ADMITTEDVALUE  ...  YIELDLASTCOUPON  YIELDTOOFFER
# TRADEDATE                                 ...                               
# 2020-07-02         210.00   1.514438e+10  ...              NaN           NaN
# 2020-07-03         210.08   1.036950e+10  ...              NaN           NaN
# 
# [2 rows x 65 columns]
```
## 16. Yahoo Finance
[Yahoo Finance](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-naver)はヤフーファイナンスが株式市場データを提供しているものです。
以下のエンドポイントが利用可能です：

- yahoo - 毎日の株価（高値、始値、終値、出来高、調整後終値）を取得。
- yahoo-actions - 過去のコーポレートアクション（配当、株式分割）を取得。
- yahoo-dividends - 過去の配当金を検索します。

```python: ipynb
import pandas_datareader.data as web
import pandas as pd
import datetime as dt

df = web.DataReader('GE', 'yahoo', start='2019-09-10', end='2019-10-09')
df.head()

#             High   Low  Open  Close      Volume  Adj Close
# Date                                                      
# 2019-09-10  9.27  8.90  8.91   9.14  62617200.0   9.062220
# 2019-09-11  9.36  9.06  9.15   9.36  57094900.0   9.280347
# 2019-09-12  9.52  9.22  9.40   9.26  68115100.0   9.181198
# 2019-09-13  9.45  9.14  9.31   9.34  45589400.0   9.270529
# 2019-09-16  9.42  9.17  9.30   9.38  45748400.0   9.310231
```
しかし上記のコードでは一部のpython実行環境だとエラーが出てしまいます。
そこでpandas_datareaderではなく直接yfinanceをインストールして使いましょう。

## Extra: 全ての解決策 yfinance
Yahoo Finance Dataを実行すると、エラーが出てしまいます。
そのため、代替品として「yfinance」というライブラリがあります。

pip環境ではいつものように下記コードでインストールできます。
```terminal
pip install yfinance
```
しかしconda環境では下記のコードを走らせるだけではエラーが出てしまいます。
```teminal
conda install yfinance
```
したがってconda-forgeのバージョンをインストールしましょう。
詳しいパッケージの情報は[ANACONDA公式](https://anaconda.org/conda-forge/yfinance)を参照
```terminal
conda install conda-forge::yfinance
```

では実際にデータを取得してみます
```python:ipynb
import pandas_datareader.data as web
import pandas as pd
import datetime as dt

df = web.DataReader('GE', 'yahoo', start='2019-09-10', end='2019-10-09')
df.head()

#            High   Low  Open  Close      Volume  Adj Close
# Date                                                      
# 2019-09-10  9.27  8.90  8.91   9.14  62617200.0   9.062220
# 2019-09-11  9.36  9.06  9.15   9.36  57094900.0   9.280347
# 2019-09-12  9.52  9.22  9.40   9.26  68115100.0   9.181198
# 2019-09-13  9.45  9.14  9.31   9.34  45589400.0   9.270529
# 2019-09-16  9.42  9.17  9.30   9.38  45748400.0   9.310231
```