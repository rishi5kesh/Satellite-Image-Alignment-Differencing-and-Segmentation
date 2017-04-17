import cv2
import numpy as np
import os

def refine():
	threshold_area=3000.0
	image_src = cv2.imread("appeared.jpg")
	im1 = cv2.imread('aligned_A.jpg')
	im2 = cv2.imread('aligned_B.jpg')
	

	gray = cv2.cvtColor(image_src, cv2.COLOR_BGR2GRAY)
	ret, gray = cv2.threshold(gray, 250, 255,0)

	image, contours, hierarchy = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	mask = np.zeros(image_src.shape, np.uint8)
	cnts = sorted(contours, key=cv2.contourArea)

	for c in cnts:
		area=cv2.contourArea(c)
		if area > threshold_area:
			cv2.drawContours(mask, [c], -1, (255,255,255), -1)
	

	cv2.imwrite("refined.jpg", mask)

	




