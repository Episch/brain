import cv2
import numpy as np
import sys
import os

baseImage = 'salmonscreen.jpg'
if len(sys.argv) > 1:
	baseImage = sys.argv[1]
path = 'weapons'
if len(sys.argv) > 2:
	path = sys.argv[2]
img_rgb = cv2.imread(baseImage)
for weapon in os.listdir(path):
	template = cv2.imread(os.path.join(path, weapon))
	w, h = template.shape[:-1]
	res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
	threshold = 0.75
	loc = np.where(res >= threshold)
	print("---- "+weapon+"\n")
	for pt in zip(*loc[::-1]):  # Switch collumns and rows
		print(pt)
		cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
		cv2.imwrite('result.png', img_rgb)
	print("Done!")
