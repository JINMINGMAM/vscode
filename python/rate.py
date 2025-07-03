import requests
from bs4 import BeautifulSoup
import json

# 요청 URL 및 헤더
url = "https://finance.naver.com/marketindex/exchangeList.naver"
headers = {'User-Agent': 'Mozilla/5.0'}

# HTML 요청
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 환율 테이블 행 추출
rows = soup.select("table.tbl_exchange tbody tr")

# 결과를 담을 리스트
exchange_data = []

for row in rows:
    tds = row.select("td")
    if len(tds) >= 7:
        item = {
            "currency": tds[0].text.strip(),
            "standard_rate": tds[1].text.strip(),
            "cash_buy": tds[2].text.strip(),
            "cash_sell": tds[3].text.strip(),
            "remit_send": tds[4].text.strip(),
            "remit_receive": tds[5].text.strip(),
            "usd_ratio": tds[6].text.strip()
        }
        exchange_data.append(item)

# JSON 문자열로 변환 및 출력
json_string = json.dumps(exchange_data, ensure_ascii=False, indent=2)
print(json_string)