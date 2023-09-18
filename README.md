# AirDetection
The Repository for the Master Thesis in the Remote Sensing Object Detection

Multiple different architectures (shown in the structure chart) are used to detect images on the <a href="https://github.com/Dr-Zhuang/geospatial-object-detection">RSD-GOD</a> dataset.

## Project Structure Chart

![repo_structv2](https://github.com/theATM/AirDetection/assets/48883111/c5d58974-52b9-44a5-b703-73c3816a8a1b)


## Gdańsk Bay Detections

Object Detected using a large YOLOv8 model. Images taken from Google Maps.


| Gdańsk Lech Wałęsa International Airport | „Błyskawica” Polish Museum Ship   | 
| :---:   | :---: | 
| ![airport_3_b](https://github.com/theATM/AirDetection/assets/48883111/fc29eefb-1b91-4a99-95f6-66f1be689579)  |  ![warship_1_b](https://github.com/theATM/AirDetection/assets/48883111/7ad746d7-29ca-4f7c-8335-fd92990f52c9) | 


## YOLOv8 COCO Results


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
