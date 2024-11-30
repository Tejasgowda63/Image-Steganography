from PIL import Image
import numpy as np

def f5_embed(cover_path, secret_message, stego_path):
    cover = Image.open(cover_path)
    cover_array = np.array(cover)

    binary_message = ''.join(format(ord(char), '08b') for char in secret_message)

    binary_message += '1111111111111110'  

    binary_index = 0
    for i in range(len(cover_array)):
        for j in range(len(cover_array[0])):
            for k in range(3): 
                if binary_index < len(binary_message):
                    cover_array[i][j][k] &= ~1 
                    cover_array[i][j][k] |= int(binary_message[binary_index])
                    binary_index += 1
                else:
                    break
            if binary_index == len(binary_message):
                break
        if binary_index == len(binary_message):
            break

    stego = Image.fromarray(cover_array)
    stego.save(stego_path)

def f5_extract(stego_path):
    stego = Image.open(stego_path)
    stego_array = np.array(stego)

    extracted_message = ''
    binary_message = ''

    for i in range(len(stego_array)):
        for j in range(len(stego_array[0])):
            for k in range(3):  
                binary_message += str(stego_array[i][j][k] & 1)
            if binary_message[-16:] == '1111111111111110':
                extracted_message = binary_message[:-16]
                break
        if extracted_message:
            break

    message = ''.join([chr(int(extracted_message[i:i+8], 2)) for i in range(0, len(extracted_message), 8)])
    return message

cover_image_path = "C:/Users/tejas/OneDrive/Desktop/steganography/original image/cricket.png"
secret_message = "Hello, this is a secret message!"
stego_image_path = "C:/Users/tejas/OneDrive/Desktop/steganography/f5 algoritham/cricket.png"

f5_embed(cover_image_path, secret_message, stego_image_path)

extracted_message = f5_extract(stego_image_path)
print("Extracted Message:", str(extracted_message))
