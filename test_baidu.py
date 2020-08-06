'''
注释：
    1. 将要搜索的文本表示成list
    2. 打开百度图片官网，输入文本，搜索
    3. 逐条下载对应的图片

注：
    此代码未写断点续爬，许多功能未添加
'''
import os
import uuid
import time
import random
import urllib
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 键盘类
import cv2


def send_param_to_baidu(name, browser):
    '''
    :param name:    str
    :param browser: webdriver.Chrome 实际应该是全局变量的
    :return:        将要输入的 关键字 输入百度图片
    '''
    # 采用id进行xpath选择，id一般唯一
    inputs = browser.find_element_by_xpath('//input[@id="kw"]')
    inputs.clear()
    inputs.send_keys(name)
    time.sleep(1)
    inputs.send_keys(Keys.ENTER)
    time.sleep(1)

    return

def download_baidu_images(save_path, img_num, browser):
    ''' 此函数应在
    :param save_path: 下载路径
    :param img_num:   下载图片数量
    :param browser:   webdriver.Chrome
    :return:
    '''
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    img_link = browser.find_element_by_xpath('//li/div[@class="imgbox"]/a/img[@class="main_img img-hover"]')
    img_link.click()
    # 切换窗口
    windows = browser.window_handles
    browser.switch_to.window(windows[-1])  # 切换到图像界面

    for i in range(img_num):
        img_link_ = browser.find_element_by_xpath('//div/img[@class="currentImg"]')
        src_link = img_link_.get_attribute('src')
        print(src_link)
        # 保存图片，使用urlib
        img_name = uuid.uuid4()
        urllib.request.urlretrieve(src_link, os.path.join(save_path, str(img_name) + '.jpg'))
        # 关闭图像界面，并切换到外观界面
        time.sleep(0.35*random.random())

        # 点击下一张图片
        browser.find_element_by_xpath('//span[@class="img-next"]').click()

    # 关闭当前窗口，并选择之前的窗口
    browser.close()
    browser.switch_to.window(windows[0])
    return

def main(names, save_root, img_num=1000):
    '''
    :param names: list str
    :param save_root: str
    :param img_num: int
    :return:
    '''
    browser = webdriver.Chrome()
    browser.get(r'https://image.baidu.com/')
    browser.maximize_window()

    for name in names:
        save_path = os.path.join(save_root, str(names.index(name)))  # 以索引作为文件夹名称
        send_param_to_baidu(name, browser)
        download_baidu_images(save_path=save_path, img_num=img_num, browser=browser)
    # 全部关闭
    browser.quit()
    return

if __name__=="__main__":
    main(names=['油罐车', '吊车'], save_root=r'F:\Temp', img_num=10)

