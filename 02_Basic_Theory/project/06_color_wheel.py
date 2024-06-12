import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge

# 색상 휠 생성
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# 기본 색상 설정
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
num_colors = len(colors)

# 색상 휠 그리기
for i, color in enumerate(colors):
    theta1 = 360 * i / num_colors
    theta2 = 360 * (i + 1) / num_colors
    wedge = Wedge(center=(0.5, 0.5), r=0.4, theta1=theta1, theta2=theta2, color=color, alpha=0.6, transform=ax.transAxes, clip_on=False)
    ax.add_patch(wedge)

# 중심에서 색상으로 선 그리기
for i in range(num_colors):
    angle = 2 * np.pi * i / num_colors
    x = 0.5 + 0.4 * np.cos(angle)
    y = 0.5 + 0.4 * np.sin(angle)
    ax.plot([0.5, x], [0.5, y], color='black')

plt.axis('off')
plt.show()
