#Copy labels about only 5 classes
import os

def remap_labels(path,out_path):
    classes = ['airport', 'plane', 'storage-tank', 'helicopter', 'ship']
    new_classes = ['airport', 'plane', 'oiltank', 'helicopter', 'warship']

    #path = 'input/dota/val/org_labels' #'DOTA-v2.0_train'
    #out_path = 'output/labels'

    for file in os.listdir(path):

        with open(os.path.join(path,file)) as f:
            df = f.read()
            file_id = file.split('.')[0][1:]
            out_content = []
            for line in df.split('\n'):
                if line == '': break
                name = line.split(' ')[8]
                if name in classes:
                    line = line.replace(name,new_classes[classes.index(name)])
                    out_content.append(line)
            # if out_content != []: # - uncomment to remove empty files
            with open(os.path.join(out_path,file),'w') as outf:
                for line in out_content:
                    outf.write(line+'\n')
    print("Remaping Done")

