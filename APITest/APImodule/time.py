import datetime
import time


start_times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
now_time = datetime.datetime.now()

end_times =(now_time + datetime.timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")
timeArray = time.strptime(end_times, "%Y-%m-%d %H:%M:%S")
timeStamp = int(time.mktime(timeArray))
print(start_times)
print(now_time)
print(end_times)
print(timeStamp)