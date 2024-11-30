import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_pixel_quality(image_path):
    image = cv2.imread(image_path)

    b, g, r = cv2.split(image)

    pixel_stats = {
        'Red': {'mean': np.mean(r), 'std': np.std(r)},
        'Green': {'mean': np.mean(g), 'std': np.std(g)},
        'Blue': {'mean': np.mean(b), 'std': np.std(b)}
    }

    return pixel_stats

def plot_pixel_quality_charts(pixel_stats):
    channels = list(pixel_stats.keys())
    means = [pixel_stats[channel]['mean'] for channel in channels]
    stds = [pixel_stats[channel]['std'] for channel in channels]

    # Plot mean pixel intensities
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(channels, means, marker='o', linestyle='-')
    plt.title('Mean Pixel Intensity in RGB Channels')
    plt.xlabel('Channels')
    plt.ylabel('Mean Intensity')

    # Plot standard deviation of pixel intensities
    plt.subplot(1, 2, 2)
    plt.plot(channels, stds, marker='o', linestyle='-')
    plt.title('Standard Deviation of Pixel Intensity in RGB Channels')
    plt.xlabel('Channels')
    plt.ylabel('Standard Deviation')

    plt.tight_layout()
    plt.show()

image_path = "C:/Users/tejas/OneDrive/Desktop/steganography/calulatorf5new.png"
pixel_stats = analyze_pixel_quality(image_path)
print("Pixel Intensity Statistics:")
for channel, stats in pixel_stats.items():
    print(f"{channel}: Mean = {stats['mean']}, Standard Deviation = {stats['std']}")

plot_pixel_quality_charts(pixel_stats)
