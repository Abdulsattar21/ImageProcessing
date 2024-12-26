import cv2
import numpy as np
img = cv2.imread('nice.jpg', 1)
cv2.imshow('Angel', img)
cv2.waitKey(0)
cv2.destroyAllWindows()




# Read the image into the python environment
img = cv2. imread('palace.jpg')
im1 = Image.open(r"palace.jpg")

paddedImg = padImage(img, 630, 790)
filterImg = filterImage(img, "gauss")
cropImg = cropImage(img, [0, 300, 0, 250])
filterImg = orderStFiltering(im1, 3, 2)
unsharpImg = unsharpMasking(img, 2)

# Displaying the image
cv2.imshow('Padded Image', paddedImg)
plt.subplot(122),plt.imshow(filterImg),plt.title('Filtered Image')
plt.show()
cv2.imshow('Cropped Image', cropImg)
cv2.imshow('Unsharp Masking Image', unsharpImg)
filterImg.show()

cv2.waitKey(0)
cv2.destroyAllWindows()