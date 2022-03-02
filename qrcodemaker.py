import qrcode
import time

custom_qr = input("Please enter URL:  ")

img = qrcode.make(custom_qr)
print('Making QR code and saving to directory...')
file_name_no_period = custom_qr.replace('.','')

file_name = file_name_no_period + '.jpg'
time.sleep(5)
img.save(file_name)
print('Your QR code has been saved.')
