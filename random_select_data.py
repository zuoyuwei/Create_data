# 随机从文件路径中选取一部分数据，存在另一文件路径中
import os
import glob
import shutil
import random

if __name__ == '__main__':
    raw_path = './raw_data/'
    out_path = './sample_data/'
    raw_image_path = glob.glob(raw_path + '*.jpg')
    raw_image_path = [os.path.basename(image_path) for image_path in raw_image_path]

    sample_image_path = random.sample(raw_image_path, 1)

    if not os.path.exists(out_path):
        os.mkdir(out_path)

    for in_image in sample_image_path:
        in_txt = in_image[:-3] + 'txt'
        shutil.move(raw_path + in_image, out_path + in_image)
        shutil.move(raw_path + in_txt, out_path + in_txt)
