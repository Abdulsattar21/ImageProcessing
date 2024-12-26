import cv2

def filterImage (inimg, filter):
  if (filter == "blur"):
    output = cv2.blur(inimg,(5,5))
  if (filter == "gauss"):
    output = cv2.GaussianBlur(inimg,(5,5),0)
  if (filter == "bilateral"):
    output = cv2.bilateralFilter(inimg,9,75,75)
  if (filter == "laplacian"):
    output = cv2.Laplacian(inimg,cv2.CV_64F)
  return output
