"""
请实现 @runtime 效果为当前调用student_run时会自动打印当前时间
def student_run(name, age):
    print("name:" + name + "age:" + age + "run")
"""

import time

def runtime(function):
    def wrapper(*args, **kwargs):
        print(time.asctime(time.localtime(time.time())))
        function(*args, **kwargs)
    return wrapper

@runtime
def student_run(name, age):
    print("name:" + name + "age:" + age + " run")


student_run("张三", "18")