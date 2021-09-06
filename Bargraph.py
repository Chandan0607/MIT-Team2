import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance.original_flavor as mpf

datafile = 'data_file.csv'
data = pd.read_csv(datafile, index_col='date')
data.index = pd.to_datetime(data.index)

dvalues = data[['open', 'high', 'low', 'close']].values.tolist()

pdates = mdates.date2num(data.index)

ohlc = [[pdates[i]] + dvalues[i]
for i in range(len(pdates))]



plt.style.use('fivethirtyeight')
fig, ax = plt.subplots(figsize=(12, 6))

mpf.plot_day_summary_ohlc(ax, ohlc[-50:], ticksize=5)

ax.set_xlabel('Date')
ax.set_ylabel('Price ($)')
ax.set_title('SPDR S&P 500 ETF Trust - Bar Chart')

ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

fig.autofmt_xdate()

plt.show()
