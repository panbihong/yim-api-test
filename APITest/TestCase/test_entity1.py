import unittest
import jsonpath
import requests
from APITest.APImodule import module1

# 这里是接口地址，必填
url1 = ""


class TestEntity(unittest.TestCase):

    def setUp(self):
        print("开始")

    # 云聊旧版获取组织架构接口
    def test_case_entity(self):
        # 调用登录函数获取最新token
        token = module1.getToken()
        # 请求头
        headers = {'token': token}
        # 请求体
        # payload = {'keyword': i}
        # 请求地址
        url = url1 + '/entity'
        # 发起get请求
        response = requests.request("GET", url, headers=headers)
        # 接口返结果处理
        result = response.json()
        print(result)
        print(result["code"])
        print(result["message"])
        # 接口返回200，并且返回结果中code=0,message=成功，
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, result["code"])
        self.assertEqual('成功', result["message"])

    # 云聊获取通讯录组织架构首页接口
    def test_case_entity_web(self):
        # 调用登录函数获取最新token
        token = module1.getToken()
        # 请求头
        headers = {'token': token}
        # 请求体
        # payload = {'keyword': i}
        # 请求地址
        url = url1 + '/entity/web'
        # 发起get请求
        response = requests.request("GET", url, headers=headers)
        # 接口返结果处理
        result = response.json()
        print(result)
        print(result["code"])
        print(result["message"])
        # 接口返回200，并且返回结果中code=0,message=成功，
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, result["code"])
        self.assertEqual('成功', result["message"])

    # 云聊根据名称获得自定义部门接口
    def test_case_entity_web2(self):
        data1 = ["总部客服", "配送中心", "智能云团队", "广州二部", "广州一部"]
        for i in data1:
            # 调用登录函数获取最新token
            token = module1.getToken()
            # 请求头
            headers = {'token': token}
            # 请求体
            payload = {'entity_name': i}
            # 请求地址
            url = url1 + '/entity/web/2'
            # 发起get请求
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

    # 云聊根据单位获取组织架构下的部门接口
    def test_case_entity3(self):
        data1 = ["1", "2", "3", "4", "5"]
        for i in data1:
            # 调用登录函数获取最新token
            token = module1.getToken()
            print(token)
            # 请求头
            headers = {'token': token}
            # 请求体
            payload = {}
            # 请求地址
            url = url1 + '/entity/'+i
            # 发起get请求
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

    # 云聊搜索部门名称接口
    def test_case_entity4(self):
        data1 = ["智能云", "学院", "广州三部", "广州一部", "广州二部"]
        for i in data1:
            # 调用登录函数获取最新token
            token = module1.getToken()
            print(token)
            # 请求头
            headers = {'token': token}
            # 请求体
            payload = {"name": i}
            # 请求地址
            url = url1 + '/entity/search'
            # 发起get请求
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
