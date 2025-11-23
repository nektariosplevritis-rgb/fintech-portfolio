#sp500_tracker.py
#Simple S&P 500 historical performance tracker
#Author: Nektarios Plevritis - CFA L1

import yfinance as yf
import pandas as pd
from datetime import datetime

def sp500_performance(years: int = 5):
  #Download S&P 500 data (^GSPC = ticket for S&P 500)
  ticket = "^GSPC"
  data = yf.download(ticket, period=f"{years}y")
  #Basic calculations
  data['Daily_Return'] = data['Close'].pct_change()
  data['Cumulative_Return'] = (1+data['Daily_Return'], cumprod()-1
  #Final stats
  total_return = data['Cumulative_Return'].iloc[-1]*100
  cagr=((data['Close'].iloc[-1] / data['Close'].iloc[0]**(1/years)
  volatility=data['Daily_Return'].std()*(252**0.5)*100 #annualized
