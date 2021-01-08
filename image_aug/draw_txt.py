import numpy as np
from PIL import Image, ImageDraw

def pil_line(myFilePathPic_r, myFilePathDraw_r, my_str_ocr):
    # image = Image.open(myFilePathPic_r)
    with open(my_str_ocr, 'r') as f:
        polygons = f.readlines()

    with Image.open(myFilePathPic_r, mode='r') as image:
        draw = ImageDraw.Draw(image)

        for polygon in polygons:
            # print(np.array(word['points']))
            # print('polygon:', type(polygon))
            x = list()
            y = list()
            points = polygon.split(',')
            points = [float(point) for point in points]
            for index in range(4):
                x.append(points[::2])
                y.append(points[1::2])
            # print('x:', x)
        #     print('y:', y)
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
    image_path = 'hua_711_001_rot270.jpg'
    txt_path = image_path.replace('_rot270.jpg', '_rot270.txt')
    image_draw_path = 'hua_711_001_rot270_draw.jpg'
    pil_line(image_path, image_draw_path, txt_path)
