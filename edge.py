import numpy as np
import cv2
import os


def edge():
	refined = cv2.imread('refined.jpg',0)
	adjust = cv2.imread('adjust2.jpg',0)

	img1 = cv2.imread('aligned_A.jpg')
	img2 = cv2.imread('aligned_B.jpg')
	edges_refined = cv2.Canny(refined,100,200)
	edges_adjust = cv2.Canny(adjust,100,200)

	cv2.imwrite("edge_refined.jpg",edges_refined)
	cv2.imwrite("edge_adjusted.jpg",edges_adjust)



	joined1_refined = np.bitwise_or(img1, edges_refined[:,:,np.newaxis])
	joined2_refined = np.bitwise_or(img2, edges_refined[:,:,np.newaxis])

	joined1_adjust = np.bitwise_or(img1, edges_adjust[:,:,np.newaxis])
	joined2_adjust = np.bitwise_or(img2, edges_adjust[:,:,np.newaxis])

	cv2.imwrite('before_refined.jpg', joined1_refined)
	cv2.imwrite('after_refined.jpg', joined2_refined)

	cv2.imwrite('before_adjusted.jpg', joined1_adjust)
	cv2.imwrite('after_adjusted.jpg', joined2_adjust)


