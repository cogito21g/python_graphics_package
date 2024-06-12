from PIL import Image

# 이미지 로드
image = Image.open('./assets/image1.png')

# 이미지 정보 출력
print(image.format)
print(image.size)
print(image.mode)

# 이미지 저장
image.save('./assets/image1.jpg')
