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
