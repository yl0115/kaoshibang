import unittest
import logging
from time import sleep
from common.desired_caps import *

class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('===========setUp==========')
        self.driver = appium_desired(udid_list[1], 4723)
        # self.driver = appium_desired(udid_list[1], 4725)
    def tearDown(self):
        logging.info('============tearDown=========')
        sleep(5)
        self.driver.close_app()
