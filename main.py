# 解决 pycharm提示Cannot find reference 'xxx' in __init__.py:https://blog.csdn.net/yuer5531/article/details/121284454
import cv2
import htamd
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
handt = htamd.ht()

while 1:
    success, img = cap.read()
    img = handt.findhand(img, show_lines=True)
    lml = handt.findpos()
    if len(lml) != 0:
        print(lml[8])

    cv2.imshow("Box", img)
    cv2.waitKey(1)
