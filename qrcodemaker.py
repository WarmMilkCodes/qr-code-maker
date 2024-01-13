import qrcode
from PIL import Image
import time
import re

def sanitize_filename(name):
    """ Sanitize the file name by keeping only alphanumeric characters and underscores. """
    return re.sub(r'\W+', '', name)

def create_custom_qr(url, file_name):
    # Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image with a transparent background
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # Customizations can be added here using PIL, like adding a logo or changing shapes

    # Save the QR Code
    img.save(file_name)
    print(f'Your QR code has been saved as {file_name}')

# Input from user
custom_url = input("Enter URL:  ")
sanitized_url = sanitize_filename(custom_url)
file_name = sanitized_url + '.png'

# Create and save the custom QR code
create_custom_qr(custom_url, file_name)
