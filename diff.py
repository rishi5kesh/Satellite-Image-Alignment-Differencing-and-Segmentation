#otsu's thresholding with Gaussian blur for noise reduction

import numpy as np 
import cv2


def findDiff():
	#get both images
	img1 = cv2.imread('aligned_A.jpg',0)
	img2 = cv2.imread('aligned_B.jpg',0)

	
	#cv2.imwrite('inter_A.jpg', img1)
	#cv2.imwrite('inter_B.jpg', img2)

	#get dimensions
	h, w = img2.shape

	#create a zeroed out image of same dimensions
	res1 = np.zeros((h,w,1), np.uint8)



	#find difference b/w 1st and 2nd image and vice versa
	disappear = cv2.subtract(img1, img2)
	appear = cv2.subtract(img2, img1)



	#set threshold values
	thresh = 70
	maxValue = 255
	 
	# apply gaussian blur and otsu's threshold
	blur1 = cv2.GaussianBlur(disappear,(5,5),0)
	ret,disappear = cv2.threshold(blur1,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	blur2 = cv2.GaussianBlur(appear,(5,5),0)
	ret,appear = cv2.threshold(blur2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

	#intermediate results
	#cv2.imwrite('disappear.jpg', disappear)
	cv2.imwrite('appeared.jpg', appear)

	#OR intermediate results
	#joined = cv2.add(disappear,appear)

	#write final results
	#cv2.imwrite('joined.jpg', joined)

	
	
	