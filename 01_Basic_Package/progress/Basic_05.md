좋습니다! 이제 3단계로 넘어가서 **데이터 시각화**를 공부해보겠습니다. 이 단계에서는 다양한 플롯 유형을 사용하여 데이터를 시각화하는 방법을 배웁니다.

### 3단계: 데이터 시각화

#### 이론
데이터 시각화는 데이터를 시각적으로 표현하여 이해하기 쉽게 만드는 과정입니다. Matplotlib을 사용하여 다양한 유형의 플롯을 그릴 수 있습니다. 각 플롯 유형은 특정한 데이터 표현에 적합합니다.

- **막대 그래프 (Bar Plot)**: 범주형 데이터를 비교하는 데 사용됩니다.
- **히스토그램 (Histogram)**: 데이터의 분포를 보여줍니다.
- **산점도 (Scatter Plot)**: 두 변수 간의 관계를 나타냅니다.
- **상자 그림 (Box Plot)**: 데이터의 사분위수를 시각화하여 데이터의 분포와 이상치를 보여줍니다.

#### 실습 1: 막대 그래프 (Bar Plot)

##### 예제 코드
```python
import matplotlib.pyplot as plt

# 데이터 생성
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 24, 36, 40, 29]

# 막대 그래프 그리기
plt.bar(categories, values, color='skyblue')

# 그래프 구성 요소 설정
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot Example')
plt.show()
```

#### 실습 2: 히스토그램 (Histogram)

##### 예제 코드
```python
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
```

#### 실습 3: 산점도 (Scatter Plot)

##### 예제 코드
```python
import matplotlib.pyplot as plt
import numpy as np

# 데이터 생성
x = np.random.rand(100)
y = np.random.rand(100)

# 산점도 그리기
plt.scatter(x, y, color='green')

# 그래프 구성 요소 설정
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot Example')
plt.show()
```

#### 실습 4: 상자 그림 (Box Plot)

##### 예제 코드
```python
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
```

#### 실습 과제
1. 위 예제 코드를 실행하여 각 플롯의 결과를 확인해보세요.
2. 막대 그래프에서 막대의 색상을 변경하고, 막대 위에 값을 표시해보세요.
3. 히스토그램에서 bin의 수를 변경해보세요.
4. 산점도에서 점의 크기와 색상을 다르게 설정해보세요.
5. 상자 그림에서 각 상자의 색상을 다르게 설정해보세요.

아래는 막대 그래프에서 막대 위에 값을 표시하는 예제입니다.

```python
import matplotlib.pyplot as plt

# 데이터 생성
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 24, 36, 40, 29]

# 막대 그래프 그리기
bars = plt.bar(categories, values, color='skyblue')

# 막대 위에 값 표시
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom')

# 그래프 구성 요소 설정
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot with Values')
plt.show()
```

이제 3단계의 실습을 마치고 나면, 다양한 데이터 시각화 방법을 이해하고 활용할 수 있게 됩니다. 다음 단계로 넘어가서 Pygame을 사용한 상호작용형 그래픽스를 배워보겠습니다. 궁금한 점이나 추가 설명이 필요하면 언제든지 질문해 주세요!