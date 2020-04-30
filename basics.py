import cv2

img = cv2.imread('vraj01.jpg',0)

cv2.imshow('image', img)
k = cv2.waitKey(0)

if k == 27:                                ## if escape is pressed move back
    cv2.destroyAllWindows()
elif k == ord('s'):                        ## if s is pressed image is saved
    cv2.imwrite('VDP01.png', img)
    cv2.destroyAllWindows()