import cv2

def unsharpMasking(inimg, k):
  gaussian_3 = cv2.GaussianBlur(inimg, (0, 0), k)
  unsharpImg = cv2.addWeighted(inimg, 1.5, gaussian_3, -0.5, 0, inimg)
  return unsharpImg
