import os
import glob
import shutil
import random
import numpy as np

if __name__ == '__main__':
    base_path = 'F:/laibo/data_hua_711_tu/train_img/'
    image_path = glob.glob(base_path + '*.jpg')
    out_image_path = base_path.replace('train_img', 'test_img')
    out_txt_path = base_path.replace('train_img', 'test_txt')

    # image_path = random.shuffle(image_path)
    # print('imagea_path:', image_path)
    test_image_path = random.sample(image_path, 50)
    # print('test_image_path:', type(test_image_path))

    if not os.path.exists(out_image_path):
        os.mkdir(out_image_path)

    if not os.path.exists(out_txt_path):
        os.mkdir(out_txt_path)

    for test_image in test_image_path:
        # print(len(test_image))
        test_txt = test_image.replace('train_img', 'train_txt').replace('.jpg', '.txt')
        # print('test_txt:', test_txt)
        shutil.move(test_image, test_image.replace('train_img', 'test_img'))
        shutil.move(test_txt, test_txt.replace('train_txt', 'test_txt'))
