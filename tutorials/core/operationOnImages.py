import sys

import numpy as np
import cv2 as cv

def main(argv):
	img = cv.imread("lena.jpg")

	cv.imshow("Input", img)

	cv.waitKey(0)
	cv.destroyAllWindows()
	return 0

if __name__ == "__main__":
	main(sys.argv[1:])