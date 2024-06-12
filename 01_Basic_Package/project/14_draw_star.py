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
