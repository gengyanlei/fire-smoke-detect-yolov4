#  烟火检测-中文说明
## 烟火检测-烟火检测数据集

* 作者： leilei
* 烟-火检测 qq群: 980489677
* 如果此项目对您有所帮助，请给个star，您的star是对我的鼓励！
* 注意：yolov4仅支持火灾检测，yolov5s支持烟雾-火灾2类检测！

### 新开源的数据集项目
* 工作服反光衣-安全帽数据集: 可用于施工区域or危险区域等指定区域检测: [reflective-clothes-detect-dataset](https://github.com/gengyanlei/reflective-clothes-detect)

### 数据集下载细节
* [烟火(10827张图像,无标签)-百度云盘下载链接](https://pan.baidu.com/s/1GhFKbp6hN26hxJWXIg_W2A) 提取码->(hhwq)
* [烟火(2059张图像,含标签)-百度云盘下载链接](https://pan.baidu.com/s/1AvCMcmZ7SaAZznmyTO65cg) 提取码->(3q4r) [GoogleDrive](https://drive.google.com/file/d/1F2YcbqLeL5XqxDHBZOr9PGrAKMhXOEI7/view?usp=sharing)
---
* [yolov4火灾检测模型-百度云盘下载链接](https://pan.baidu.com/s/14g0SkV5vR8OhnDOCTW6r9A) 提取码->(w3ip)
* yolov5烟雾火灾检测模型 直接在yolov5文件夹中！
* [darknet-yolov4官方github安装教程](https://github.com/AlexeyAB/darknet#how-to-compile-on-linux-using-make)
* [yolov4.conv.137](https://drive.google.com/open?id=1cewMfusmPjYWbrnuJRuKhPMwRe_b9PaT)
* 如果想使用最新版本darknet预测函数，请参考[darknet_images.py](https://github.com/AlexeyAB/darknet/blob/master/darknet_images.py)文件。

### 数据集详细情况说明
* 烟火检测数据集(按照Pascal VOC格式排列):
    ```
    --VOC2020
        --Annotations (xml_num: 2059)
        --ImageSets(Main)
        --JPEGImages (image_num: 2059)
        
        --label_name: fire
    ```
* 解压压缩文件命令
    ```
    tar -xzvf ***.tar  (win or linux: Git Bash)
    or 
    7zip (win: 7zip; 360zip 需要解压2次)
    ```
* 将VOC格式转成yolo格式:
    ```
    调用yolov4 -> scripts -> voc_label.py
    ```
* 烟火检测数据集包含的场景类型:
    ```
    大火-小火，建筑起火、草原起火、森林起火、车辆(汽车、卡车、摩托车、电动车)起火、白天-黑夜起火、室内-室外起火；
    烟雾同火场景一致！
    ```
* 百度图片爬虫代码
    ```
    请使用 crawl_baidu.py
    ```
* **数据预标注** ###############关键###################
    ```
    (1)下载10827烟雾-火灾检测数据集
    (2)利用本人开源的yolov5火灾-烟雾检测模型，为未标注的图像预标注
    (3)人工修正火灾-烟雾检测预标注，重新训练yolov4、yolov5
    (4)加油！！！
    ```

### yolov4 测试-训练代码使用说明
* yolov4测试：

    1. 首先按照yolov4，本人已经将自己编译好的darknet上传，因此你不需要二次编译；
    2. 下载百度云盘中的yolov4火灾检测模型，将其放到backup_fire文件夹；
    3. 调用darknet_API.py函数:
        ```
        from darknet_API import Detect
        detect = Detect(metaPath=r'./cfg/fire.data', configPath=r'./cfg/yolov4-fire.cfg',\
                        weightPath=r'./backup_fire/yolov4-fire_best.weights',\
                        namesPath=r'./cfg/fire.names')
        image = cv2.imread(r'/home/Datasets/20200714085948.jpg', -1)
        draw_img = detect.predict_image(image, save_path='./pred.jpg')
        ```
* yolov4 训练：

    1. 将VOC格式转成yolo格式
    2. 修改cfg等文件的配置参数
    3. 执行如下命令:
        ```
        ./darknet detector train cfg/fire.data cfg/yolov4-fire.cfg yolov4.conv.137 -gpus 0 -map -dont_show
        ```
### yolov5 测试代码使用说明
* yolov5测试：

    1. 切换到yolov5，终端执行如下命令:
    ```
    python detect.py --source ***/aaa.jpg --weights ./best.pt
    ```

### 可视化
* ./result: 火灾预测

|![fire-detect-demo](https://github.com/gengyanlei/fire-detect-yolov4/blob/master/result/result_demo.jpg?raw=true)|
|----|

* ./xml_lab: 火灾标注

|![fire-detect-annotation](https://github.com/gengyanlei/fire-detect-yolov4/blob/master/xml_lab/annotation.jpg)|
|----|

### 参考博客-github项目
* train_data contain 1-2-3-4:
* train_data1: https://blog.csdn.net/LEILEI18A/article/details/107334474
* train_data2: https://bitbucket.org/gbdi/bowfire-dataset/downloads/
* train_data3: https://github.com/OlafenwaMoses/FireNET/releases/download/v1.0/fire-dataset.zip
* train_data4: https://github.com/cair/Fire-Detection-Image-Dataset/blob/master/Fire%20images.rar
* fire-demo-dataset: http://signal.ee.bilkent.edu.tr/VisiFire/Demo/SampleClips.html
* google云盘下载链接由qq群中小伙伴提供

### 郑重声明:
* **本数据仅学术探索！！！**

### 本人构建的其它数据集
* [building-segmentation-dataset](https://github.com/gengyanlei/build_segmentation_dataset)
* [reflective-clothes-detect-dataset](https://github.com/gengyanlei/reflective-clothes-detect)
