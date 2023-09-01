# Rename yolo labels dowlnoaded from the Roboflow
import os

dir_in = 'output/labels/'
dir_img = 'output/images/'

visited = []
img_visited = []
letters = ['b','c','d','e','f','g','h','i','j','k']


def get_new_name(dir, file,name,end,visit):
    for l in letters:
        new_name = name + l
        if new_name in visit:
            continue
        else:
            os.rename(dir + file, dir + new_name + end)
            visit.append(new_name)
            return 0
    return 1

#Labels
end = '.txt'
labels = os.listdir(dir_in)
for file in os.listdir(dir_in):
    if '_jpg' in file:
        name = file.split('_jpg')[0]
    else:
        name = file.split(end)[0]
        visited.append(name)
        continue

    r = get_new_name(dir_in,file,name,end,visited)
    if r == 1:
        print("To few letters")

# Images:
imgend = '.jpg'
for label in labels:
    file = label.split(end)[0] + imgend
    if '_jpg' in file:
        name = file.split('_jpg')[0]
    else:
        name = file.split(imgend)[0]
        visited.append(name)
        continue


    r = get_new_name(dir_img,file,name,imgend,img_visited)
    if r == 1:
        print("To few letters")



