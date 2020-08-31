'''
注释：
    此版本基于2020-06月darknet.py，最新darknet.py修改较多，可能需要重新测试
    darknet python调用接口，参考darknet.py即可！
'''
import os
import cv2
import numpy as np
import random
import darknet

class Detect:
    def __init__(self, metaPath, configPath, weightPath, namesPath, gpu_id=2):
        '''
        :param metaPath:   ***.data 存储各种参数
        :param configPath: ***.cfg  网络结构文件
        :param weightPath: ***.weights yolo的权重
        :param namesPath:  ***.data中的names路径，这里是便于读取使用
        :param gpu_id:     gpu id
        '''
        # 设置gpu
        darknet.set_gpu(gpu_id)
        # 网络
        self.netMain = darknet.load_net_custom(configPath.encode("ascii"), weightPath.encode("ascii"), 0, 1) # batch=1
        # 各种参数
        self.metaMain = darknet.load_meta(metaPath.encode("ascii"))
        # 读取标签类别名称列表
        self.names = self.read_names(namesPath)
        # 每类颜色肯定一致，但是每次执行不一定都一样
        self.colors = self.color()

    def read_names(self, namesPath):
        # 专门读取包含类别标签名的***.names文件
        with open(namesPath, 'r') as f:
            lines = f.readlines()
            altNames = [x.strip() for x in lines]
        f.close()
        return altNames

    def color(self):
        # rgb 格式
        colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(self.metaMain.classes)]
        return colors

    def predict_image(self, image, thresh=0.25, is_show=True, save_path=''):
        '''
        :param image:    cv2.imread 图像, darknet自己会对图像进行预处理
        :param thresh:   置信度阈值, 其它阈值不变
        :param is_show:  是否将画框之后的图像返回
        :param save_path: 画框后的保存路径
        :return:         返回1个矩阵
        '''
        # bgr->rgb
        rgb_img = image[..., ::-1]
        # 获取图片大小，网络输入大小
        height, width = rgb_img.shape[:2]
        network_width = darknet.network_width(self.netMain)
        network_height = darknet.network_height(self.netMain)
        # 将图像resize到输入大小
        rsz_img = cv2.resize(rgb_img, (network_width, network_height), interpolation=cv2.INTER_LINEAR)
        # 转成tensor的形式，以及[1,C,H,W]
        darknet_image, _ = darknet.array_to_image(rsz_img)
        detections = darknet.detect_image(self.netMain, self.metaMain, darknet_image, thresh=thresh)

        if is_show:
            for detection in detections:
                x, y, w, h = detection[2][0], \
                             detection[2][1], \
                             detection[2][2], \
                             detection[2][3]
                # 置信度
                conf = detection[1]
                # 预测标签
                label = detection[0].decode()
                # 获取坐标
                x *= width / network_width
                w *= width / network_width
                y *= height / network_height
                h *= height / network_height
                # 转成x1y1x2y2,左上右下坐标; x是w方向
                xyxy = np.array([x - w / 2, y - h / 2, x + w / 2, y + h / 2])

                index = self.names.index(label)
                label_conf = f'{label} {conf:.2f}'
                self._plot_one_box(xyxy, rgb_img, self.colors[index], label_conf)
            bgr_img = rgb_img[..., ::-1]
            # 保存图像
            if save_path:
                cv2.imwrite(save_path, bgr_img)

            return bgr_img  #返回画框的bgr图像
        return detections

    def _plot_one_box(self, xyxy, img_rgb, color, label):
        # 直接对原始图像操作
        img = img_rgb[..., ::-1]  # bgr
        pt1 = (int(xyxy[0]), int(xyxy[1]))  # 左上角
        pt2 = (int(xyxy[2]), int(xyxy[3]))  # 右下角

        thickness = round(0.001 * max(img.shape[0:2])) + 1  # 必须为整数
        # if thickness > 1:
        #     thickness = 1  # 可强制为1
        cv2.rectangle(img, pt1, pt2, color, thickness)  # 画框,thickness线粗细
        # 获取字体的宽x-高y，实际上此高y应该乘1.5 才是字体的真实高度(bq是占上中、中下3个格)
        t_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, fontScale=thickness / 3, thickness=thickness)[0]
        # 按照2种方式显示，默认是在框上面显示，当上框仅挨着上边界时，采用框内显示；右边界不管

        c1 = (pt1[0], pt1[1] - int(t_size[1] * 1.5)) if pt1[1] - int(t_size[1] * 1.5) >= 0 else (pt1[0], pt1[1])
        c2 = (pt1[0] + t_size[0], pt1[1]) if pt1[1] - int(t_size[1] * 1.5) >= 0 else (
        pt1[0] + t_size[0], pt1[1] + int(t_size[1] * 1.5))
        # 判断c1 xy坐标是否都大于0
        if c1[0] < 0 or c1[1] < 0:
            x_t = c1[0] if c1[0] >= 0 else 0
            y_t = c1[1] if c1[1] >= 0 else 0
            c1 = (x_t, y_t)
        # 字体框内背景填充与框颜色一致
        cv2.rectangle(img, c1, c2, color, -1)  # 当thickness=-1时为填充
        # 绘制文本，文本是在下1/3位置开始
        text_pos = (c1[0], c1[1] + t_size[1])
        cv2.putText(img, label, text_pos, cv2.FONT_HERSHEY_SIMPLEX, thickness / 3, [225, 255, 255], thickness=thickness, lineType=cv2.LINE_AA)



if __name__ == '__main__':
    # gpu 通过环境变量设置CUDA_VISBLE_DEVICES=0
    # detect = Detect(metaPath=r'./cfg/helmet.data',
    #                 configPath=r'./cfg/yolov4-obj.cfg',
    #                 weightPath=r'./backup/yolov4-obj_best.weights',
    #                 namesPath=r'./data/helmet.names')

    # detect = Detect(metaPath=r'./cfg/coco.data',
    #                 configPath=r'./cfg/yolov4.cfg',
    #                 weightPath=r'./yolov4.weights',
    #                 namesPath=r'./data/coco.names')

    detect = Detect(metaPath=r'./cfg/fire.data',
                    configPath=r'./cfg/yolov4-fire.cfg',
                    weightPath=r'./backup_fire/yolov4-fire_best.weights',
                    namesPath=r'./cfg/fire.names',
                    gpu_id=2)

    # image = cv2.imread(r'/home/Datasets/image/000000.jpg', -1)
    # image = cv2.imread(r'/home/Datasets/20200714085948.jpg', -1)
    # detect.predict_image(image, save_path='./pred.jpg')

    ''' 读取视频，保存视频 '''
    cap = cv2.VideoCapture(r'/home/Datasets/fire1.avi')
    # 获取视频的fps， width height
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(count)
    # 创建视频
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(r'/home/Datasets/fire1.mp4', fourcc=fourcc, fps=fps, frameSize=(width,height))
    ret, frame = cap.read()  # ret表示下一帧还有没有 有为True
    while ret:
        # 预测每一帧
        pred = detect.predict_image(frame)
        video_writer.write(pred)
        cv2.waitKey(fps)
        # 读取下一帧
        ret, frame = cap.read()
        print(ret)
    cap.release()
    cv2.destroyAllWindows()














