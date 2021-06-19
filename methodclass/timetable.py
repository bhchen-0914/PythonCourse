import time
import calendar


# 构造按格式打印时间方法
def cat_time():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


# 构造查看日历方法

def cat_calendar(year, month):
    try:
        cal = calendar.month(year, month)
        print(cal)
    except:
        print('请输入有效年月')


# 构造手动查看日历方法
def view_calendar():
    year = int(input('输入年份：'))
    month = int(input('输入月份：'))
    cat_calendar(year, month)


