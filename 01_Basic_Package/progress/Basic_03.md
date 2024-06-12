좋습니다! 그래픽스를 한 단계씩 차근차근 배워봅시다. 첫 번째 단계로, **Matplotlib**를 사용한 2D 그래픽스부터 시작하겠습니다. 이 라이브러리는 데이터 시각화에 널리 사용되며, 간단한 플롯부터 복잡한 그래프까지 다양하게 그릴 수 있습니다.

### 1단계: Matplotlib 기본 사용법

#### 목표
- Matplotlib 설치 및 기본 사용법 익히기
- 간단한 선 그래프 그리기
- 그래프의 구성 요소 익히기

#### 이론
Matplotlib은 데이터 시각화를 위한 강력한 라이브러리로, 다양한 유형의 그래프를 그릴 수 있습니다. 기본적인 구성 요소는 다음과 같습니다:

- **Figure**: 모든 그래프를 포함하는 최상위 객체입니다.
- **Axes**: 실제 그래프가 그려지는 부분입니다. 하나의 Figure에 여러 개의 Axes를 가질 수 있습니다.
- **Axis**: x축과 y축을 의미합니다.
- **Plot**: 실제 데이터를 시각화하는 선, 막대, 점 등의 요소입니다.

이제 이론을 바탕으로 간단한 그래프를 그려보겠습니다.

#### Matplotlib 설치
먼저, Matplotlib을 설치해야 합니다. 아래 명령어를 사용하여 설치합니다.

```bash
pip install matplotlib
```

#### 간단한 선 그래프 그리기
Matplotlib을 사용하여 간단한 선 그래프를 그리는 방법을 배워보겠습니다.

##### 예제 코드
아래 코드를 따라 해 보세요.

```python
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


# Figure와 Axes 생성
fig, ax = plt.subplots()

# 선 그래프 그리기
ax.plot(x, y, label='Sine Wave')

# 그래프 구성 요소 설정
ax.set_xlabel('X-axis')  # x축 레이블
ax.set_ylabel('Y-axis')  # y축 레이블
ax.set_title('Sine Wave')  # 그래프 제목
ax.legend()  # 범례 추가
ax.grid(True)  # 그리드 표시

# 그래프 보여주기
plt.show()

```

##### 코드 설명
- `import matplotlib.pyplot as plt`: Matplotlib의 pyplot 모듈을 plt라는 이름으로 불러옵니다.
- `import numpy as np`: 수학 함수 및 배열 연산을 위한 numpy 라이브러리를 불러옵니다.
- `np.linspace(0, 10, 100)`: 0에서 10까지 100개의 균등한 데이터를 생성합니다.
- `plt.plot(x, y)`: x와 y 데이터를 사용하여 선 그래프를 그립니다.
- `plt.xlabel('X-axis')`: x축 레이블을 설정합니다.
- `plt.ylabel('Y-axis')`: y축 레이블을 설정합니다.
- `plt.title('Sine Wave')`: 그래프 제목을 설정합니다.
- `plt.grid(True)`: 그리드를 표시합니다.
- `plt.show()`: 그래프를 화면에 보여줍니다.

- `fig, ax = plt.subplots()`: Figure와 Axes 객체를 생성합니다.
- `ax.plot(x, y, label='Sine Wave')`: x와 y 데이터를 사용하여 선 그래프를 그리고, 범례 레이블을 설정합니다.
- `ax.set_xlabel('X-axis')`: x축 레이블을 설정합니다.
- `ax.set_ylabel('Y-axis')`: y축 레이블을 설정합니다.
- `ax.set_title('Sine Wave')`: 그래프 제목을 설정합니다.
- `ax.legend()`: 범례를 추가합니다.
- `ax.grid(True)`: 그리드를 표시합니다.
- `plt.show()`: 그래프를 화면에 보여줍니다.

#### 연습 과제
1. 위 코드를 실행하여 결과를 확인해보세요.
2. `np.cos(x)` 데이터를 사용하여 코사인 파형을 추가해보세요. (힌트: `ax.plot(x, np.cos(x), label='Cosine Wave')`를 추가하면 됩니다.)
3. 두 개의 그래프를 하나의 플롯에 동시에 그려보세요 (힌트: `plt.plot()`을 두 번 사용하면 됩니다).
4. 그래프의 색상과 선 스타일을 변경해보세요. (힌트: `ax.plot(x, y, color='r', linestyle='--', label='Sine Wave')`와 같이 설정할 수 있습니다.)

이제 이론과 실습을 통해 기본적인 Matplotlib 사용법을 익혔습니다. 다음 단계로 나아가면서 더 복잡한 그래프와 추가 기능을 배워보겠습니다. 