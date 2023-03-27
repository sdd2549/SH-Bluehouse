import cv2
import numpy as np

# 이미지를 불러옵니다.
img = cv2.imread('./data/3333.tif')

# 이미지를 회색조로 변경합니다.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 가우시안 블러(흐리게) 처리합니다.
gray = cv2.GaussianBlur(gray, (3, 3), 0)

# 엣지 검출을 수행합니다.
edges = cv2.Canny(gray, 100, 200)

# Bilateral Filtering을 수행합니다.
cartoon = cv2.bilateralFilter(img, 5, 50, 50)

# 검출한 엣지와 Bilateral Filtering을 적용한 이미지를 합성합니다.
for i in range(3):
    cartoon[:, :, i][edges != 0] = np.mean(cartoon[:, :, i])

# 결과를 출력합니다.
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
