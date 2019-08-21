import cv2
import numpy as np
im_origin = cv2.imread('D:\\Kaggle\\img_processing\\comcastbillmarkedup1.png')
im_gray = cv2.imread('D:\\Kaggle\\img_processing\\comcastbillmarkedup1.png', cv2.IMREAD_GRAYSCALE)
(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
print(np.array(im_origin).shape, np.array(im_gray).shape, np.array(im_bw).shape)
rgb_bw = np.repeat(np.array(im_bw)[..., np.newaxis], 3, -1)
print(rgb_bw.shape)
#, cv2.CV_LOAD_IMAGE_GRAYSCALE
cv2.imshow('origin', im_origin)
cv2.imshow('grey', im_gray)
cv2.imshow('binary', im_bw)
cv2.waitKey(0)