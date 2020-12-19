import datetime
import time
import unittest
import jsonpath
import requests
from APITest.APImodule import module1

# 这里是接口地址，必填
url1 = ""


class TestNotice(unittest.TestCase):

    def setUp(self):
        print("开始")

    # 新建系统公告
    def test_case_new(self):
        # 获取当前时间戳毫秒级,str和int可以转换格式，方便拼接
        time1 = str(round(time.time() * 1000))
        data1 = ["测试公告001", "测试公告002", "测试公告003"]

        for i in data1:
            # 调用登录函数获取最新token
            token = module1.getToken()
            # 请求头
            headers = {'token': token}
            # 请求体

            payload = {'title': i,
                       'content': "这是测试内容",
                       'organization_ids': "3",
                       'identity_type': "",
                       'send_at': "1635600271000",
                       'invalid_at': "1636600271000",
                       'is_dialog': "0"
                       }
            # 请求地址
            url = url1 + '/notice'
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

    # 编辑公告
    def test_case_editor(self):
        # 获取当前未发布公告的id，str和int可以转换时间格式，方便拼接
        gid = str(module1.getNoticeId())
        print(gid)

        # 获取当前时间戳毫秒级，str和int可以转换时间格式，方便拼接
        time1 = str(round(time.time() * 1000))
        print(time1)
        # 调用登录函数获取最新token
        token = module1.getToken()
        print(token)
        # 请求头
        headers = {'token': token}
        # 请求体

        payload = {'title': "修改的标题111",
                   'content': "这是修改内容",
                   'organization_ids': "3",
                   'identity_type': "",
                   'send_at': "1635600271000",
                   'invalid_at': "1636600271000",
                   'is_dialog': "0"
                   }
        # 请求地址
        url = url1 + '/notice/' + gid
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
        self.assertEqual('成功', result["message"])

    # 获取轮播公告
    def test_case_getNoticeList(self):
        # 调用登录函数获取最新token
        token = module1.getToken()
        # 请求头
        headers = {'token': token}
        # 请求体

        payload = {}
        # 请求地址
        url = url1 + '/notice/valid'
        # 发起请求
        response = requests.request("GET", url, headers=headers, params=payload)
        # 接口返结果处理
        result = response.json()
        print(result)
        print(result["code"])
        print(result["message"])
        print(result["data"])
        # 接口返回200，并且返回结果中code=0,message=成功，
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, result["code"])
        self.assertEqual('成功', result["message"])
        time.sleep(2)

    # 公告管理-列表
    def test_case_NoticeList2(self):
        # 调用登录函数获取最新token
        token = module1.getToken()
        # 请求头
        headers = {'token': token}
        # 请求体,is_publish	发布状态：0 待发布 1 已发布
        payload = {"page": "1", "per_page": "10", "is_publish": "1", "search": ""}
        # 请求地址
        url = url1 + '/notice'
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

    # 删除公告
    def test_case_deleteNotice(self):
        # 获取当前未发布公告的id，str和int可以转换格式，方便拼接
        gid = str(module1.getNoticeId())
        print(gid)
        # 调用登录函数获取最新token
        token = module1.getToken()
        # 请求头
        headers = {'token': token}
        # 请求体
        payload = {}
        # 请求地址
        url = url1 + '/notice/' + gid
        # 发起请求
        response = requests.request("DELETE", url, headers=headers, params=payload)
        # 接口返结果处理
        result = response.json()
        print(result)
        print(result["code"])
        print(result["message"])
        # 接口返回200，并且返回结果中code=0,message=成功，
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, result["code"])
        self.assertEqual('成功', result["message"])

    # 立即发布公告
    def test_case_publishNotice(self):
        # 获取当前未发布公告的id，str和int可以转换格式，方便拼接
        gid = str(module1.getNoticeId())
        print(gid)
        # 调用登录函数获取最新token
        token = module1.getToken()
        # 请求头
        headers = {'token': token}
        # 请求体
        payload = {}
        # 请求地址
        url = url1 + '/notice/' + gid + '/publish'
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
        self.assertEqual('成功', result["message"])

    # 下线公告
    def test_case_OfflineNotice(self):
        # 获取当前未发布公告的id，str和int可以转换格式，方便拼接
        gid = str(module1.getNoticeId2())
        print(gid)
        # 调用登录函数获取最新token
        token = module1.getToken()
        # 请求头
        headers = {'token': token}
        # 请求体
        payload = {}
        # 请求地址
        url = url1 + '/notice/' + gid + '/offline'
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
        self.assertEqual('成功', result["message"])

    # 获取公告详情
    def test_case_NoticeDetails(self):
        # 获取当前未发布公告的id，str和int可以转换格式，方便拼接
        gid = str(module1.getNoticeId2())
        print(gid)
        # 调用登录函数获取最新token
        token = module1.getToken()
        # 请求头
        headers = {'token': token}
        # 请求体
        payload = {}
        # 请求地址
        url = url1 + '/notice/' + gid
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

    # 获取参数项，如员工身份标识、管理员
    def test_case_NoticeParams(self):
        # 调用登录函数获取最新token
        token = module1.getToken()
        # 请求头
        headers = {'token': token}
        # 请求体
        payload = {}
        # 请求地址
        url = url1 + '/notice/params'
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
