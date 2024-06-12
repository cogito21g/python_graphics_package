import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
data = np.random.randn(1000)

# 히스토그램 그리기
plt.hist(data, bins=30, color='purple', edgecolor='black')

# 그래프 구성 요소 설정
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.show()
