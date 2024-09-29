![AirDetectionBanner2](https://github.com/user-attachments/assets/94e4ac07-334e-4f95-a60b-399c1547e7aa)


# Remote Sensing Object Detection Project

The Repository for the Master's Thesis in the Remote Sensing Object Detection. This Project explores the fascinating field of object detection in satellite imagery.

- The project's main objective is to compare the effectiveness of modern neural network architectures on <a href="https://github.com/Dr-Zhuang/geospatial-object-detection">RSD-GOD</a>  remote sensing dataset
- Propose improvements that could strengthen the models' ability to correctly detect various objects of interest
- Analyse the challanges with the top-down object detection
- Present [RSD-GOD](https://github.com/Dr-Zhuang/geospatial-object-detection) + [DOTAv2](https://captain-whu.github.io/DOTA/dataset.html) custon hybrid dataset called [DOTANA](https://drive.google.com/file/d/1s0u--CU-VVmv0t_O9_3TNNA2VcLahLPu/view?usp=sharing)
- Dataset Annotations RSD-GOD and DOTANA (in COCO, YOLO and VOC formats) are available for download [here](https://drive.google.com/file/d/1aypqgUDdSnJbElffF6P864MAnz0v7BLb/view?usp=sharing)


Multiple different architectures (shown in the structure chart) are used to detect images on the <a href="https://github.com/Dr-Zhuang/geospatial-object-detection">RSD-GOD</a> dataset. 


## Project Structure Chart

![AirDetectionSchema4](https://github.com/user-attachments/assets/cea94386-eced-4791-a667-a6393423047a)


## Gdańsk Bay Detections

Object Detected using a large YOLOv8 model. Images taken from Google Maps.


| Gdańsk Lech Wałęsa International Airport | „Błyskawica” Polish Museum Ship   | 
| :---:   | :---: | 
| ![airport_3_b](https://github.com/theATM/AirDetection/assets/48883111/fc29eefb-1b91-4a99-95f6-66f1be689579)  |  ![warship_1_b](https://github.com/theATM/AirDetection/assets/48883111/7ad746d7-29ca-4f7c-8335-fd92990f52c9) | 


## YOLOv8 COCO Results on RSD-GOD dataset


### Validation scores

<pre>
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.675 <br/>
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.972 <br/>
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.794 <br/>
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.359 <br/>
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.602 <br/>
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.722 <br/>
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.403 <br/>
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.726 <br/>
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.739 <br/>
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.467 <br/>
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.684 <br/>
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.784 <br/>
</pre>
  
 ### Test scores
  
<pre> 
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.589 <br/>
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.932 <br/>
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.652 <br/>
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.135 <br/>
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.418 <br/>
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.640 <br/>
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.364 <br/>
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.671 <br/>
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.681 <br/>
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.228 <br/>
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.587 <br/>
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.728 <br/>
</pre>

### Model Zoo


| YOLOv8  | Yolov5 | Yolov3 | SSD | DETR | Faster R-CNN | RTMDet
| :-----------: | :----: | :----: |  :----: | :----: | :----: | :----: |
| [Y28](https://drive.google.com/file/d/1ai4D---5uvQeoz2RzkisL5hlNCXDshSg/view?usp=sharing) [Y25](https://drive.google.com/file/d/1I4L0x9Hoo-8R9oGka45giOWHbq33AcEG/view?usp=sharing) <br> [Y9](https://drive.google.com/file/d/1bk0tnVXpOP7wc_9Pp2L16MuhuW1vxDG2/view?usp=sharing) [Y7](https://drive.google.com/file/d/1g9L0rVkM9B2IeH6rYLcdfWcCwUKSuw_5/view?usp=sharing) <br> [L6](https://drive.google.com/file/d/1PMvREHjc_NFcAvgTdImDsp0ooyG631kQ/view?usp=sharing) [L8](https://drive.google.com/file/d/1eKePU7NxfheCx19Yjb_ijPqgk5n-EY7G/view?usp=sharing) [L31](https://drive.google.com/file/d/1MHUkYqBYJTLESNbcjDCOH0bHE1v8X1Fx/view?usp=sharing) | [F29](https://drive.google.com/file/d/1FSccHMgBY9TrLokY8GxcW_k-VhXIzbIr/view?usp=sharing) | [O2](https://drive.google.com/file/d/1XbCKVi2A16a5E_rcWITa9IeLb5F1SGnt/view?usp=sharing) | [S23](https://drive.google.com/file/d/1sAsoLrs2eh66HGHyVldOu1I2l1yBQCyV/view?usp=sharing) <br> [S21](https://drive.google.com/file/d/1TVtVp_qJ0GdEV0s-6AZsdF_A8kXXnT4U/view?usp=sharing) | [D5](https://drive.google.com/file/d/1G84ybh_JvDLgcF-1OWM2ge63e3fCoESb/view?usp=sharing) [D6](https://drive.google.com/file/d/17XW5SPGvE9HOQHyVpQjchYuD8PlTpXOF/view?usp=sharing) <br> [D2](https://drive.google.com/file/d/1nt5jr17RP7hYRSsYByOoxuIyvWosARdf/view?usp=sharing) | [R4](https://drive.google.com/file/d/10CBfGHrepi_bTf17anL6ZzJqo2L60I3P/view?usp=sharing) [R20](https://drive.google.com/file/d/1ICOF3mc-WDt6NJP8HTzpbhPZZ9RJBPuI/view?usp=sharing) | [T1](https://drive.google.com/file/d/1crx4ypjRHtVeqtknwi4EW6w3u_MATnTo/view?usp=sharing) [T2](https://drive.google.com/file/d/1a1c11KqA0Gt_VmFKCu_RQe-ESwam6Xp0/view?usp=sharing) <br> [T3](https://drive.google.com/file/d/1HYP-lMsq8xlZ6qG7_MmAQi5Gc33HMU8x/view?usp=sharing) [T4](https://drive.google.com/file/d/1tNolx3TwHCgiWj8NJC42Qp-pcFsvH77b/view?usp=sharing) |

