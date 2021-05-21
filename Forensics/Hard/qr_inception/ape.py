import cv2
import numpy as np
img = cv2.imread("inception.png")
det = cv2.QRCodeDetector()
data, bbox, straight_qrcode = det.detectAndDecode(img)
#rv, pts = det.detectMulti(np.hstack([im, im])) 
print("multiple:", data) # True
# if there is a QR code
#if bbox is not None:
#    print(f"QRCode data:\n{data}")
#    # display the image with lines
#    # length of bounding box
#    n_lines = len(bbox)
#    for i in range(n_lines):
#        # draw all lines
#        point1 = tuple(bbox[i][0])
#        point2 = tuple(bbox[(i+1) % n_lines][0])
#        cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)