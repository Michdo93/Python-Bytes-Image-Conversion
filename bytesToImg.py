import base64
import io
import cv2
from imageio import imread
import matplotlib.pyplot as plt
import numpy as np

with open('testImageBytes', 'r') as file:
    data = file.read()

data = eval(data)

# reconstruct image as an numpy array
img = imread(io.BytesIO(data))
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
