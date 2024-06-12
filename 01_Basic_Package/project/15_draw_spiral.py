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
