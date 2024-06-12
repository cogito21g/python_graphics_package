from PIL import Image

# 이미지 로드
image = Image.open('./assets/image1.png')

# 이미지 크기 조정
resized_image = image.resize((200, 200))
resized_image.save('./assets/resized_image.png')

# 이미지 자르기
cropped_image = image.crop((100, 100, 400, 400))
cropped_image.save('./assets/cropped_image.png')

# 이미지 회전
rotated_image = image.rotate(45)
rotated_image.save('./assets/rotated_image.png')
