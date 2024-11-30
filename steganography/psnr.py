import cv2
import numpy as np

def calculate_psnr(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr

def calculate_mse(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    return mse

# Example usage:
# Load the original and compressed images
original_image = cv2.imread('C:/Users/tejas/OneDrive/Desktop/steganography/original image/cricket.png')
compressed_image = cv2.imread('C:/Users/tejas/OneDrive/Desktop/steganography/f5 algoritham/cricket.png')


# Convert the images to grayscale if they are color images
original_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
compressed_gray = cv2.cvtColor(compressed_image, cv2.COLOR_BGR2RGB)

# Calculate PSNR
psnr_value = calculate_psnr(original_gray, compressed_gray)
print(f"PSNR value: {psnr_value} dB")

# Calculate MSE
mse_value = calculate_mse(original_gray, compressed_gray)
print(f"MSE value: {mse_value}")
