# 用来检验生成的json文件和原始画的标注json文件是否有较大出入
# date：2020/11/03
# author: zyw

import json
import numpy as np
from PIL import Image, ImageDraw

def pil_line(myFilePathPic_r, myFilePathDraw_r, my_str_ocr):
    # image = Image.open(myFilePathPic_r)

    with Image.open(myFilePathPic_r, mode='r') as image:
        draw = ImageDraw.Draw(image)

        for word in my_str_ocr['shapes']:
            # print(np.array(word['points']))
            print(word['points'])
            x = list()
            y = list()
            points = word['points']
            for index in range(4):
                x.append(points[index][0])
                y.append(points[index][1])
            print('x:', x)
            print('y:', y)
            left = np.min(x)
            right = np.max(x)
            top = np.min(y)
            lower = np.max(y)
            width = right - left
            print('width:', width)
            height = lower - top
            print('height:', height)

            # draw.line((100, 100, 1000, 1000 / 2), 'red')

            if left > 0 and top > 0 and width > 0 and height > 0:
                # 上
                draw.line((left, top, left + width, top), fill='cyan')
                # 下
                draw.line((left, top + height, left + width, top + height), fill='cyan')

                # 左
                draw.line((left, top, left, top + height), fill='cyan')

                # 右
                draw.line((left + width, top, left + width, top + height), fill='cyan')

        image.save(myFilePathDraw_r)


if __name__ == '__main__':
    myDirPath = r'./raw_data/'
    myFilePathPic = myDirPath + r'hua_711_tt.jpg'
    myFilePathJson = myDirPath + r'hua_711_tt.json'
    myFilePathDraw = myDirPath + r'hua_711_tt_pil.jpg'

    for num in range(0, 1):
        myFilePathPic_r = myFilePathPic.replace("tt", str(num+1).rjust(3, '0'))[:]
        myFilePathJson_r = myFilePathJson.replace("tt", str(num+1).rjust(3, '0'))[:]
        myFilePathDraw_r = myFilePathDraw.replace("tt", str(num+1).rjust(3, '0'))[:]

        '''
        读取json
        '''
        my_jsonfile = open(myFilePathJson_r, 'r')
        my_str_ocr = json.load(my_jsonfile)

        # my_dict_ocr = json.loads(my_str_ocr)

        pil_line(myFilePathPic_r, myFilePathDraw_r, my_str_ocr)

