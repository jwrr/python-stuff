
import cv2
print(cv2.__version__)

img = cv2.imread('./string-theory.jpg')
cv2.imshow('String Theory', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

