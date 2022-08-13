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
jpg_as_text = buffer.tobytes()

jpg_as_text = str(jpg_as_text)

text_file = open("testImageBytes2", "w")
 
#write string to file
text_file.write(jpg_as_text)
 
#close file
text_file.close()
