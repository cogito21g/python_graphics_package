import matplotlib.pyplot as plt 

# 채도와 명도 예제
saturation_levels = [0.2, 0.4, 0.6, 0.8, 1.0]
brightness_levels = [0.2, 0.4, 0.6, 0.8, 1.0]

# 채도와 명도 시각화
fig, ax = plt.subplots(len(saturation_levels), len(brightness_levels), figsize=(10, 10))
for i, saturation in enumerate(saturation_levels):
    for j, brightness in enumerate(brightness_levels):
        color = plt.get_cmap('hsv')(i / len(saturation_levels))
        adjusted_color = [channel * saturation for channel in color]
        adjusted_color = [channel * brightness for channel in adjusted_color]
        ax[i, j].imshow([[adjusted_color]])
        ax[i, j].axis('off')
        ax[i, j].set_title(f'S: {saturation}, B: {brightness}')

plt.show()
