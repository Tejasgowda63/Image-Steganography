# Stego-Based Authentication System

This project implements a steganography-based authentication system that enhances security by integrating user credentials with stego images for the login process.

![Screenshot 2024-11-24 134901](https://github.com/user-attachments/assets/a48b43a0-8214-484c-9793-6c3460ffe180)

## Features

### Signup Process
1. **User Inputs**:
   - Name
   - Username
   - Profile Image
   - Password
   - Confirm Password
2. **Key Operations**:
   - Image analysis for embedding credentials using steganography.
   - Password encryption.
   - Password matching validation.

### Signup System Architecture
<img src="https://github.com/user-attachments/assets/9d85c16b-d687-45d5-bcc8-ccffbd754b73" alt="description" width="400" height="600">

### Login Process
1. **User Inputs**:
   - Username
   - Password
   - Stego Image
2. **Key Operations**:
   - Extraction of credentials from the stego image.
   - Validation of extracted credentials against user-provided input.
   - Secure login to the dashboard.

### Login System Architecture
<img src="https://github.com/user-attachments/assets/ddc9d844-87ee-469b-a887-cf899920678a" alt="description" width="400" height="400">

### Login Page
![Login System Architecture](https://github.com/user-attachments/assets/83150705-9cf0-4a18-9358-cbd3eedc8ba2)

### Encryption
1. **Encryption**:
   - Upload the image to encrypt.
   - Enter the text to encrypt into the image.
   - Encrypt text messages into image.
  
![encrypt](https://github.com/user-attachments/assets/66859ac2-ce6d-4dbb-987c-cd93dc90ccaa)

### Decryption
1. **Decryption**:
   - Upload the image to decrypt.
   - Decrypt text messages from image.

![Decrypt](https://github.com/user-attachments/assets/7bd17f2e-fa43-435e-82ba-cae029a7999a)

## Project Workflow

### Signup Flow
- **Input Collection**: Users provide their name, username, image, password, and confirm their password.
- **Image Processing**: The profile image is processed using steganography to embed the credentials securely.
- **Password Encryption**: User passwords are encrypted before being stored in the database.
- **Validation**: The system ensures the password and confirm password match.

### Login Flow
- **Input Collection**: Users enter their username, password, and upload their stego image.
- **Image Analysis**: The system extracts embedded credentials from the stego image.
- **Validation**: The extracted credentials are validated against the database, granting access upon successful matching.

## Technical Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django (Python)
- **Database**: SQLite
- **Security Mechanisms**:
  - Steganography for image embedding.
  - Hashing and encryption for passwords.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Tejasgowda63/Image-Steganography.git
   cd Image-Steganography
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Start the Server**:
   ```bash
   python manage.py runserver
   ```

5. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:8000`.

Working of Image Steganography using LSB Algoritham 

![Working of image steganography](https://github.com/user-attachments/assets/3e568902-7ac2-4eb4-85b5-8fff348b8d4b)


Model Error Rate with example images

![Validation of the Algoritham](https://github.com/user-attachments/assets/1aed3efe-d2d5-4071-b017-c3435f449603)

## Future Enhancements
- Implementing multi-factor authentication.
- Enhancing the stego-algorithm for better robustness.
- Adding support for cloud storage of stego images.

