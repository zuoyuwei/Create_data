import json
import glob
import numpy as np

def polygon_area(poly):
    '''
    compute area of a polygon
    :param poly:
    :return:
    '''
    edge = [
        (poly[1][0] - poly[0][0]) * (poly[1][1] + poly[0][1]),
        (poly[2][0] - poly[1][0]) * (poly[2][1] + poly[1][1]),
        (poly[3][0] - poly[2][0]) * (poly[3][1] + poly[2][1]),
        (poly[0][0] - poly[3][0]) * (poly[0][1] + poly[3][1])
    ]
    return np.sum(edge)/2.

def check_and_validate_polys(polys):
    '''
    check so that the text poly is in the same direction,
    and also filter some invalid polygons
    :param polys:
    :param tags:
    :return:
    '''
    if len(polys) == 0:
        return polys
    # polys[:, :, 0] = np.clip(polys[:, :, 0], 0, w-1)
    # polys[:, :, 1] = np.clip(polys[:, :, 1], 0, h-1)

    validated_polys = []
    for poly in polys:
        p_area = polygon_area(poly)
        if abs(p_area) < 1:
            # print poly
            print('invalid poly')
            continue
        if p_area > 0:
            print('poly in wrong direction')
            poly = poly[(0, 3, 2, 1), :]   # 改变四边形点坐标顺序到顺时针方向
        validated_polys.append(poly)
    return np.array(validated_polys)

if __name__ == '__main__':
    base_path = r'./raw_data/'
    json_paths = glob.glob(base_path + '/*.json')
    for json_path in json_paths:
        # ext = json_path.split('.')[-1].replace('txt')
        txt_path = json_path[:-5] + '_json.txt'
        with open(json_path, 'r') as f_json:
            content = json.load(f_json)
        with open(txt_path, 'w') as f_txt:
            polys = [poly['points'] for poly in content['shapes']]
            validate_polys = check_and_validate_polys(polys)
            # print('validate_polys:', len(validate_polys))
            for validate_poly in validate_polys:
                x1 = validate_poly[0][0]
                y1 = validate_poly[0][1]
                x2 = validate_poly[1][0]
                y2 = validate_poly[1][1]
                x3 = validate_poly[2][0]
                y3 = validate_poly[2][1]
                x4 = validate_poly[3][0]
                y4 = validate_poly[3][1]
                f_txt.write(str(x1)+','+str(y1)+','+str(x2)+','+str(y2)+','+
                            str(x3)+','+str(y3)+','+str(x4)+','+str(y4))
                f_txt.write('\n')