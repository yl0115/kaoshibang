import logging, random
from common.desired_caps import appium_desired
from common.common_fun import Common, By, NoSuchElementException
from time import sleep

class RegisterView(Common):
    # 登录界面注册按钮元素
    register_text = (By.ID, 'com.tal.kaoyan:id/login_register_text')
    # 新用户注册界面设置用户头像元素
    userheader = (By.ID, 'com.tal.kaoyan:id/activity_register_userheader')
    # 选择index下标为13的图片
    item_image = (By.ID, 'com.tal.kaoyan:id/item_image')
    # 点击选择好的图片保存按钮
    save = (By.ID, 'com.tal.kaoyan:id/save')
    # 输入注册用户名
    username_edittext = (By.ID, 'com.tal.kaoyan:id/activity_register_username_edittext')
    # 输入注册密码
    password_edittext = (By.ID, 'com.tal.kaoyan:id/activity_register_password_edittext')
    # 输入注册邮箱
    email_edittext = (By.ID, 'com.tal.kaoyan:id/activity_register_email_edittext')
    register_btn = (By.ID, 'com.tal.kaoyan:id/activity_register_register_btn')
    # 完善资料界面的按钮
    goBtn = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_goBtn')
    # 选择学校框元素
    school_name= (By.ID,'com.tal.kaoyan:id/perfectinfomation_edit_school_name')
    # 地区
    forum_title= (By.ID,'com.tal.kaoyan:id/more_forum_title')
    # 大学
    university= (By.ID,'com.tal.kaoyan:id/university_search_item_name')
    # 目标专业
    perfectinfomation_major= (By.ID,'com.tal.kaoyan:id/activity_perfectinfomation_major')
    subject_title= (By.ID,'com.tal.kaoyan:id/major_subject_title')
    search_item_name= (By.ID,'com.tal.kaoyan:id/major_search_item_name')
    # 我界面昵称元素
    username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')
    # 主页我的元素
    button_mysefl = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')


    def register_action(self, register_username, register_password, register_email):
        self.check_cancelBtn()
        self.swipeLeft()
        self.check_skip()
        logging.info('=================register_action===============')
        # 点击注册按钮
        self.driver.find_element(*self.register_text).click()
        # 设置用户头像
        logging.info('set userhead')
        self.driver.find_element(*self.userheader).click()
        self.driver.find_elements(*self.item_image)[1].click()
        self.driver.find_element(*self.save).click()
        logging.info('username is %s' %register_username)
        self.driver.find_element(*self.username_edittext).send_keys(register_username)
        sleep(3)
        logging.info('password is %s' %register_password)
        self.driver.find_element(*self.password_edittext).send_keys(register_password)
        logging.info('email is %s' %register_email)
        self.driver.find_element(*self.email_edittext).send_keys(register_email)
        logging.info('click register_btn')
        self.driver.find_element(*self.register_btn).click()

        try:
            self.driver.find_element(*self.goBtn)
        except NoSuchElementException:
            logging.error('register fail!')
            self.getScreenShot('register_fail')
            return False
        else:
            self.add_register_info()
            if self.check_register_staus():
                return True
            else:
                return False

    def add_register_info(self):
        """选择专业和学校"""
        logging.info('=================add_register_info===============')
        logging.info('select school')
        self.driver.find_element(*self.school_name).click()
        # self.swipeUp()
        self.driver.find_elements(*self.forum_title)[0].click()
        self.driver.find_elements(*self.university)[1].click()
        logging.info('select major')
        self.driver.find_element(*self.perfectinfomation_major).click()
        self.driver.find_elements(*self.subject_title)[0].click()
        self.driver.find_elements(*self.search_item_name)[0].click()
        self.driver.find_element(*self.goBtn).click()

    def check_register_staus(self):
        logging.info('=================check_register_staus===============')
        # 去掉弹窗
        self.check_market_ad()
        try:
            self.driver.find_element(*self.button_mysefl).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error('register fail')
            self.getScreenShot('register_Fail')
            return False
        else:
            logging.info('register success!')
            return True





#
#
# if __name__ == '__main__':
#
#     driver = appium_desired('127.0.0.1:62001', 4723)
#     register = RegisterView(driver)
#     # 输入用户名
#     username = str('zxw2018' + 'fly' + str(random.randint(1000, 9000)))
#     # 输入密码
#     password = str('zxw' + str(random.randint(1000, 9000)))
#     # 填写邮箱
#     email = str('yanglei' + str(random.randint(1000, 9000)) + '@163.com')
#
#     register.register_action(register_username=username, register_password=password, register_email=email)
#     sleep(3)
#     driver.close_app()
#     sleep(6)