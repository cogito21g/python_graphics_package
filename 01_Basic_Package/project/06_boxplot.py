import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
data = [np.random.randn(100) for _ in range(4)]

# 상자 그림 그리기
plt.boxplot(data, patch_artist=True, notch=True)

# 그래프 구성 요소 설정
plt.xlabel('Dataset')
plt.ylabel('Value')
plt.title('Box Plot Example')
plt.show()
