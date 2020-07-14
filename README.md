# fire-detect-yolov4 and [fire-detect-dataset](https://pan.baidu.com/s/1QlUTC8QW4wj0-Rwfx3fIPA)

* author is leilei(CSU)

## Some details
* [darknet-yolov4-install-tutorial](https://github.com/AlexeyAB/darknet#how-to-compile-on-linux-using-make)
* fire-dataset download: [BaiDuYunPan](https://pan.baidu.com/s/1QlUTC8QW4wj0-Rwfx3fIPA) 提取码->(9mr7)
* fire-yolov4-weights download: [BaiDuYunPan](https://pan.baidu.com/s/14g0SkV5vR8OhnDOCTW6r9A) 提取码->(w3ip)

## How to use this code?
0. download fire-yolov4's weight, and put it in backup_fire folder
1. Call the darknet_API main function:
    * `from darknet_API import Detect`
    * `detect = Detect(metaPath=r'./cfg/fire.data', configPath=r'./cfg/yolov4-fire.cfg', weightPath=r'./backup_fire/yolov4-fire_best.weights', namesPath=r'./cfg/fire.names')`
    * `image = cv2.imread(r'/home/Datasets/20200714085948.jpg', -1)`
    * `draw_img = detect.predict_image(image, save_path='./pred.jpg')`

## demo
* ./result: fire-detect demos

|![fire-detect-demo](https://github.com/gengyanlei/fire-detect-yolov4/blob/master/result/result_demo.jpg?raw=true)|
|----|
