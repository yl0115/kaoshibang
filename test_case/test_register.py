from common.myunit import StartEnd
from businessView.registerView import RegisterView
import logging
import unittest
import random

class Register_Test(StartEnd):
    def test_user_register(self):
        logging.info('====================test_user_register==============')
        r = RegisterView(self.driver)
        username = str('y' + 'fly' + str(random.randint(1000, 9000)))
        # 输入密码
        password = str('y0123' + str(random.randint(1000, 9000)))
        # 填写邮箱
        email = str('y' + str(random.randint(1000, 9000)) + '@163.com')
        self.assertFalse(r.register_action(username, password, email))


if __name__ == '__main__':
    unittest.main()
