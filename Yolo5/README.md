### Yolov5 Training

To run experiments on Yolov5 simply copy the RSD-GOD and Dotana .yaml configuration files to the Yolov8 Repo.

Then run train.py with example parameters: 
* train.py --data rsd-god.yaml --weights yolov5s.pt --epochs 100 --batch 16
* train.py --data dotana.yaml --weights yolov5s.pt --epochs 100 --batch 16 --freeze 4

To get COCO styled metricies change the save_json to True in val.py and add own path for the coco_instances_val.json (in yolified coco format)

To validate run val.py --data rsd-god.yaml --weights mymodels/best.pt --save-json

To predict on images run detect.py --weights mymodels/best.pt --source dir_with_images/

Download Pretrained Model F29 [Here](https://drive.google.com/file/d/1FSccHMgBY9TrLokY8GxcW_k-VhXIzbIr/view?usp=sharing)

### Original README [Here](README_ORIGINAL.md)