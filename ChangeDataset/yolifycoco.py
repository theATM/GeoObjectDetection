
def yolifycoco(in_coco,out_coco,split='_jpg'):

    #in_coco = 'instances_val.json'
    #out_coco ='instances_val_yolo.json'


    mapping = {
        1:0,
        2:1,
        3:2,
        4:3,
        5:4
    }

    import json

    # Opening JSON file
    f = open(in_coco)

    # returns JSON object as
    # a dictionary
    data = json.load(f)
    #data_copy = data.copy()

    assert data['categories'][0]['id']  == list(mapping.keys())[0], f"Categories starts from {data['categories'][0]} this script is designed to map them {list(mapping.keys())[0]}->{list(mapping.values())[0]}"

    # #Remove the object class:
    for i,d in enumerate(data['categories']):
        data['categories'][i]['id'] = mapping[d['id']]


    #if data['images'][0]['id'] == 0 and data['annotations'][0]['id'] == 0:
    #    # images ids starts and annotations from 0 but categories start from 1
    #    id_offset = 0
    #else:
    #    raise 'Unnown image ids format, maybe you have already used this script, first id is' + str(data['images'][0]['id'])
#
    #for i,d in enumerate(data['annotations']):
    #    assert data['images'][d['image_id']-id_offset]['id'] == d['image_id'] , f"{data['images'][d['image_id']-id_offset]['id']}, {d['image_id']}"

    # Iterating through the json list to remap the Roboflow annotations
    for i,d in enumerate(data['annotations']):
        if type(d['image_id']) == int:
            image_id = d['image_id']  #- id_offset
            data['annotations'][i]['category_id'] = mapping[d['category_id']]
            data['annotations'][i]['image_id'] = data['images'][image_id]['file_name'].split(split)[0]
            data['images'][image_id]['id'] = data['images'][image_id]['file_name'].split(split)[0]
            data['annotations'][i]['id'] = data['annotations'][i]['id']  #- id_offset

    # Iterate through images (they might not have any annotations) to change ids:
    for i,d in enumerate(data['images']):
        if type(d['id']) == int:
            image_id = d['id']
            data['images'][i]['id'] = data['images'][image_id]['file_name'].split(split)[0]

    # Closing file
    f.close()

    # Save to the new file
    with open(out_coco, 'w') as f:
        json.dump(data, f, indent=4)

    print("Done yolifying coco")


def yolifycocodota(in_coco,out_coco):
    # FOR DOTA IMAGES
    #in_coco = 'instances_train.json'
    #out_coco = 'instances_train_yolo.json'

    mapping = {
        1: 0,
        2: 1,
        3: 2,
        4: 3,
        5: 4
    }

    import json

    # Opening JSON file
    f = open(in_coco)

    # returns JSON object as
    # a dictionary
    data = json.load(f)
    # data_copy = data.copy()

    assert data['categories'][0]['id'] == list(mapping.keys())[
        0], f"Categories starts from {data['categories'][0]} this script is designed to map them {list(mapping.keys())[0]}->{list(mapping.values())[0]}"

    # #Remove the object class:
    for i, d in enumerate(data['categories']):
        data['categories'][i]['id'] = mapping[d['id']]

    if data['images'][0]['id'] == 1 and data['annotations'][0]['id'] == 1:
        # Both images and annotations and categories start from 1
        # change id by 1:
        id_offset = 1
    else:
        raise 'Unnown image ids format, maybe you have already used this script, first id is' + str(
            data['images'][0]['id'])

    for i, d in enumerate(data['annotations']):
        assert data['images'][d['image_id'] - id_offset]['id'] == d[
            'image_id'], f"{data['images'][d['image_id'] - id_offset]['id']}, {d['image_id']}"

    # Iterating through the json list to remap the Roboflow annotations
    for i, d in enumerate(data['annotations']):
        if type(d['image_id']) == int:
            image_id = d['image_id'] - id_offset
            data['annotations'][i]['category_id'] = mapping[d['category_id']]
            data['annotations'][i]['image_id'] = data['images'][image_id]['file_name'].split('.png')[0]
            data['images'][image_id]['id'] = data['images'][image_id]['file_name'].split('.png')[0]
            data['annotations'][i]['id'] = data['annotations'][i]['id'] - id_offset

    # Iterate through images (they might not have any annotations) to change ids:
    for i, d in enumerate(data['images']):
        if type(d['id']) == int:
            data['images'][i]['id'] = data['images'][i]['file_name'].split('.png')[0]

    # Closing file
    f.close()

    # Save to the new file
    with open(out_coco, 'w') as f:
        json.dump(data, f, indent=4)

    print("Done")