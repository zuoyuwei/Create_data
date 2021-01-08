# data:2020/05/31
# update:2020/10/12
# author:zuo
# purpose:save preprocess into labelme format

from sys import argv

'''图像转为序列化的数据并存储为json文件'''

from base64 import b64encode
from json import dumps
import os
import glob
import cv2
import json

# class img_to_json(object):
#     """
#         这个类是用来将图像数据转化成json文件的，方便下一步的处理。主要是为了获取
#         图像的字符串信息
#     """
#     def __init__(self, process_img_path="img_0.jpg",
#                  img_type=".jpg",
#                  out_file_path="img_0.json",
#                  out_file_type=".json"):
#         """
#         :param process_img_path: 待处理图片的路径
#         :param img_type: 待处理图片的类型
#         :param out_file_path: 输出文件的路径
#         :param out_file_type: 输出文件的类型
#         使用glob从指定路径中获取所有的img_type的图片
#         """
#         # self.process_img = glob.glob(process_img_path + "/*" + img_type)
#         self.process_img = process_img_path
#         # self.out_file = out_file_path
#         self.out_file = out_file_path
#         self.out_file_type = out_file_type
#         self.img_type = img_type
#
#     def en_decode(self):
#         """
#         对获取的图像数据进行编码，解码后并存储到指定文件，保存为json文件
#         :return: null
#         """
#         print('-' * 30)
#         print("运行 Encode--->Decode\nStart process.....\nPlease wait a moment")
#         print('-' * 30)
#         """
#         Start process.....   Please wait a moment
#         """
#         """filepath, shotname, extension, tempfilename:目标文件所在路径，文件名，文件后缀,文件名+文件后缀"""
#         def capture_file_info(filename):
#             (filepath, tempfilename) = os.path.split(filename)
#             (shotname, extension) = os.path.splitext(tempfilename)
#             return filepath, shotname, extension, tempfilename
#
#         ENCODING = 'utf-8'  # 编码形式为utf-8
#
#         # SCRIPT_NAME, IMAGE_NAME, JSON_NAME = argv  # 获得文件名参数
#
#         img = [self.process_img]  # 所有图片的形成的列表信息
#         # img_number = capture_file_info(img)[1]
#         # imgs = sorted(img,key=lambda )
#
#         out_file_path = self.out_file
#
#         # imgtype = self.img_type
#
#         out_file_type = self.out_file_type
#         print("待处理的图片的数量:",len(img))
#         if len(img) == 0:
#             print("There was nothing under the specified path.")
#             return 0
#         for imgname in img:
#             # midname = imgname[imgname.rindex("\\"):imgname.rindex("." + imgtype)]
#             # midname = capture_file_info(imgname)[1]   # midname:图片的名称，不带后缀名
#             IMAGE_NAME = imgname
#             # IMAGE_NAME = midname + imgtype
#             # JSON_NAME = midname + out_file_type
#             JSON_NAME = out_file_path
#             # 读取二进制图片，获得原始字节码，注意 'rb'
#             with open(IMAGE_NAME, 'rb') as jpg_file:
#                 byte_content = jpg_file.read()
#             # 把原始字节码编码成 base64 字节码
#             base64_bytes = b64encode(byte_content)
#             # 将 base64 字节码解码成 utf-8 格式的字符串
#             base64_string = base64_bytes.decode(ENCODING)
#             # 用字典的形式保存数据
#             """raw_data:用来存放加入特性的数据，img_raw_data:用来存放不加入特性的数据，只有图片的字符串数据"""
#             raw_data = {}
#             raw_data["version"] = '4.2.10'
#             raw_data["imageData"] = base64_string
#             # img_raw_data = {}
#             # img_raw_data = base64_string
#             # 将字典变成 json 格式，indent =2:表示缩进为 2 个空格
#             json_data = dumps(raw_data)
#             # json_img_data = dumps(img_raw_data)
#             # 将 json 格式的数据保存到指定的文件中
#             with open(out_file_path, 'w') as json_file:
#                 json_file.write(json_data)

# -*- coding:utf-8 -*-

# json_file = './1.json'

# data = json.load(open(json_file))

# 参考labelme的json格式重新生成json文件，
# 便可以使用labelme的接口解析数据

def dict_json(imageData,shapes,imagePath,fillColor=None,lineColor=None):
    '''

    :param imageData: str
    :param shapes: list
    :param imagePath: str
    :param fillColor: list
    :param lineColor: list
    :return: dict
    '''
    return {"imageData":imageData,"shapes":shapes,"fillColor":fillColor,
            'imagePath':imagePath,'lineColor':lineColor}

def dict_shapes(points,label,fill_color=None,line_color=None):
    return {'points':points,'fill_color':fill_color,'label':label,'line_color':line_color}

# 注以下都是虚拟数据，仅为了说明问题
# imageData="image data"
# shapes=[]
# # 第一个对象
# points=[[10,10],[120,10],[120,120],[10,120]] # 数据模拟
# # fill_color=null
# label='cat_1'
# # line_color=null
# shapes.append(dict_shapes(points,label))
#
# # 第二个对象
# points=[[150,200],[200,200],[200,250],[150,250]] # 数据模拟
# label='cat_2'
# shapes.append(dict_shapes(points,label))
#
# fillColor=[255,0,0,128]
#
# imagePath='E:/TextLocal/CHINESE-OCR-master/img_0.jpg'
#
# with open(imagePath, 'rb') as jpg_file:
#     byte_content = jpg_file.read()
#     # 把原始字节码编码成 base64 字节码
#     base64_bytes = b64encode(byte_content)
#     # 将 base64 字节码解码成 utf-8 格式的字符串
#     base64_string = base64_bytes.decode('utf-8')
#
# imageData = base64_string
#
# lineColor=[0,255,0,128]
#
# data=dict_json(imageData,shapes,imagePath,fillColor,lineColor)
#
# # 写入json文件
# json_file = 'E:/TextLocal/CHINESE-OCR-master/img_0.json'
# json.dump(data,open(json_file,'w'))

if __name__ == '__main__':
    base_path = r'./raw_data/'
    files_path = glob.glob(base_path+'/*.txt')

    print('Total txt file number:',len(files_path))

    lineColor = [0, 255, 0, 128]

    fillColor = [255, 0, 0, 128]

    for file_path in files_path:
        imagePath = file_path[:-4]+'.jpg'
        # print('start read txt file:',file_path)
        shapes = []
        # print('start generate json....')
        with open(file_path,'r') as f:
            lines = f.readlines()
            # points = []
            for line in lines:
                print('line:', line)
                [x1,y1,x2,y2,x3,y3,x4,y4] = line.split(',')[:8]
                results = line.split(',')[8:]
                result = ','.join(results)
                points = []
                points.append([int(x1),int(y1)])
                points.append([int(x2), int(y2)])
                points.append([int(x3), int(y3)])
                points.append([int(x4), int(y4)])
                label = result
                shapes.append(dict_shapes(points,label))

        # image = cv2.imread(filename=imagePath, flags=0)
        # cv2.imshow('test1', image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        with open(imagePath, 'rb') as jpg_file:
            byte_content = jpg_file.read()
            # 把原始字节码编码成 base64 字节码
            base64_bytes = b64encode(byte_content)
            # 将 base64 字节码解码成 utf-8 格式的字符串
            base64_string = base64_bytes.decode('utf-8')

        imageData = base64_string

        data = dict_json(imageData, shapes, imagePath, fillColor, lineColor)

        # 写入json文件
        json_file = file_path[:-4]+'.json'
        json.dump(data, open(json_file, 'w'))

        print('end generate json!')
