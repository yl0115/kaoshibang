from baseView.base_View import BaseView
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
import os
import time
import csv
from selenium.webdriver.common.by import By


class Common(BaseView):
    cancelBtn = (By.ID, 'android:id/button2')
    skipBtn = (By.ID, 'com.tal.kaoyan:id/tv_skip')
    wemedia_cacle = (By.ID, 'com.tal.kaoyan:id/view_wemedia_cacel')

    def check_cancelBtn(self):
        """检查app提示是否更新，点击取消按钮"""
        logging.info('============check_cancelBtn=============')
        try:
            # 点击跳过按钮
            skip_ = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info("no checkskip")
        else:
            skip_.click()

    def check_skip(self):
        """检查屏幕引导页跳过按钮"""
        logging.info("check skip")
        try:
            # 点击跳过按钮
            skip_ = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info("no checkskip")
        else:
            skip_.click()

    def get_size(self):
        """获取屏幕大小"""
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipeLeft(self):
        """向左滑动"""
        logging.info('swipeLeft')
        l = self.get_size()
        x1 = int(l[0]*0.9)
        y1 = int(l[1]*0.5)
        x2 = int(l[0]*0.1)
        self.driver.swipe(x1, y1, x2, y1, 1000)

    def swipeUp(self):
        """向上滑动"""
        l = self.get_size()
        x1 = int(l[0]*0.5)
        y1 = int(l[1]*0.9)
        y2 = int(l[1]*0.2)
        self.driver.swipe(x1, y1, x1, y2, 10000)

    def getTime(self):
        """获取当前时间"""
        self.now = time.strftime("%Y-%m-%d %H_%M_%S ")
        return self.now

    def getScreenShot(self, module):
        """截图并存放到指定位置"""
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module, time)
        logging.info('get %s screenshots' %module)
        self.driver.get_screenshot_as_file(image_file)

    def check_market_ad(self):
        """检查是否有弹窗"""
        logging.info('=============check_market_ad==========')
        try:
            element = self.driver.find_element(*self.wemedia_cacle)
        except NoSuchElementException:
            pass
        else:
            logging.info('close market ad')
            element.click()

    def get_csv_data(self,csv_file, line):
        """data读取数据"""
        logging.info('==================get_csv_data============')
        with open(csv_file, 'r')as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row


# if __name__ == '__main__':
#     driver = appium_desired()
#     com = Common(driver)
#     com.check_cancelBtn()
#     for i in range(2):
#         com.swipeLeft()
#     com.check_skip()
#     com.getScreenShot("start app")



    # csv_file = '../data/account.csv'
    # data = com.get_csv_data(csv_file, 1)
    # print(data[0])
    # print(data[1])

