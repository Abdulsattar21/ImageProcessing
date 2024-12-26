import cv2
from PIL import Image, ImageFilter
from matplotlib import pyplot as plt

def cropImage (inimg, cropArray):
  # image[startY:endY, startX:endX]
  cropImg = inimg[cropArray[0]:cropArray[1], cropArray[2]:cropArray[3]]
  return cropImg
