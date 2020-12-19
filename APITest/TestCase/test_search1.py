import unittest
import jsonpath
import requests
from APITest.APImodule import module1

# 这里是接口地址，必填
url1 = ""


class TestSearch(unittest.TestCase):

    def setUp(self):
        print("开始")

    # 云聊员工搜索接口
    def test_case_search1(self):
        data1 = ["刘童杰", "陈洪秀", "谢彩霞", "张英波", "张剑锋"]
        for i in data1:
            # 调用登录函数获取最新token
            token = module1.getToken()
            # 请求头
            headers = {'token': token}
            # 请求体
            payload = {'keyword': i}
            # 请求地址
            url = url1 + '/staff/search'
            # 发起get请求
            response = requests.request("GET", url, headers=headers, params=payload)
            # 接口返结果处理
            result = response.json()
            # 通过jsonpath模糊搜索name字段
            name = jsonpath.jsonpath(result, '$..name')
            print(result)
            print(name)
            print(result["code"])
            print(result["message"])
            # 接口返回200，并且返回结果中code=0,message=成功，
            self.assertEqual(200, response.status_code)
            self.assertEqual(0, result["code"])
            self.assertEqual('成功', result["message"])
            # self.assertIn(i, name)

    # 云聊APPP员工搜索接口
    def test_case_appsearch(self):
        data1 = ["刘童杰", "陈洪秀", "谢彩霞", "张英波", "张剑锋"]
        for i in data1:
            # 调用登录函数获取最新token
            token = module1.getToken()
            # 请求头
            headers = {'token': token}
            # 请求体
            payload = {'keyword': i}
            # 请求地址
            url = url1 + '/app'
            # 发起get请求
            response = requests.request("GET", url, headers=headers, params=payload)
            # 接口返结果处理
            result = response.json()
            # 通过jsonpath模糊搜索name字段
            # name = jsonpath.jsonpath(result, '$..name')
            print(result)

            print(result["code"])
            print(result["message"])
            # 接口返回200，并且返回结果中code=0,message=成功，
            self.assertEqual(200, response.status_code)
            self.assertEqual(0, result["code"])
            self.assertEqual('成功', result["message"])

    def tearDown(self):
        print("结束")
