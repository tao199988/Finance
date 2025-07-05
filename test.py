from sec_edgar_downloader import Downloader
from bs4 import BeautifulSoup
import os
import re

# 初始化下載器
dl = Downloader("sec_data","test@test.com")  # 所有下載的資料會放在這個資料夾

# 下載 Apple 最近一份 10-K 年報
dl.get("10-K", "AAPL", limit=1)

# 找出下載的 HTML 檔案位置
folder_path = os.path.join("sec-edgar-filings", "AAPL", "10-K")
latest_folder = sorted(os.listdir(folder_path))[-1]  # 取最新一份報告
html_files = [f for f in os.listdir(os.path.join(folder_path, latest_folder)) if f.endswith(".htm") or f.endswith(".html")]
print(html_files)
# 載入 HTML 檔案
with open(os.path.join(folder_path, latest_folder, html_files[0]), "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "lxml")

print(soup)
# 解析報告標題與結構
print("📄 報告標題：")
print(soup.title.text.strip())
print("\n")

# 找出所有可能的財務資料表格（此處範例抓含「Consolidated Statements」的 table）
tables = soup.find_all("table")

# 搜尋包含關鍵字的表格，例如 "Consolidated Statements of Operations"
target_tables = []
for table in tables:
    if table.find_previous("p") and "Consolidated" in table.find_previous("p").text:
        target_tables.append(table)

# 以簡單方式印出其中一個表格的文字內容（示意）
for idx, table in enumerate(target_tables[:1]):
    print(f"🔍 表格 {idx+1} 預覽：")
    print(table.get_text(separator="\n", strip=True))
