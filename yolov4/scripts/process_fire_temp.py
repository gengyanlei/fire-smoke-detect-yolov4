'''
    处理火灾检测数据集 VOC2020
'''
import os
import numpy as np

# xml_root = r'/home/ailab/dataset/Security_check/VOC2020/Annotations/'
# xmls = os.listdir(xml_root)
# f =open(r'/home/ailab/dataset/Security_check/VOC2020/ImageSets/Main/train.txt', 'w')
# for xml in xmls:
#     f.write(xml.split('.')[0]+'\n')
# f.close()



# 处理安检图像
# root = r'/home/ailab/dataset/hlw_fire_data/VOC2020/JPEGImages/'
# f = open(r'/home/ailab/dataset/hlw_fire_data/VOC2020/2020_train.txt', 'w')
# names = os.listdir(root)
# for name in names:
#     print(name)
#     f.write(os.path.join(root, name)+'\n')
# f.close()

''' 区分train test '''
names = os.listdir(r'/home/ailab/dataset/hlw_fire_data/VOC2020/JPEGImages')
names = [name for name in names if name.endswith('.jpg')]
num = len(names)
# 打乱
np.random.shuffle(names)

train_txt = open('', 'w')
test_txt = open('', 'w')

for i in range(num):
    # train
    if i < (num*4 // 5):
        train_txt.write(names[i].split('.')[0]+'\n')
    else:
        test_txt.write(names[i].split('.')[0]+'\n')
train_txt.close()
test_txt.close()

