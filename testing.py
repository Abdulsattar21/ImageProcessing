import cv2
from PIL import Image
from matplotlib import pyplot as plt
from PadImage import padImage
from cropImage import cropImage
from filterImage import filterImage
from orderStFiltering import orderStFiltering
from unsharoMasking import unsharpMasking


# Read the image into the python environment
img = cv2. imread('PEPPERS.TIF')
im1 = Image.open(r"PEPPERS.TIF")

outimgPad = padImage(img, 630, 790)
outimgcrop = cropImage(img, [0, 300, 0, 250])
outimgfilter = filterImage(img, "gauss")
outimgorder = orderStFiltering(img, 3, 1)
outimgUnSharp = unsharpMasking(img, 2)

# Displaying the image
cv2.imshow('Padded Image', outimgPad)
plt.subplot(122),plt.imshow(outimgfilter),plt.title('Filtered Image')
plt.show()
cv2.imshow('Cropped Image', outimgcrop)
cv2.imshow('Unsharp Masking Image', outimgUnSharp)
cv2.imshow('order Image', outimgorder)
#outimgfilter.show()
cv2.waitKey(0)
cv2.destroyAllWindows()