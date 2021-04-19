# fire-smoke-detect and english description
## fire-smoke-detect and fire-smoke-detect-dataset

* author is leilei
* fire-smoke-detection qq-group(full): 980489677, qq-group2: 710514100
* If this project is helpful to you, please give a star, your star is an encouragement to me!
* Note: yolov4 only supports fire detection, yolov5s supports smoke-fire type 2 detection!

### installation environment
```
    python: 3.6+
    ubuntu16.04 or 18.04
    darknet (cuda10.0 docker)
    pytorch 1.6+ (cuda10.2 docker)
```

### new open-source dataset
* Workwear Reflective Clothing-Safety Helmet Data Set: [reflective-clothes-detect-dataset](https://github.com/gengyanlei/reflective-clothes-detect)
* It can be used for detection of designated areas such as construction areas or dangerous areas.

### Improve and optimize
* eg：Smoke is further subdivided into white smoke, black smoke, and gray smoke, and fires can also be further refined

### dataset download details
* [smoke-fire (10827's images,no labels)-BaiDuYunPanDownLoadLink](https://pan.baidu.com/s/1GhFKbp6hN26hxJWXIg_W2A) Code->(hhwq)
* [fire-smoke (2059's images,include labels)-BaiDuYunPanDownLoadLink](https://pan.baidu.com/s/1AvCMcmZ7SaAZznmyTO65cg) Code->(3q4r)
* [fire-smoke (2059's images,include labels)-**GoogleDrive** DownLoadLink](https://drive.google.com/file/d/1ydVpGphAJzVPCkUTcJxJhsnp_baGrZa7/view?usp=sharing)
---
* [yolov4 fire-detect's weight-BaiDuYunPanDownLoadLink](https://pan.baidu.com/s/14g0SkV5vR8OhnDOCTW6r9A) Code->(w3ip)
* yolov5 fire-smoke-detect's weight is in yolov5 folder!
* [darknet-yolov4-install-tutorial](https://github.com/AlexeyAB/darknet#how-to-compile-on-linux-using-make)
* [yolov4.conv.137](https://drive.google.com/open?id=1cewMfusmPjYWbrnuJRuKhPMwRe_b9PaT)
* If you want to use the latest version of darknet prediction function, please refer to [latest_darknet_API.py](https://github.com/gengyanlei/fire-detect-yolov4/blob/master/latest_darknet_API.py).

### How to use dataset?
* We annotate the fire-detection-dataset as Pascal VOC format:
    ```
    --VOC2020
        --Annotations (xml_num: 2059)
        --ImageSets(Main)
        --JPEGImages (image_num: 2059)
        
        --label_name: fire
    ```
* Unzip **.tar file command
    ```
    tar -xzvf ***.tar  (win or linux: Git Bash)
    or 
    7zip (win: 7zip; 360zip need 2 time unzip)
    ```
* If you want to convert VOC to YOLO format:
    ```
    Call yolov4's scripts voc_label.py
    ```
* Fire scene:
    ```
    vehicle-fire、grassland-fire、forest-fire、building-fire、Big and small fire、Day and night fire;
    ```
* Crawl fire-smoke images
    ```
    * crawl baidu-Bing images: crawl_baidu.py or crawl_baidu_bing.py
    ```
* **Data pre-labeling** ############### Key ###################
    ```
    (1)Download 10827 smoke-fire detection data set
    (2)Use my open source yolov5 fire-smoke detection model to pre-label unlabeled images
    (3)Manual correction of fire-smoke detection pre-labeling, retraining yolov4, yolov5
    (4)Come on！！！
    ```

### how to use test-train's code in yolov4
* yolov4's test：

    1. First of all, according to yolov4, I have uploaded the darknet compiled by myself, so you do not need to compile twice; **unzip yolov4's libdarknet.zip -> libdarknet.so！**
    2. Download the yolov4 fire detection model in Baidu cloud disk and put it in the backup_fire folder;
    3. Call the darknet_API.py function;
        ```
        from darknet_API import Detect
        detect = Detect(metaPath=r'./cfg/fire.data', configPath=r'./cfg/yolov4-fire.cfg',\
                        weightPath=r'./backup_fire/yolov4-fire_best.weights',\
                        namesPath=r'./cfg/fire.names')
        image = cv2.imread(r'/home/Datasets/20200714085948.jpg', -1)
        draw_img = detect.predict_image(image, save_path='./pred.jpg')
        ```
* yolov4 to onnx：
    
    1. yolov4 to onnx refer ./yolov4/yolov4_to_onnx/yolov4_to_onnx.py
    2. onnx to trt engine refer ./yolov4/yolov4_to_onnx/onnx_to_trt7.py
* yolov4's train：

    1. Convert VOC format data to YOLO format data
    2. Configure file information such as cfg
    3. Call the darknet command:
        ```
        ./darknet detector train cfg/fire.data cfg/yolov4-fire.cfg yolov4.conv.137 -gpus 0 -map -dont_show
        If there is insufficient gpu memory, you can modify the batch size and cancel the random multi-scale. 
        By default, random=1, cancel will be random=0
        ```
### how to use test's code in yolov5
* yolov5's test：

    1. cd yolov5, and excuting an order:
    ```
    python detect.py --source ***/aaa.jpg --weights ./best.pt
    ```

### demo
* ./result: fire-smoke-detect demos

|![fire-smoke-detect-demo](../result/result_demo.jpg)|
|----|

* ./xml_lab: fire-detection image annotations

|![fire-detect-annotation](../xml_lab/annotation.jpg)|
|----|

### Cite
* train_data contain 1-2-3-4:
* train_data1: https://blog.csdn.net/LEILEI18A/article/details/107334474
* train_data2: https://bitbucket.org/gbdi/bowfire-dataset/downloads/
* train_data3: https://github.com/OlafenwaMoses/FireNET/releases/download/v1.0/fire-dataset.zip
* train_data4: https://github.com/cair/Fire-Detection-Image-Dataset/blob/master/Fire%20images.rar
* fire-demo-dataset: http://signal.ee.bilkent.edu.tr/VisiFire/Demo/SampleClips.html
* google云盘下载链接由qq群中小伙伴提供

### Reputation:
* **This data is for academic exploration only！！！**

### Other
* [building-segmentation-dataset](https://github.com/gengyanlei/build_segmentation_dataset)
* [reflective-clothes-detect-dataset](https://github.com/gengyanlei/reflective-clothes-detect)


