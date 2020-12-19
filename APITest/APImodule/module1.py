import jsonpath
import requests
import hashlib

# 这里是接口地址，必填
url1 = ""


# 登录接口获取token
def getToken():
    payload = {'account': '张英波',
               'password': 'test888888',
               'sign': 'f9a69c19-25c7-4ebf-ae96-468f80c487db',
               'app_version': '1.17.3'
               }

    url = url1 + '/staff/signin'
    response = requests.request("POST", url, data=payload)
    result = response.json()
    # 获取token
    token1 = jsonpath.jsonpath(result, '$..token')
    # 格式化token
    token2 = "".join(token1)
    # 返回token
    return token2


# MD5加密，32位小写
def md5vale(key):
    input_name = hashlib.md5()

    input_name.update(key.encode("utf-8"))

    sign = input_name.hexdigest()

    print(key, "  ---->  ", sign)
    # 返回加密后的sign
    return sign


# 获取未发布公告列表接口
def getNoticeId():
    # 调用登录函数获取最新token
    token = getToken()
    # 请求头
    headers = {'token': token}

    # 请求体,is_publish	发布状态：0 待发布 1 已发布
    payload = {"page": "1", "per_page": "5", "is_publish": "0", "search": ""}
    # 请求地址
    url = url1 + '/notice'
    # 发起请求
    response = requests.request("GET", url, headers=headers, params=payload)
    # 接口返结果处理
    result = response.json()
    print(result)
    print(result["code"])
    print(result["message"])
    # 获取返回的公告中第一条公告的id
    noticeId = result["data"]["data"][0]["id"]
    print(result["data"]["data"][0]["id"])
    return noticeId


# 获取已发布公告列表接口
def getNoticeId2():
    # 调用登录函数获取最新token
    token = getToken()
    # 请求头
    headers = {'token': token}

    # 请求体,is_publish	发布状态：0 待发布 1 已发布
    payload = {"page": "1", "per_page": "5", "is_publish": "1", "search": ""}
    # 请求地址
    url = url1 + '/notice'
    # 发起请求
    response = requests.request("GET", url, headers=headers, params=payload)
    # 接口返结果处理
    result = response.json()
    print(result)
    print(result["code"])
    print(result["message"])
    # 获取返回的公告中第一条公告的id
    noticeId = result["data"]["data"][0]["id"]
    print(result["data"]["data"][0]["id"])
    return noticeId


if __name__ == '__main__':
    print(getToken())
