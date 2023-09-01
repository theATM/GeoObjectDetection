import DotaTools.dota_utils as util
import os
import cv2
import json

wordname_2 = ['airport', 'helicopter', 'oiltank', 'plane', 'warship']

def DOTA2COCO(srcpath_img,srcpath_labels, destfile, end = '.png'):
    imageparent = srcpath_img# os.path.join(srcpath, 'images')
    labelparent = srcpath_labels#os.path.join(srcpath, 'labels')

    data_dict = {}
    info = {'contributor': 'captain group',
           'data_created': '2018',
           'description': 'This is trimmed 2.0 version of DOTA dataset.',
           'url': 'http://captain.whu.edu.cn/DOTAweb/',
           'version': '2.0',
           'year': 2018}
    data_dict['info'] = info
    data_dict['categories'] = []
    data_dict['images'] = []
    data_dict['annotations'] = []
    for idex, name in enumerate(wordname_2):
        single_cat = {'id': idex + 1, 'name': name, 'supercategory': 'objects'}
        data_dict['categories'].append(single_cat)

    inst_count = 1
    image_id = 1
    with open(destfile, 'w') as f_out:
        filenames = util.GetFileFromThisRootDir(labelparent)
        for file in filenames:
            basename = util.custombasename(file)
            # image_id = int(basename[1:])

            imagepath = os.path.join(imageparent, basename + end)
            img = cv2.imread(imagepath)
            height, width, c = img.shape

            single_image = {}
            single_image['file_name'] = basename + end
            single_image['id'] = image_id
            single_image['width'] = width
            single_image['height'] = height
            data_dict['images'].append(single_image)

            # annotations
            objects = util.parse_dota_poly2(file)
            for obj in objects:
                single_obj = {}
                single_obj['area'] = obj['area']
                single_obj['category_id'] = wordname_2.index(obj['name']) + 1
                single_obj['segmentation'] = []
                single_obj['segmentation'].append(obj['poly'])
                single_obj['iscrowd'] = 0
                xmin, ymin, xmax, ymax = min(obj['poly'][0::2]), min(obj['poly'][1::2]), \
                                         max(obj['poly'][0::2]), max(obj['poly'][1::2])

                width, height = xmax - xmin, ymax - ymin
                single_obj['bbox'] = xmin, ymin, width, height
                single_obj['image_id'] = image_id
                data_dict['annotations'].append(single_obj)
                single_obj['id'] = inst_count
                inst_count = inst_count + 1
            image_id = image_id + 1
        json.dump(data_dict, f_out, indent=4)


def dota2coco(srcpath_img,srcpath_labels, out_json,end='.png'):
    DOTA2COCO(srcpath_img,srcpath_labels,out_json,end)
    print("Dota to coco Done")
