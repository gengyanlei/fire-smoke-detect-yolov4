'''
注释：
    0. 首先打开本地翻墙代理 # 需要自己手动操作
    1. 将要搜索的文本表示成list
    2. 打开谷歌图片官网，输入文本，搜索
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
    inputs = browser.find_element_by_xpath('//div/input[@class="gLFyf gsfi"]')
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
    
    # google 有反爬，加入header试试
    opener = urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36')]
    urllib.request.install_opener(opener)

    img_link = browser.find_element_by_xpath('//div[@id="islmp"]//a/div/img')
    img_link.click()
    # 会出现另1个画面，再进行定位

    for i in range(img_num):
        img_link_ = browser.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img')  #此处失败 没有找到合适的，每次都是多个出现，这里用浏览器给的，发现都一样
        src_link = img_link_.get_attribute('src')
        try:
            print(src_link)
            # 保存图片，使用urlib
            img_name = uuid.uuid4()
            urllib.request.urlretrieve(src_link, os.path.join(save_path, str(img_name) + '.jpg'))
            # 关闭图像界面，并切换到外观界面
            time.sleep(random.random()*1.5)
        except:
            print(src_link)

        # 点击下一张图片
        browser.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[1]/a[2]').click()
        time.sleep(random.random() * 1)

    return

def main(names, save_root, img_num=100):
    '''
    :param names: list str
    :param save_root: str
    :param img_num: int
    :return:
    '''
    browser = webdriver.Chrome()
    browser.get(r'https://www.google.com.hk/imghp?hl=zh-CN&tab=wi&ogbl')
    browser.maximize_window()

    for name in names:
        save_path = os.path.join(save_root, str(names.index(name)))  # 以索引作为文件夹名称
        send_param_to_baidu(name, browser)
        download_baidu_images(save_path=save_path, img_num=img_num, browser=browser)
    # 全部关闭
    browser.quit()
    return

if __name__=="__main__":
    # 车辆起火-森林起火-草原起火-打火机火焰
    # names = ['Vehicle catches fire', 'Forest fire', 'Grassland catches fire', 'Lighter flame']
    names = ['Lighter flame']
    main(names=names, save_root=r'F:\Temp', img_num=200)

