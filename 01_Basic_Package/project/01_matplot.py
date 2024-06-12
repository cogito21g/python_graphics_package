import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 그래프 생성
plt.plot(x, y)
plt.xlabel('X-axis')  # x축 레이블
plt.ylabel('Y-axis')  # y축 레이블
plt.title('Sine Wave')  # 그래프 제목
plt.grid(True)  # 그리드 표시
plt.show()  # 그래프 보여주기


# 데이터 생성
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Figure와 Axes 생성
fig, ax = plt.subplots()

# 두 개의 선 그래프 그리기
ax.plot(x, y1, label='Sine Wave', color='blue', linestyle='-')
ax.plot(x, y2, label='Cosine Wave', color='red', linestyle='--')

# 그래프 구성 요소 설정
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Sine and Cosine Waves')
ax.legend()
ax.grid(True)

# 그래프 보여주기
plt.show()
