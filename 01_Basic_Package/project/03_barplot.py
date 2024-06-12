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
