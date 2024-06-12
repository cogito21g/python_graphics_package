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
