import datetime
import time
import unittest
import jsonpath
import requests
from APITest.APImodule import module1

# 这里是接口地址，必填
url1 = "https://test-yim-api.yidejia.com"


class TestSend(unittest.TestCase):

    def setUp(self):
        print("开始")

    # 发送短信验证码
    def test_send(self):

        # 调用登录函数获取最新token
        # token = module1.test_login_code()
        # 请求头
        headers = {}
        # 请求体

        payload = {
                   'area_cdoe': "+86",
                   'phone': "18820787573"

                   }
        # 请求地址
        url = url1 + '/user/login/code/send'
        # 发起请求
        response = requests.request("POST", url, headers=headers, params=payload)
        # 接口返结果处理
        result = response.json()
        print(result)
        print(result["code"])
        print(result["message"])

        # 接口返回200，并且返回结果中code=0,message=成功，
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, result["code"])
        self.assertEqual('成功', result["message"])
        time.sleep(2)



    def tearDown(self):
        print("结束")
