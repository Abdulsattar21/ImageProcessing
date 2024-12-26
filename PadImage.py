import cv2

def padImage (inimg, nrp, ncp):
  height, width = inimg.shape[:2]
  top = int((nrp - height) / 2)
  bottom = int((nrp - height) / 2)
  left = int((ncp - width) / 2)
  right = int((ncp - width) / 2)
  paddedImage = cv2.copyMakeBorder(inimg, top , bottom, left, right, cv2.BORDER_CONSTANT)
  return paddedImage


