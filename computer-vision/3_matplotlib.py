import cv2
from matplotlib import pyplot as plt

print("hello")

img = cv2.imread('./string-theory.jpg')
# cv2.imshow('String Theory', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('String Theory')
plt.show()


