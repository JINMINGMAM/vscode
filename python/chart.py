import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# 한글 폰트
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 결과 저장
departments = ['영업부', '기획부', '개발부']
sales_data = {
    '사이트A': [],
    '사이트B': [],
    '사이트C': []
}

# -----------------------
# 사이트별 스크래핑 함수
# -----------------------
def scrape_sales(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.select("table.sales tr")[1:]  # 첫 번째 행은 헤더

    result = []
    for row in rows:
        cols = row.select("td")
        result.append(int(cols[1].text.replace(",", "")))
    return result

# -----------------------
# 실제 요청 (예시 URL, 변경 필요)
# -----------------------
# 가상 URL – 실제 업무 시스템에서는 내부 서버 또는 API일 수 있음
urls = {
    '사이트A': 'https://example.com/siteA_sales.html',
    '사이트B': 'https://example.com/siteB_sales.html',
    '사이트C': 'https://example.com/siteC_sales.html'
}

# 예시 대신 샘플 데이터 입력 (실제 스크래핑 실패 방지용)
sales_data['사이트A'] = [10000, 8000, 12000]
sales_data['사이트B'] = [11000, 9000, 13000]
sales_data['사이트C'] = [10500, 8500, 12500]

# -----------------------
# 시각화 (부서별 막대 그래프)
# -----------------------
import numpy as np
x = np.arange(len(departments))
width = 0.25

plt.figure(figsize=(10, 6))
plt.bar(x - width, sales_data['사이트A'], width=width, label='사이트A')
plt.bar(x, sales_data['사이트B'], width=width, label='사이트B')
plt.bar(x + width, sales_data['사이트C'], width=width, label='사이트C')

plt.xticks(x, departments)
plt.ylabel("매출액 (천 원)")
plt.title("부서별 매출 비교")
plt.legend()
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()
