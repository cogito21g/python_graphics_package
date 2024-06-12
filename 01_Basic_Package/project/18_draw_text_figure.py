from PIL import Image, ImageDraw, ImageFont

# 이미지 로드
image = Image.open('./assets/image1.png')
draw = ImageDraw.Draw(image)

# 폰트 설정 (TrueType 폰트 파일 경로 필요)
font = ImageFont.truetype("./assets/arial.ttf", 40)

# 텍스트 그리기
draw.text((100, 100), "Hello, Pillow!", fill="white", font=font)

# 사각형 그리기
draw.rectangle((200, 200, 300, 300), outline="red", width=5)

# 이미지 저장
image.save('./assets/drawn_image.png')
