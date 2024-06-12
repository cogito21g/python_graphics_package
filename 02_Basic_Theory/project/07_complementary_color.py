import matplotlib.pyplot as plt

# 보색 관계 예제
complementary_colors = {
    'Red': 'Green',
    'Blue': 'Orange',
    'Yellow': 'Purple'
}

# 보색 관계 시각화
fig, ax = plt.subplots(1, len(complementary_colors), figsize=(15, 2))
for idx, (color, comp_color) in enumerate(complementary_colors.items()):
    ax[idx].imshow([[plt.get_cmap('hsv')(i) for i in range(256)]])
    ax[idx].set_title(f'{color} - {comp_color}')
    ax[idx].axis('off')

plt.show()
