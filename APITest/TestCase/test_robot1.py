import unittest
import jsonpath
import requests
from APITest.APImodule import module1

# 这里是接口地址，必填
url1 = ""


class TestRobot(unittest.TestCase):

    def setUp(self):
        print("开始")

    # 获取群内的机器人配置（查询是否OA管理员）接口
    def test_case_robotCheck(self):
        gid = str(1907)
        # 调用登录函数获取最新token
        token = module1.getToken()
        # 请求头
        headers = {'token': token}
        # 请求体
        payload = {}
        # 请求地址
        url = url1 + '/chatroom/' + gid + '/robot'
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
        self.assertEqual('成功', result["message"])

        # 业绩推送接口
    def test_case_encouragePush(self):
        # 调用登录函数获取最新token
        token = module1.getToken()
        # 请求头
        headers = {'token': token}
        # 请求体
        payload = {"order_cash": "12345",
                   "oa_entity_id": "1047",
                   "staff_name": "唐凯丽",
                   "oa_staff_id": "1959",
                   "is_vip": True,
                   "oa_entity_name": "广州二部"

                   }
        # 请求地址
        url = url1 + '/encourage-push'
        # 发起请求
        response = requests.request("POST", url, headers=headers, data=payload)
        # 接口返结果处理
        result = response.json()
        print(result)
        print(result["code"])
        print(result["message"])
        # 接口返回200，并且返回结果中code=0,message=成功，
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, result["code"])
        self.assertEqual('成功', result["message"])

    def tearDown(self):
        print("结束")
