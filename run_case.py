import unittest
from HTMLTestRunner import HTMLTestRunner
from api.base import Base
from setting import username,password,TEST_REPORT_FILE

if __name__ == '__main__':

    Base().login(username,password)
    suite = unittest.TestLoader().discover('./cases','test*case.py')

    with open(TEST_REPORT_FILE,'wb') as f:
        runner = HTMLTestRunner(f,title='测试报告')
        runner.run(suite)