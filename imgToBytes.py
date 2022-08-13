import base64
import io
import cv2

filename = "/home/ubuntu/reconstructed2.jpg"

img = cv2.imread(filename)
height, width, channels = img.shape
print(height)
print(width)
print(channels)

retval, buffer = cv2.imencode('.jpg', img)
jpg_as_text = base64.b64encode(buffer)

print(jpg_as_text)

with open('/home/ubuntu/testImageBytes2', 'wb') as file_to_save:
    file_to_save.write(jpg_as_text)
