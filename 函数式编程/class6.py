"""
装饰器练习
实现自带参数的装饰器并根据参数调整装饰器的逻辑
实现多个装饰器嵌套使用
"""

import sys
import time


def check_repeat(check_mode):  # check_mode参数是查重模式参数，为0时，找到重复项便返回，为1时，没找到返回
    def function(func):
        def wrapper(*args):
            if check_mode == 0:
                for items in admin_message:
                    if items['username'] == args[0]:
                        print('该用户已存在,正在返回主菜单')
                        time.sleep(1)
                        return
                func(*args)
            elif check_mode == 1:
                for items in admin_message:
                    if items['username'] == args[0]:
                        func(*args)
                        return
                print('没有找到该用户')
        return wrapper
    return function


def check_root(func):  # 查验是否有root权限
    def wrapper(*args):
        username = input('请输入管理员账号：')
        password = input('请输入管理员密码:')
        if username == root_count['username'] and password == root_count['password']:
            print('管理员身份已确认')
            time.sleep(1)
            func(*args)
        else:
            print('管理员身份确认失败，返回主菜单')
            time.sleep(1)
    return wrapper


@check_repeat(0)
def reg_success(set_username, set_password):
    admin_message.append({'username': set_username, 'password': set_password})
    print('注册成功')


def register():
    print('~' * 10, '注册界面', '~' * 10)
    set_username = input('设置用户名：')
    set_password = input('设置密码：')
    reg_success(set_username, set_password)
    return


def login():
    print('~' * 10, '登录界面', '~' * 10)
    access_num = 3
    while access_num > 0:
        login_username = input('请输入用户名：')
        login_password = input('请输入密码：')
        for items in admin_message:
            if login_username == items['username'] and login_password == items['password']:
                print('登录成功')
                return
        access_num -= 1
        if access_num != 0:
            print('账号或密码错误,你还有%d次机会' % access_num)
    print('bye bye')
    sys.exit()


def delete_account():
    print('~' * 10, '删除界面', '~' * 10)
    delete_username = input('输入要删除的用户名：')
    delete_success(delete_username)
    return


@check_root
@check_repeat(1)
def delete_success(delete_username):
    for items in admin_message:
        if delete_username == items['username']:
            admin_message.remove(items)
            print('删除成功')


def change_password():
    print('~' * 10, '修改密码', '~' * 10)
    ch_username = input('输入账号：')
    for items in admin_message:
        if ch_username == items['username']:
            items['password'] = input('输入新密码：')
            print('修改成功')
            return
    print('没有找到该账户，请重新输入')
    return


@check_root
def show_list():
    print('~' * 10, '信息如下', '~' * 10)
    print('账号', ' ' * 10, '密码', ' ' * 10)
    for items in admin_message:
        print('%s                %s' % (items['username'], items['password']))
    return


def execute(func_list):
    if func_list == '1':
        register()
        return
    elif func_list == '2':
        login()
        return
    elif func_list == '3':
        delete_account()
        return
    elif func_list == '4':
        change_password()
        return
    elif func_list == '5':
        show_list()
        return
    elif func_list == '6':
        print('程序结束')
        sys.exit()
    else:
        print('非法输入，请重试')


def main():
    while True:
        print('~' * 30, '功能列表', '~' * 30)
        func_list = input('1:注册\n2:登录\n3:删除\n4:修改密码\n5:查看信息\n6:退出\n')
        execute(func_list)


if __name__ == '__main__':
    admin_message = []
    root_count = {'username': 'root', 'password': 'root'}
    main()
