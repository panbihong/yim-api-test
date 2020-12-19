import unittest
import jsonpath
import requests
import time
from APITest.APImodule import module1

# 这里是接口地址，必填
url1 = ""


class TestYbs(unittest.TestCase):

    def setUp(self):
        print("开始")

    # ybs视频分享接口
    def test_fenxiang(self):
        # 参数sign，获取当前时间转化格式为2020-12-10，拼接参数值给MD5加密
        date = time.strftime("%Y-%m-%d", time.localtime())
        sign = module1.md5vale(date + "-ybs-247")

        url = url1+"/share/message/to/yim"

        payload = {"staff_id": 247, "chatroom_ids": [1905,1906,1907], "sign": sign,
                   "video_url": "https://p0.ssl.qhimgs1.com/t01bf6d38632d799096.jpg",
                   "title": "学院视频地址带token", "desc": "哈哈哈哈",
                   "href": "https://hao.360.com/?a1004", "project": "ybs"}
        headers = {
            'Content-Type': 'application/json'
        }
        # 发起json格式的post请求
        response = requests.request("POST", url, json=payload, headers=headers)
        result = response.json()
        res2 = jsonpath.jsonpath(result, '$..code')
        res3 = jsonpath.jsonpath(result, '$..data')
        res4 = jsonpath.jsonpath(result, '$..message')
        print(result)
        # 接口返回200，并且返回结果中'code': 0, 'data': '分享成功', 'message': '成功'
        self.assertEqual(200, response.status_code)
        self.assertIn(0, res2)
        self.assertIn('分享成功', res3)
        self.assertIn('成功', res4)

    # ybs项目空间接口
    def test_xianmu(self):
        # 参数sign，获取当前时间转化格式为2020-12-10，拼接参数值给MD5加密
        date = time.strftime("%Y-%m-%d", time.localtime())
        sign = module1.md5vale(date + "-ybs-247")

        url = url1+"/ybs/staff/project/template"

        payload = {
            "staff_id": 247,
            "sign": sign,
            "chatroom_ids": [
                1906,
                1905,
                1907
            ],
            "staff_ids": [
                247
            ],
            "title": "11-03项目进度播报测试一",
            "href": "https://test-ybs-app.atido.com/#/projectspace/projectDetail/taskList?id=44&typ",
            "data": [
                {
                    "text": "今天完成任务10个",
                    "size_type": 1
                },
                {
                    "text": "1:[第一个任务]",
                    "size_type": 2
                }, {
                    "text": "1:[第二个任务]",
                    "size_type": 2
                }, {
                    "text": "1:[第三个任务]",
                    "size_type": 2
                }, {
                    "text": "总逾期任务3个,请及时跟进",
                    "size_type": 1
                }, {
                    "text": "项目进度90%",
                    "size_type": 1
                }

            ]
        }

        headers = {
            'Content-Type': 'application/json'
        }
        # 发起json格式的post请求
        response = requests.request("POST", url, json=payload, headers=headers)
        result = response.json()
        res2 = jsonpath.jsonpath(result, '$..code')

        res4 = jsonpath.jsonpath(result, '$..message')
        print(result)
        # 接口返回200，并且返回结果中'code': 0, 'message': '成功'
        self.assertEqual(200, response.status_code)
        self.assertIn(0, res2)
        self.assertIn('成功', res4)

    def tearDown(self):
        print("结束")
