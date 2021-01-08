# Date: 2020/11/4
# Author: zye
# coding: utf-8

import cv2
import math
import glob
import numpy as np
from PIL import Image

# box为0~1的值，为[ymin, xmin, ymax, xmax]
# landmarks为0~1的值，为多个[y0,x0,y1,x1,y2,x2......yn,xn]
def random_rotation(image, raw_polygons, angle):
    # 为随机旋转的角度-90~90度
    angle = angle
    theta = angle * (math.pi / 180.0)

    # 获取旋转的中心坐标
    # 也即是图像的中心坐标
    image_height = image.shape[0]
    # print('image_width:', image_width)
    image_width = image.shape[1]
    scaler = np.stack([image_width, image_height], axis=0)
    center = np.reshape(0.5 * scaler, [1, 2])

    # 求旋转矩阵
    rotation = np.stack([np.cos(theta), np.sin(theta), -np.sin(theta), np.cos(theta)], axis=0)
    rotation_matrix = np.reshape(rotation, [2, 2])

    # 旋转方框
    # ymin, xmin, ymax, xmax = box
    # h, w = ymax - ymin, xmax - xmin
    # box = np.stack([ymin, xmin, ymin, xmax, ymax, xmax, ymax, xmin], axis=0)
    # box = np.matmul(np.reshape(box, [4, 2]) * scaler - center, rotation_matrix) + center
    # box = box / scaler
    # y, x = box[:, 0], box[:, 1]
    # ymin, ymax = np.min(y), np.max(y)
    # xmin, xmax = np.min(x), np.max(x)
    # box = np.stack([ymin, xmin, ymax, xmax], axis=0)

    # 旋转坐标
    total_landmarks = []
    for landmarks in raw_polygons:
        landmarks = landmarks.strip().split(',')
        landmarks = [np.floor(float(landmark)) for landmark in landmarks]
        # print('landmarks:', landmarks)
        # print('scaler:', scaler)
        # landmarks = [landmarks[1], landmarks[0], landmarks[3], landmarks[2], landmarks[5], landmarks[4], landmarks[7], landmarks[6]]
        # print('landmarks:', landmarks)
        landmarks = np.reshape(landmarks, [4, 2])
        # print('center:', center)
        for i in range(len(landmarks)):
            if angle == 90:
                temp = landmarks[i][0]
                landmarks[i][0] = landmarks[i][1]
                landmarks[i][1] = image_width - temp

            elif angle == 180:
                landmarks[i][0] = image_width - landmarks[i][0]
                landmarks[i][1] = image_height - landmarks[i][1]

            elif angle == 270:
                temp = landmarks[i][0]
                landmarks[i][0] = image_height - landmarks[i][1]
                landmarks[i][1] = temp

            else:
                break

        # landmarks = np.matmul(landmarks - center, rotation_matrix) + center
        # print('landmarks:', landmarks)
        landmarks = [landmarks[0][0], landmarks[0][1], landmarks[1][0], landmarks[1][1], landmarks[2][0], landmarks[2][1], landmarks[3][0], landmarks[3][1]]

        # print('landmarks:', landmarks)
        total_landmarks.append(landmarks)
        # input('wait input........')

    # 旋转图像
    image = Image.fromarray(image)
    # im_rotate = image.rotate(angle)
    im_rotate = image.transpose(Image.ROTATE_270)
    im_rotate = np.array(im_rotate)
    return im_rotate, total_landmarks

if __name__ == '__main__':
    base_path = 'F:/laibo/data_hua_711_tu/train_img_and_txt'
    image_paths = glob.glob(base_path + '/*.jpg')
    for image_path in image_paths:
        raw_txt_path = image_path.replace('.jpg', '.txt')
        output_txt_path = image_path.replace('.jpg', '_rot270.txt')
        image_array = np.array(cv2.imread(image_path, cv2.COLOR_BGR2RGB))
        with open(raw_txt_path, 'r') as f:
            raw_polygons = f.readlines()
        image_rotate, total_landmarks = random_rotation(image=image_array, raw_polygons=raw_polygons, angle=90)
        cv2.imwrite(image_path.replace('.jpg', '_rot270.jpg'), image_rotate)
        with open(output_txt_path, 'w') as f_w:
            for index, rot_landmark in enumerate(total_landmarks):
                # print('rot_landmark:', len(rot_landmark))
                str_rot_landmark = [str(rot_landmark[i]) for i in range(len(rot_landmark))]
                str_rot_landmark = ','.join(str_rot_landmark)
                # print('str_rot_landmark:', str_rot_landmark)
                f_w.write(str_rot_landmark)
                if index == (len(total_landmarks) - 1):
                    continue
                f_w.write('\n')
