좋습니다! 이제 6단계로 넘어가서 **Turtle 그래픽스**를 공부해보겠습니다. Turtle 모듈은 Python의 표준 라이브러리로, 간단한 그래픽스를 그리기 위한 도구로 많이 사용됩니다. 주로 교육 목적으로 사용되며, 기본적인 도형을 쉽게 그릴 수 있습니다.

### 6단계: Turtle 그래픽스

#### 이론
Turtle 모듈은 다음과 같은 기본 개념을 포함합니다:
- **Turtle 객체**: 그림을 그리는 데 사용되는 거북이 객체
- **캔버스**: Turtle 객체가 그림을 그리는 화면
- **명령어**: Turtle 객체를 이동시키거나, 도형을 그리는 데 사용되는 다양한 명령어

#### 실습: Turtle 기본 사용법

##### 예제 코드: 간단한 도형 그리기
아래 코드는 Turtle을 사용하여 간단한 사각형을 그리는 예제입니다.

```python
import turtle

# 캔버스 설정
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Turtle Graphics Example")

# Turtle 객체 생성
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")

# 사각형 그리기
for _ in range(4):
    t.forward(100)  # 100 픽셀 앞으로 이동
    t.right(90)    # 오른쪽으로 90도 회전

# 종료
turtle.done()
```

##### 코드 설명
- `screen = turtle.Screen()`: 캔버스를 설정합니다.
- `t = turtle.Turtle()`: Turtle 객체를 생성합니다.
- `t.shape("turtle")`: 거북이 모양으로 설정합니다.
- `t.color("blue")`: 거북이의 색상을 파란색으로 설정합니다.
- `for _ in range(4)`: 사각형을 그리기 위해 4번 반복합니다.
- `t.forward(100)`: 100 픽셀 앞으로 이동합니다.
- `t.right(90)`: 오른쪽으로 90도 회전합니다.
- `turtle.done()`: 그래픽을 유지합니다.

#### 실습 1: 다양한 도형 그리기

##### 예제 코드: 삼각형 그리기
아래 코드는 Turtle을 사용하여 삼각형을 그리는 예제입니다.

```python
import turtle

# 캔버스 설정
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Turtle Graphics Example")

# Turtle 객체 생성
t = turtle.Turtle()
t.shape("turtle")
t.color("green")

# 삼각형 그리기
for _ in range(3):
    t.forward(100)
    t.left(120)

# 종료
turtle.done()
```

##### 코드 설명
- `t.left(120)`: 왼쪽으로 120도 회전합니다. 삼각형을 그리기 위해 120도로 회전합니다.

#### 실습 2: 색상과 선 두께 설정

##### 예제 코드: 색상과 선 두께 설정
아래 코드는 Turtle을 사용하여 색상과 선 두께를 설정하여 별을 그리는 예제입니다.

```python
import turtle

# 캔버스 설정
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Turtle Graphics Example")

# Turtle 객체 생성
t = turtle.Turtle()
t.shape("turtle")
t.color("purple")
t.pensize(3)  # 선 두께 설정

# 별 그리기
for _ in range(5):
    t.forward(100)
    t.right(144)

# 종료
turtle.done()
```

##### 코드 설명
- `t.pensize(3)`: 선의 두께를 3으로 설정합니다.
- `t.right(144)`: 오른쪽으로 144도 회전합니다. 별을 그리기 위해 144도로 회전합니다.

#### 실습 과제
1. 위 예제 코드를 실행하여 다양한 도형을 그려보세요.
2. 원과 다각형을 그려보세요.
3. 다른 색상과 선 두께를 설정해보세요.
4. 복잡한 도형(예: 나선형)을 그려보세요.

아래 코드는 나선형을 그리는 예제입니다.

```python
import turtle

# 캔버스 설정
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Turtle Graphics Example")

# Turtle 객체 생성
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")

# 나선형 그리기
for i in range(100):
    t.forward(i * 2)
    t.right(45)

# 종료
turtle.done()
```

이제 Turtle 그래픽스의 기본 사용법을 익혔습니다. 다음 단계에서는 Pillow를 사용한 이미지 처리를 배워보겠습니다. 