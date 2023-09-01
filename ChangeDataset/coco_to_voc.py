import json
import os

from tqdm import tqdm
from xmltodict import unparse

def coco2voc(src, dst_base, ext='.png'):
    # BBOX_OFFSET: Switch between 0-based and 1-based bbox.
    # The COCO dataset is in 0-based format, while the VOC dataset is 1-based.
    # To keep 0-based, set it to 0. To convert to 1-based, set it to 1.
    BBOX_OFFSET = 1

    dst_base = dst_base #os.path.join("data", "VOCdevkitCOCO", "VOCCOCO")

    #dst_dirs = {x: os.path.join(dst_base, x) for x in ["Annotations", "ImageSets", "JPEGImages"]}
    #dst_dirs['ImageSets'] = os.path.join(dst_dirs['ImageSets'], "Main")
    #for k, d in dst_dirs.items():
    #    os.makedirs(d, exist_ok=True)


    def base_dict(filename, width, height, depth=3):
        return {
            "annotation": {
                "filename": os.path.split(filename)[-1],
                "size": {'width': width, 'height': height, "depth": depth},
                "object": []
            }
        }


    def base_object(size_info, name, bbox):
        x1, y1, w, h = bbox
        x2, y2 = x1 + w, y1 + h

        width = size_info['width']
        height = size_info['height']

        x1 = max(x1, 0) + BBOX_OFFSET
        y1 = max(y1, 0) + BBOX_OFFSET
        x2 = min(x2, width - 1) + BBOX_OFFSET
        y2 = min(y2, height - 1) + BBOX_OFFSET

        return {
            'name': name, 'difficult': '0',
            'bndbox': {'xmin': x1, 'ymin': y1, 'xmax': x2, 'ymax': y2}
        }


    sets = {
        "test": src,
    }

    cate = {x['id']: x['name'] for x in json.load(open(sets["test"]))['categories']}

    for stage, filename in sets.items():
        print("Parse", filename)
        data = json.load(open(filename))

        images = {}
        for im in tqdm(data["images"], "Parse Images"):
            img = base_dict(im['file_name'], im['width'], im['height'], 3)
            images[im["id"]] = img

        for an in tqdm(data["annotations"], "Parse Annotations"):
            ann = base_object(images[an['image_id']]['annotation']["size"], cate[an['category_id']], an['bbox'])
            images[an['image_id']]['annotation']['object'].append(ann)

        for k, im in tqdm(images.items(), "Write Annotations"):
            im['annotation']['object'] = im['annotation']['object'] or [None]
            unparse(im,
                    open(os.path.join(dst_base, "{}.xml".format(im['annotation']['filename'].split(ext)[0])), "w"),
                    full_document=False, pretty=True)

        print("Write image sets")
        #with open(os.path.join(dst_dirs["ImageSets"], "{}.txt".format(stage)), "w") as f:
        #    f.writelines(list(map(lambda x: 'P' + str(x).zfill(4) + "\n", images.keys())))

        print("OK")



def coco2vocrsd(src, dst_base):
    # BBOX_OFFSET: Switch between 0-based and 1-based bbox.
    # The COCO dataset is in 0-based format, while the VOC dataset is 1-based.
    # To keep 0-based, set it to 0. To convert to 1-based, set it to 1.
    BBOX_OFFSET = 1
    if not os.path.exists(dst_base):
        os.makedirs(dst_base)

    #dst_dirs = {x: os.path.join(dst_base, x) for x in ["Annotations", "ImageSets", "JPEGImages"]}
    #dst_dirs['ImageSets'] = os.path.join(dst_dirs['ImageSets'], "Main")
    #for k, d in dst_dirs.items():
    #    os.makedirs(d, exist_ok=True)


    def base_dict(filename, width, height, depth=3):
        return {
            "annotation": {
                "filename": os.path.split(filename)[-1],
                "size": {'width': width, 'height': height, "depth": depth},
                "object": []
            }
        }


    def base_object(size_info, name, bbox):
        x1, y1, w, h = bbox
        x2, y2 = x1 + w, y1 + h

        width = size_info['width']
        height = size_info['height']

        x1 = max(x1, 0) + BBOX_OFFSET
        y1 = max(y1, 0) + BBOX_OFFSET
        x2 = min(x2, width - 1) + BBOX_OFFSET
        y2 = min(y2, height - 1) + BBOX_OFFSET

        return {
            'name': name, 'bndbox': {'xmin': x1, 'ymin': y1, 'xmax': x2, 'ymax': y2}
        }


    sets = {
        "test": src,
    }

    cate = {x['id']: x['name'] for x in json.load(open(sets["test"]))['categories']}

    for stage, filename in sets.items():
        print("Parse", filename)
        data = json.load(open(filename))

        images = {}
        for im in tqdm(data["images"], "Parse Images"):
            img = base_dict(im['file_name'], im['width'], im['height'], 3)
            images[im["id"]] = img

        for an in tqdm(data["annotations"], "Parse Annotations"):
            ann = base_object(images[an['image_id']]['annotation']["size"], cate[an['category_id']], an['bbox'])
            images[an['image_id']]['annotation']['object'].append(ann)

        for k, im in tqdm(images.items(), "Write Annotations"):
            im['annotation']['object'] = im['annotation']['object'] or [None]
            unparse(im,
                    open(os.path.join(dst_base, "{}.xml".format(im['annotation']['filename'].split('.jpg')[0])), "w"),
                         full_document=False, pretty=True)

        #print("Write image sets")
        #with open(os.path.join(dst_base, "{}.txt".format(stage)), "w") as f:
        #    f.writelines(list(map(lambda x: 'P' + str(x).zfill(4) + "\n", images.keys())))

        print("OK")