import time
import unittest
import jsonpath
import requests
from APITest.APImodule import module1

# 这里是接口地址，必填
url1 = ""


class TestAppLet(unittest.TestCase):

    def setUp(self):
        print("开始")

    # 小程序商场直播通知接口
    def test_case_shop(self):
        # 请求头
        headers = {'token': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VfaWQiOjMyNjgsInVzZXJfaWQiOjl9"
                            "._Pd7EiXDi_L4_ii3hLm4DMJg3uYi7UL_86WEMTdaSOQ"}

        text = {"主题：家居好物买个够，金币专场秒不停！\r\n"
                "时间：今晚20:00-21:30\r\n"
                "直播内容：\r\n"
                "▶‌‌‌‌秋冬的这些家居好物，人手必备\r\n"
                "✔‌‌‌‌冬季双色保暖围巾！可做办公室毛毯实用，仅需59元\r\n"
                "✔‌‌‌‌公主风睡裙，孕妇也可穿！仅需109元✔‌‌‌‌贡缎秋冬家居服，实用睡衣套装，仅需139元\r\n"
                "‌‌‌‌▶‌‌‌‌金币秒杀好物，内衣火爆登场！\r\n"
                "✔‌‌‌‌经典款无痕内衣（可选细肩带/宽肩带），秒杀价：58金币\r\n！"
                "✔‌‌‌‌可休闲可职场的衬衣裙，秒杀价：120金币！\r\n"
                "✔‌‌‌‌冬天保暖神器：可爱的兔子睡袍（男女款），秒杀价：99金币/99元\r\n"
                "‌▶‌人气新品毛衣，够厚实！够保暖！今晚上市！\r\n"
                "‌‌▶‌‌‌‌所有【伊直播】前缀商品，通通返员工金币！双十一战役即将打响，激发沉寂客户，直播福利搞起来！"}

        # 请求体
        payload = {'title': '这个是标题',
                   'url': 'https://p0.ssl.qhimgs1.com/t01bf6d38632d799096.jpg',
                   'href': 'https://hao.360.com/?a1004',
                   'text': text,
                   'text1': '醒目提醒',
                   'text2': '按钮文字'

                   }
        # 请求地址
        url = url1 + '/broadcast/live'
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

    def test_intel(self):
        url = url1 + "/mini/intelligent/answer"
        # 参数sign，获取当前时间转化格式，拼接参数值给MD5加密:时间戳-mini-test_mini123456
        date = time.time()
        time1 = str(round(date * 1000))
        time2 = str(round(date * 1))
        sign2 = time1+"-mini-test_123456"
        print(sign2)
        sign = module1.md5vale(sign2)
        print(sign)
        payload = {'page': '1',
                   'per_page': '10',
                   'updated_at_start': '1604396400000',
                   'updated_at_end': time1,
                   'sign': sign,
                   'time': time1
                 }

        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

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
