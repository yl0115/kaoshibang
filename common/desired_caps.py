from appium import webdriver
import yaml
import logging
import logging.config
import os
import multiprocessing

CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

udid_list = ['174e49cd7d32','127.0.0.1:62001']

def appium_desired(udid, port):
    with open('../config/kyb_caps.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    base_dir = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_dir, 'app', data['app'])
    desires_caps = {
        'platformName': data['platformName'],
        'deviceName': data['deviceName'],
        'platformVersion': data['platformVersion'],
        'udid': udid,
        'app': app_path,
        'appPackage': data['appPackage'],
        'appActivity': data['appActivity'],
        'noReset': data['noReset'],
        'unicodeKeyboard': data['unicodeKeyboard'],
        'resetKeyboard': data['resetKeyboard'],
        'automationName': data['automationName']
    }
    logging.info('start app')
    driver = webdriver.Remote('http://'+str(data['ip'])+":"+str(port)+'/wd/hub', desires_caps)
    driver.implicitly_wait(5)
    file.close()
    return driver

# """启动多台设备"""
# # desired_process = []
# # for i in range(len(udid_list)):
# #     port = 4723 + 2*i
# #     desired = multiprocessing.Process(target=appium_desired, args=(udid_list[i], port))
# #     desired_process.append(desired)

# if __name__ == '__main__':
    # for desired in desired_process:
    #     desired.start()
    # for desired in desired_process:
    #     desired.join()
    # appium_desired(udid_list[1],4723)
    # appium_desired(udid_list[1],4725)
    # with open('../config/kyb_caps.yaml', 'r', encoding='utf-8') as file:
    #     data = yaml.load(file, Loader=yaml.FullLoader)
    # # 获取当前文件路径的上一目录路劲
    # base_dir = os.path.dirname(os.path.dirname(__file__))
    # app_path = os.path.join(base_dir, 'app', data['app'])
    # print(app_path)
