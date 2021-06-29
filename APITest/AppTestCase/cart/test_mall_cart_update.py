import datetime
import time
import unittest
import jsonpath
import requests
from APITest.APImodule import module1

# 这里是接口地址，必填
url1 = "https://test-yim-api.yidejia.com"


class Test(unittest.TestCase):

    def setUp(self):
        print("开始")

    # 更新购物车商品 【token】
    def test_1(self):
        # 调用登录函数获取最新token
        token = module1.test_login_code()
        # 请求头
        headers = {
            "token": token

        }

        payload = {
            "cart_key": "25363",
            "goods_number": "51"

        }
        # 请求地址
        url = url1 + '/mall/api/v1/cart'
        # 发起请求
        response = requests.request("PUT", url, headers=headers, params=payload)
        # 接口返结果处理
        result = response.json()
        print(result)
        print(result["code"])
        print(result["message"])

        # 接口返回200，并且返回结果中code=0,message=成功，
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, result["code"])
        self.assertEqual('success', result["message"])

    def tearDown(self):
        print("结束")
