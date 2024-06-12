from PIL import Image

# 이미지 로드
image = Image.open('./assets/image1.png')

# 흑백 변환
gray_image = image.convert('L')
gray_image.save('./assets/gray_image.png')
