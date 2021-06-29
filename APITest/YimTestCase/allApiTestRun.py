import time
import unittest
import HTMLTestRunner


# 获取所有测试用例
def get_allcase():
    # 测试用例存放路径
    case_path = 'E:/yim-api-test/APITest/AppTestCase'
    # 获取路径下面所有包含test_*.py命名的测试用例
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test_*.py")
    # 把测试用例加进测试用例集合suite
    suite = unittest.TestSuite()
    suite.addTest(discover)
    # 返回用例集合suite
    return suite


if __name__ == '__main__':
    # 运行测试用例
    timestr = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))  # 本地日期时间作为测试报告的名字
    filename = 'E:/yim-api-test/APITest/report/' + 'app接口第3轮测试结果' + timestr + '.html'  # 这个路径改成自己的目录路径
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='测试结果',
        description='Report_description'
    )
    # 执行测试用例，调用get_allcase()方法会返回测试用例集合给run()方法运行
    runner.run(get_allcase())
    fp.close()
