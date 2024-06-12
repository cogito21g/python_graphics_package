import matplotlib.pyplot as plt

# RGB 색상 예제
colors = {
    'Red': [255, 0, 0],
    'Green': [0, 255, 0],
    'Blue': [0, 0, 255],
    'Yellow': [255, 255, 0],
    'Cyan': [0, 255, 255],
    'Magenta': [255, 0, 255]
}

# 색상 출력
fig, ax = plt.subplots(1, len(colors), figsize=(15, 2))
for idx, (name, rgb) in enumerate(colors.items()):
    ax[idx].imshow([[rgb]])
    ax[idx].set_title(name)
    ax[idx].axis('off')

plt.show()
