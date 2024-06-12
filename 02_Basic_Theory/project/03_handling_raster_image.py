from PIL import Image, ImageFilter

# 이미지 열기
img = Image.open('./assets/image1.png')

# 이미지 표시
img.show()

# 이미지 크기 조절
resized_img = img.resize((100, 100))

# 이미지 저장 및 표시
resized_img.save('./result/resized_image.jpg')
resized_img.show()

# 블러 필터 적용
blurred_img = img.filter(ImageFilter.BLUR)

# 이미지 저장 및 표시
blurred_img.save('./result/blurred_image.png')
blurred_img.show()

