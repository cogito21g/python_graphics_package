### 6. 색상 이론

#### 6.1 색상 휠
**이론**:
- **색상 휠의 개념**: 색상 휠은 색상 간의 관계를 시각적으로 나타내는 도구입니다. 색상은 기본 색(primary colors), 보조 색(secondary colors), 3차 색(tertiary colors)으로 나뉩니다.
- **활용 사례**: 색상 선택, 색상 조합, 색상 대비

**실습**:
Python을 사용하여 색상 휠을 그려보겠습니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# 색상 휠 생성
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# 기본 색상 설정
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
num_colors = len(colors)

# 색상 휠 그리기
for i, color in enumerate(colors):
    wedge = plt.Circle((0.5, 0.5), 0.4, color=color, alpha=0.6, 
                       transform=plt.gca().transAxes, clip_on=False)
    ax.add_patch(wedge)

# 중심에서 색상으로 선 그리기
for i in range(num_colors):
    angle = 2 * np.pi * i / num_colors
    x = 0.5 + 0.4 * np.cos(angle)
    y = 0.5 + 0.4 * np.sin(angle)
    ax.plot([0.5, x], [0.5, y], color='black')

plt.axis('off')
plt.show()
```
이 코드는 간단한 색상 휠을 생성하고 하나의 색을 시각적으로 보여줍니다.

```python
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

```
이 코드는 간단한 색상 휠을 생성하고 여러가지 색을 시각적으로 보여줍니다.

#### 6.2 보색
**이론**:
- **보색의 개념**: 보색은 색상 휠에서 서로 반대에 위치한 색상입니다. 예를 들어, 빨강과 초록, 파랑과 주황이 보색 관계에 있습니다.
- **활용 사례**: 디자인에서 색상 대비를 높이기 위해 사용됩니다.

**실습**:
Python을 사용하여 보색 관계를 시각화해보겠습니다.

```python
import matplotlib.pyplot as plt

# 보색 관계 예제
complementary_colors = {
    'Red': 'Green',
    'Blue': 'Orange',
    'Yellow': 'Purple'
}

# 보색 관계 시각화
fig, ax = plt.subplots(1, len(complementary_colors), figsize=(15, 2))
for idx, (color, comp_color) in enumerate(complementary_colors.items()):
    ax[idx].imshow([[plt.get_cmap('hsv')(i) for i in range(256)]])
    ax[idx].set_title(f'{color} - {comp_color}')
    ax[idx].axis('off')

plt.show()
```

이 코드는 보색 관계를 시각적으로 보여줍니다.

#### 6.3 채도와 명도
**이론**:
- **채도의 개념**: 채도는 색상의 진하기를 의미합니다. 채도가 높을수록 색상이 선명해지고, 낮을수록 회색에 가까워집니다.
- **명도의 개념**: 명도는 색상의 밝기를 의미합니다. 명도가 높을수록 밝아지고, 낮을수록 어두워집니다.

**실습**:
Python을 사용하여 다양한 채도와 명도를 시각화해보겠습니다.

```python
import matplotlib.pyplot as plt

# 채도와 명도 예제
saturation_levels = [0.2, 0.4, 0.6, 0.8, 1.0]
brightness_levels = [0.2, 0.4, 0.6, 0.8, 1.0]

# 채도와 명도 시각화
fig, ax = plt.subplots(len(saturation_levels), len(brightness_levels), figsize=(10, 10))
for i, saturation in enumerate(saturation_levels):
    for j, brightness in enumerate(brightness_levels):
        color = plt.get_cmap('hsv')(i / len(saturation_levels))
        adjusted_color = [channel * saturation for channel in color]
        adjusted_color = [channel * brightness for channel in adjusted_color

]
        ax[i, j].imshow([[adjusted_color]])
        ax[i, j].axis('off')
        ax[i, j].set_title(f'S: {saturation}, B: {brightness}')

plt.show()
```

이 코드는 다양한 채도와 명도의 색상을 시각적으로 보여줍니다.

