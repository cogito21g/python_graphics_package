좋습니다! 이제 2단계로 넘어가서 **Matplotlib 심화**를 공부해보겠습니다. 이 단계에서는 여러 개의 플롯을 그리는 방법과 서브플롯을 사용하는 방법을 배워보겠습니다.

### 2단계: Matplotlib 심화

#### 이론
1. **여러 개의 플롯 그리기**: 하나의 그래프에 여러 개의 플롯을 그리는 방법을 배웁니다.
2. **서브플롯**: 하나의 Figure에 여러 개의 Axes(서브플롯)를 배치하여 여러 그래프를 동시에 표시하는 방법을 배웁니다.
3. **스타일 설정**: 다양한 스타일과 색상을 사용하여 그래프의 시각적 요소를 개선하는 방법을 배웁니다.

#### 실습 1: 여러 개의 플롯 그리기

##### 예제 코드
아래 코드를 따라 해 보세요.

```python
import matplotlib.pyplot as plt
import numpy as np

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
```

##### 코드 설명
- `ax.plot(x, y1, label='Sine Wave', color='blue', linestyle='-')`: x와 y1 데이터를 사용하여 파란색 실선으로 사인 파형을 그립니다.
- `ax.plot(x, y2, label='Cosine Wave', color='red', linestyle='--')`: x와 y2 데이터를 사용하여 빨간색 점선으로 코사인 파형을 그립니다.

#### 실습 2: 서브플롯 사용하기

##### 예제 코드
이번에는 하나의 Figure에 여러 개의 서브플롯을 그리는 방법을 배워보겠습니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Figure와 서브플롯 생성
fig, (ax1, ax2) = plt.subplots(2, 1)

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

# 그래프 레이아웃 조정 및 보여주기
plt.tight_layout()
plt.show()
```

##### 코드 설명
- `fig, (ax1, ax2) = plt.subplots(2, 1)`: 2행 1열의 서브플롯을 생성하고 각각의 Axes 객체를 `ax1`, `ax2`로 설정합니다.
- `ax1.plot(x, y1, label='Sine Wave', color='blue', linestyle='-')`: 첫 번째 서브플롯에 사인 파형을 그립니다.
- `ax2.plot(x, y2, label='Cosine Wave', color='red', linestyle='--')`: 두 번째 서브플롯에 코사인 파형을 그립니다.
- `plt.tight_layout()`: 서브플롯 간의 간격을 자동으로 조정하여 레이아웃을 깔끔하게 만듭니다.

#### 실습 과제
1. 위 코드를 실행하여 결과를 확인해보세요.
2. 서브플롯을 2x2 배열로 변경하고, 다른 두 개의 그래프(예: 탄젠트, 코탄젠트)를 추가해보세요.
3. 각 서브플롯의 제목, 축 레이블, 스타일을 변경해보세요.

아래 코드는 2x2 배열의 서브플롯 예제입니다.

```python
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
```

이제 2단계 실습을 마치고 나면, 다음 단계로 넘어가서 데이터 시각화에 대해 배우도록 하겠습니다. 