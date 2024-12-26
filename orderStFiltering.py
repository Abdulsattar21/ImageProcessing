import cv2
from PIL import ImageFilter

def orderStFiltering(inimg, filterSize, typeOfStatistics):
  if (typeOfStatistics == 1):
    # Median filter
    outputImage = cv2.medianBlur(inimg,filterSize)
  elif (typeOfStatistics == 2):
    # Max filter
    outputImage = inimg.filter(ImageFilter.MaxFilter(size = filterSize))
  elif (typeOfStatistics == 3):
    # Mi filter
    outputImage = inimg.filter(ImageFilter.MinFilter(size = filterSize))
  return outputImage