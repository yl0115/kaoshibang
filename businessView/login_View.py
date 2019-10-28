import logging
from common.common_fun import Common
from common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class loginView(Common):
    username_type = (By.ID, 'com.tal.kaoyan:id/login_email_edittext')
    password_type = (By.ID, 'com.tal.kaoyan:id/login_password_edittext')
    loginBtn = (By.ID, 'com.tal.kaoyan:id/login_login_btn')
    top_commit = (By.ID, 'com.tal.kaoyan:id/tip_commit')
    # 我界面昵称元素
    username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')
    # 主页我的元素
    button_mysefl = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')
    # 我界面右上角设置元素
    RightButton = (By.ID, 'com.tal.kaoyan:id/myapptitle_RightButton_textview')
    # 个人设置退出登录按钮元素
    logout_text = (By.ID, 'com.tal.kaoyan:id/setting_logout_text')
    # 登录后弹出我知道了元素
    task_no_task = (By.ID, 'com.tal.kaoyan:id/task_no_task')
    # 退出点击确定元素
    # top_commit = (By.ID, 'com.tal.kaoyan:id/tip_commit')

    def login_action(self, username, password):
        self.check_cancelBtn()
        self.check_skip()
        logging.info("======================login_action====================")
        logging.info("username is %s" % username)
        self.driver.find_element(*self.username_type).send_keys(username)
        logging.info("password is %s" % password)
        self.driver.find_element(*self.password_type).send_keys(password)
        logging.info("click loginBtn")
        self.driver.find_element(*self.loginBtn).click()
        logging.info("logging")

    def check_account_alert(self):
        """重复登录弹窗关闭"""
        logging.info('=================check_account_alert===================')
        try:
            element = self.driver.find_element(*self.top_commit)
        except NoSuchElementException:
            pass
        else:
            logging.info('close top_commit')
            element.click()

    def task_no(self):
        logging.info('========================task_no==============')
        try:
            element = self.driver.find_element(*self.task_no_task)
        except NoSuchElementException:
            pass
        else:
            logging.info('close task_no')
            element.click()

    def check_LoginStaus(self):
        logging.info('===================check_LoginStaus============')
        self.task_no()
        self.check_market_ad()
        self.check_account_alert()

        try:
            self.driver.find_element(*self.button_mysefl).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error('login fail')
            self.getScreenShot('login_Fail')
            return False
        else:
            logging.info('login success!')
            self.logout_action()
            return True
    def logout_action(self):
        logging.info('================logout_action============')
        self.driver.find_element(*self.RightButton).click()
        self.driver.find_element(*self.logout_text).click()
        self.driver.find_element(*self.top_commit).click()


# if __name__ == '__main__':
#     driver = appium_desired('127.0.0.1:62001', 4723)
#     lo = loginView(driver)
#     lo.login_action('王蕾1992', 'yl123456789')
#     lo.check_LoginStaus()

