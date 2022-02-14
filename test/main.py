# 导入包
# 导入OpenCV库
import cv2
from hyperlpr import *


def spotImg(path):
    # 读入图片
    image = cv2.imread(path)
    # 识别结果
    result = HyperLPR_plate_recognition(image)
    print(result)
    for i, r in enumerate(result):
        txt, confidence, rect = r
        ''' 
            cx: 中心点x
            xy: 中心点y
            w:  宽度
            h:  高度
        '''
        cx, cy, w, h = rect
        print(cx, cy, w, h)

spotImg("demo.jpg")
