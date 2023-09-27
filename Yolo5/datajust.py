import numpy as np
import os
import xml.etree.ElementTree as ET
import shutil

labels = {
    "helicopter": 0,
    "airport"   : 1,
    "warship"   : 2,
    "plane"     : 3,
    "oiltank"   : 4,
}

setdirmapping = {
    "testingsets" : "test",
    "trainingsets" : "train",
    "validationsets": "val"
}


in_dataset_path = "RSD-HARSH-TXT"
out_dataset_path = "dataout"

if os.path.exists(out_dataset_path+"/labels") is False:
    os.mkdir(out_dataset_path+"/labels")

if os.path.exists(out_dataset_path+"/labels/train") is False:
    os.mkdir(out_dataset_path+"/labels/train")

if os.path.exists(out_dataset_path+"/labels/test") is False:
    os.mkdir(out_dataset_path+"/labels/test")

if os.path.exists(out_dataset_path+"/labels/val") is False:
    os.mkdir(out_dataset_path+"/labels/val")

if os.path.exists(out_dataset_path+"/images") is False:
    os.mkdir(out_dataset_path+"/images")

if os.path.exists(out_dataset_path+"/images/train") is False:
    os.mkdir(out_dataset_path+"/images/train")

if os.path.exists(out_dataset_path+"/images/test") is False:
    os.mkdir(out_dataset_path+"/images/test")

if os.path.exists(out_dataset_path+"/images/val") is False:
    os.mkdir(out_dataset_path+"/images/val")



for setdir in os.listdir(in_dataset_path):
    outsetdir = setdirmapping[setdir]

    # Preprocess labels
    for annot in os.listdir(in_dataset_path+"/"+setdir+"/xml"):
        try:
            tree = ET.parse(in_dataset_path+"/"+setdir+"/xml/" + annot)
        except Exception as e:
            print(e)
            print('Ignore this bad annotation: ' + setdir + " " + annot)
            continue
        # Read Image:
        img = {'objects': []}
        for elem in tree.iter():
            if 'filename' in elem.tag:
                img['filename'] = elem.text
            if 'width' in elem.tag:
                img['width'] = int(elem.text)
            if 'height' in elem.tag:
                img['height'] = int(elem.text)
            if 'object' in elem.tag or 'part' in elem.tag:
                obj = {}
                for attr in list(elem):
                    if 'name' in attr.tag:
                        obj['name'] = attr.text
                    if 'bndbox' in attr.tag:
                        for dim in list(attr):
                            if 'xmin' in dim.tag:
                                obj['xmin'] = int(round(float(dim.text)))
                            if 'ymin' in dim.tag:
                                obj['ymin'] = int(round(float(dim.text)))
                            if 'xmax' in dim.tag:
                                obj['xmax'] = int(round(float(dim.text)))
                            if 'ymax' in dim.tag:
                                obj['ymax'] = int(round(float(dim.text)))
                img['objects'] += [obj]
        # Save to file
        filename = img['filename'][:-3]+"txt" # Change te extension
        with open(out_dataset_path+"/labels/"+outsetdir+"/"+filename,"w") as file:
            for obj in img['objects']:
                #Write Class name code
                line = str(labels[obj["name"]]) + " "
                #Calculate x-center y-center width height
                w = obj['xmax'] - obj['xmin']
                h = obj['ymax'] - obj['ymin']
                x = obj['xmin'] + w / 2
                y = obj['ymin'] + h / 2
                #Scale them to 0 - 1
                w = w / img['width']
                h = h / img["height"]
                x = x / img['width']
                y = y / img["height"]
                # Add them to the file
                line += str(x) + " " + str(y) + " " + str(w) + " " + str(h) + '\n'
                file.write(line)

    # Just copy images
    for img in os.listdir(in_dataset_path + "/" + setdir + "/image"):
        shutil.copyfile(in_dataset_path + "/" + setdir + "/image/"+img, out_dataset_path + "/images/" + outsetdir + "/" + img)






