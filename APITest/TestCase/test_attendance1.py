import unittest
import jsonpath
import requests
import time
from APITest.APImodule import module1

url1 = ""


class TestAttendance(unittest.TestCase):

    def setUp(self):
        print("开始")

    # 考勤推送接口
    def test_attendancePush(self):
        # 参数sign，获取当前时间转化格式为2020-12-10，拼接参数值给MD5加密
        date = time.strftime("%Y-%m-%d", time.localtime())
        sign = module1.md5vale(date + "-ybs-247")

        # 调用登录函数获取最新token
        token = module1.getToken()
        # 请求头
        headers = {'token': token}
        body = {'sign': sign,
                'request_time': date
                }

        url = url1 + "/attendance/push?" + body

        payload = {
            "type": 1,
            "click_attention": [
                {
                    "employee_id": 39351,
                    "click_time": "5分钟",
                    "title": "还有5分钟就要上班了，别忘记打卡哦",
                    "jump_name": "立即打卡",
                    "jump_link": "https://test-ybs-app.atido.com/#/attendance/index"
                }
            ],
            "personal_data": [
                {
                    "employee_id": 39351,
                    "time_interval": "(2020.08.01-2020-08-07)",
                    "title": "上周考勤周报(2020.08.01-2020-08-07)",
                    "content": "您的考勤无异常记录",
                    "jump_name": "查看详情",
                    "jump_link": "https://test-ybs-app.atido.com/#/attendance/index"
                },
                {
                    "employee_id": 39351,
                    "late_times": "迟到：1次",
                    "lack_times": "缺卡：2次",
                    "leave_early_times": "早退：1次",
                    "time_interval": "(2020.08.01-2020-08-07)",
                    "is_abnormal": True,
                    "title": "上周考勤周报(2020.08.01-2020-08-07)",
                    "content": "您的有3条异常记录",
                    "jump_name": "去处理",
                    "jump_link": "https://test-ybs-app.atido.com/#/attendance/index"
                }
            ],
            "group_data": [
                {
                    "employee_id": 39351,
                    "global_data": "整体数据8人参与考勤，平均工时8.2小时",
                    "abnormal_data": "异常数据1人迟到，1人早退，2人缺卡，3人旷工",
                    "time_interval": "(2020.08.01-2020-08-07)",
                    "title": "团队考勤周报(2020.08.01-2020-08-07)",
                    "jump_name": "查看详情",
                    "jump_link": "https://test-ybs-app.atido.com/#/attendance/index"
                }
            ]
        }
        # payload = {"type": a, "click_attention": [{"employee_id": "39351", "click_time": "time", "lack_time":
        # "time", "late_time": "11", "title": "time", "jump_name": "time", "jump_link": "time"}], "personal_data": [
        # {"employee_id": "id", "time_interval": "time", "leave_early_times": "time", "late_times": "11",
        # "lack_times": "time", "is_abnormal": "time", "title": "time", "content": "time", "jump_name": "time",
        # "jump_link": "time"}], "group_data": [ {"employee_id": "id", "global_data": "time", "abnormal_data":
        # "time", "time_interval": "11", "title": "time", "jump_name": "time", "jump_link": "time"}] }

        # 发起post请求
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

    def tearDown(self):
        print("结束")
