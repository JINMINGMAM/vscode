import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 한글 폰트 설정 (Windows 기준)
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

# 데이터
data = {
    '프로젝트': ['A 프로젝트', 'B 프로젝트', 'C 프로젝트', 'D 프로젝트'],
    '예산 (백만원)': [100, 150, 200, 120],
    '실적 (백만원)': [90, 160, 180, 130]
}

df = pd.DataFrame(data)
x = range(len(df))
bar_width = 0.35

# 그래프
plt.figure(figsize=(9, 5))
plt.bar(x, df['예산 (백만원)'], width=bar_width, label='예산', color='skyblue')
plt.bar([i + bar_width for i in x], df['실적 (백만원)'], width=bar_width, label='실적', color='orange')

# X축 레이블 회전 적용
plt.xticks([i + bar_width / 2 for i in x], df['프로젝트'], rotation=15)

plt.ylabel('금액 (백만원)')
plt.title('프로젝트 예산 대비 실적 비교')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
