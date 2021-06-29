import unittest
import jsonpath
import requests
from APITest.APImodule import module1

# 这里是接口地址，必填
url1 = ""


class TestMessage(unittest.TestCase):

    def setUp(self):
        print("开始")

    # 发送消息接口
    def test_case_sendMessage(self):

        gid = str(1905)
        print(gid)
        # 调用登录函数获取最新token
        token = module1.getToken()
        # 请求头
        headers = {'token': token}
        # 请求体
        # is_room是否为群聊 0 不是 1 是 ；type消息类型 ；content消息内容
        payload = {'is_room': '1',
                   'type': '1',
                   'content': '@智能助理(智能助理) 云聊闪退天气很好',
                   'meta': '{"is_at_all":false,"at_user_ids":[{"id":7,"name":"智能助理(智能助理)"}],"file_size":18,'
                           '"file_type":"rgba(10, 19, 18, 1)"} '
                   }
        # 请求地址
        url = url1 + '/conversation/' + gid + '/message'
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

    # 获取群消息接口
    def test_case_getMessage(self):

        gid = str(1907)
        print(gid)
        # 调用登录函数获取最新token
        token = module1.getToken()
        # 请求头
        headers = {'token': token}
        # 请求体
        payload = {'is_room': '1',
                   'count': '5'

                   }
        # 请求地址
        url = url1 + '/conversation/' + gid + '/message'
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

    def tearDown(self):
        print("结束")
