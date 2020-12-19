# yim-api-test
接口自动化的测试用例

隐藏了接口地址，需要调试的时候加上接口地址就可以调试了

APITest目录是代码


APITest目录下的APImodule目录，写了登录获取token接口，MD5加密，获取一些公告ID等前提条件的接口


APITest目录下的TestCase目录下是测试用例，allApiTestRun.py是运行测试用例集合，并且输出测试报告 其他test_开头的都是测试用例


APITest目录下的report是输出测试报告的


本期使用了python+unittest+requests实现简单的接口自动化测试


后面会尝试利用新框架pytest，引入更多的开源库，提高测试用例的管理等等
