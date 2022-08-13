import base64
import io
import cv2
from imageio import imread
import matplotlib.pyplot as plt
import numpy as np

filename = "/home/ubuntu/testImageBytes"
with open(filename, "rb") as fid:
    data = fid.read()

b64_string = data

# reconstruct image as an numpy array
img = imread(io.BytesIO(b64_string))
height, width, channels = img.shape
print(height)
print(width)
print(channels)

# show image
plt.figure()
plt.imshow(img, cmap="gray")

# finally convert RGB image to BGR for opencv
# and save result
cv2_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imwrite("reconstructed2.jpg", cv2_img)
plt.show()
