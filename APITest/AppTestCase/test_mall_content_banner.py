import datetime
import time
import unittest
import jsonpath
import requests
from APITest.APImodule import module1

# 这里是接口地址，必填
url1 = "https://test-yim-api.yidejia.com"


class TestBanner(unittest.TestCase):

    def setUp(self):
        print("开始")

    # 通过key获取banner【缓存】【不分页】
    def test_banner(self):
        # 调用登录函数获取最新token
        # token = module1.test_login_code()
        # 请求头
        headers = {}
        # 请求体
        banner = ["ios_banner_home_top", "ios_cate_banner", "ios_banner_skin_top",
                  "ios_banner_gibson_top", "ios_banner_beauty_top", "ios_banner_cloth_top",
                  "ios_banner_baby_top", "ios_banner_brand_top"
                  ]

        for i in banner:
            payload = {
                "keys[]": i,
                "thumb_image_width": ""

            }
            # 请求地址
            url = url1 + '/mall/api/v1/content/banner'
            # 发起请求
            response = requests.request("GET", url, headers=headers, params=payload)
            # 接口返结果处理
            result = response.json()

            print(result)
            print(result["code"])
            print(result["message"])

            # 接口返回200，并且返回结果中code=0,message=成功，
            self.assertEqual(200, response.status_code)
            self.assertEqual(0, result["code"])
            self.assertEqual('success', result["message"])
            time.sleep(2)

    def tearDown(self):
        print("结束")
