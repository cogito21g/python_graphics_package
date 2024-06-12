import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = 1/np.tan(x)

# Figure와 서브플롯 생성
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

# 첫 번째 서브플롯: 사인 파형
ax1.plot(x, y1, label='Sine Wave', color='blue', linestyle='-')
ax1.set_title('Sine Wave')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis')
ax1.legend()
ax1.grid(True)

# 두 번째 서브플롯: 코사인 파형
ax2.plot(x, y2, label='Cosine Wave', color='red', linestyle='--')
ax2.set_title('Cosine Wave')
ax2.set_xlabel('X-axis')
ax2.set_ylabel('Y-axis')
ax2.legend()
ax2.grid(True)

# 세 번째 서브플롯: 탄젠트 파형
ax3.plot(x, y3, label='Tangent Wave', color='green', linestyle='-.')
ax3.set_title('Tangent Wave')
ax3.set_xlabel('X-axis')
ax3.set_ylabel('Y-axis')
ax3.legend()
ax3.grid(True)

# 네 번째 서브플롯: 코탄젠트 파형
ax4.plot(x, y4, label='Cotangent Wave', color='purple', linestyle=':')
ax4.set_title('Cotangent Wave')
ax4.set_xlabel('X-axis')
ax4.set_ylabel('Y-axis')
ax4.legend()
ax4.grid(True)

# 그래프 레이아웃 조정 및 보여주기
plt.tight_layout()
plt.show()
