# Credits to: https://blog.quantinsti.com/python-trading/#:~:text=Python%20makes%20it%20easier%20to,hassle%20and%20time%2Dconsuming%20job.
# An implementation of MACD trading signal

import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = yf.download('TSLA', start='2020-01-01')

sns.lineplot(data=data)
sns.set_style('darkgrid')
plt.figure(figsize=(10, 5))
data['Close'].plot()
plt.legend()
plt.show()

# calculate exponential moving average
data['12d_EMA'] = data.Close.ewm(span=12, adjust=False).mean()
data['26d_EMA'] = data.Close.ewm(span=26, adjust=False).mean()

data[['Close','12d_EMA','26d_EMA']].plot(figsize=(10,5))
plt.show()

# calculate macd
data['macd'] = data['12d_EMA'] - data['26d_EMA']

# calculate signal
data['macdsignal'] = data.macd.ewm(span=9, adjust=False).mean()

data[['macd', 'macdsignal']].plot()
plt.show()

# macd trading signal, when value of MACD signal > signal, buy, else sell
# define signal
data['trading_signal'] = np.where(data['macd'] > data['macdsignal'], 1, -1)

# calculate returns
# pct_change calculates percentage change within pandas.DataFrame
data['returns'] = data.Close.pct_change()

# calculate strategy returns
data['strategy_returns'] = data.returns * data.trading_signal.shift(1)

# calculate cumulative returns
# cumprod() calculates cumulative product using pandas.DataFrame
cumulative_strategy_returns = (data.strategy_returns + 1).cumprod()

# plot strategy returns
cumulative_strategy_returns.plot()
plt.show()

# Sample strategy evaluation
# annualised return/compound annual growth rate

# total number of trading days
days = len(cumulative_strategy_returns)

# calculate compound annual growth rate
# 252 is the 252 business days in a year
annual_returns = (cumulative_strategy_returns.iloc[-1]**(252/days)-1)*100

print('The CAGR is %.2f%%' % annual_returns)

# Annualised volatility - variation in stock price over time
# calculate annualised volatility
annual_volatility = data.strategy_returns.std() * np.sqrt(252) * 100

print('The annualised volatility is %.2f%%' % annual_volatility)

# Sharpe ratio - risk taken in comparison to risk-free investments
# using sharpe ratio = (annualised return of investment - annualised risk free rate) / standard deviation of investment

# Current annual risk free rate of Australia is 0.06%, sad times
risk_free_rate = 0.0006
daily_risk_free_return = risk_free_rate/252

# calculate excess returns, subtracting daily returns by daily risk free return
excess_daily_returns = data.strategy_returns - daily_risk_free_return

# calculate sharpe ratio
sharpe_ratio = (excess_daily_returns.mean() / excess_daily_returns.std()) * np.sqrt(252)

print('The Sharpe ratio is %.2f' % sharpe_ratio)
# the higher the sharpe ratio, the better the return relative to investment risk