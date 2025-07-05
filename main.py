import yfinance as yf
import pandas as pd
from sec_edgar_downloader import Downloader


if __name__ == "__main__":
    ticker = "MSFT"
    year   = 2019
    tk = yf.Ticker(ticker)
    df_bs = tk.balance_sheet
    df_is = tk.financials
    df_cf = tk.cashflow

    print("Balance Sheet:")
    print(df_bs)
    print("\nIncome Statement:")
    print(df_is)
    print("\nCash Flow:")
    print(df_cf)

    dl = Downloader(company_name="Apple Inc.", email_address="test@test.com")

    # 下載 Apple 的 10-K 報告
    dl.get("10-K", "AAPL",limit=1)