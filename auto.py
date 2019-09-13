# -*- coding:utf-8 -*-
import re
import sys
from os.path import abspath, dirname

__author__ = 'pf'
import time
import requests


def text_create():
    log_path = dirname(abspath(sys.argv[0]))  # 新创建的txt文件的存放路径
    full_path = log_path + '\\log' + '.txt'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'w')
    file.close()


def text_write(content):
    log_path = dirname(abspath(sys.argv[0]))  # 新创建的txt文件的存放路径
    full_path = log_path + '\\log' + '.txt'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'r+')
    file.read()
    file.write(content)
    file.close()


class Login:
    # 初始化
    def __init__(self):
        # 检测间隔时间，单位为秒
        self.every = 60

    # 模拟登录
    def login(self):
        print(self.getCurrentTime(), u"拼命连网中...")
        url = "http://10.91.200.211/ac_portal/login.php"
        # 消息头
        headers = {
            'Host': "10.91.200.211",
            'Connection': "keep-alive",
            'Content-Length': "56",
            'accept': "*/*",
            'X-Requested-With': "XMLHttpRequest",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
            'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
            'origin': "http://10.91.200.211",
            'Referer': "http://10.91.200.211/ac_portal/proxy.html?template=default&tabs=pwd&vlanid=0&_ID_=0&switch_url=&url=",
            'Accept-Encoding': "gzip, deflate",
            'Accept-Language': "zh-CN,zh;q=0.9",
            # 'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        }
        # 提交的信息
        payload = {
            'opr': 'pwdLogin',
            'userName': 'xxxxxxxxx',
            'pwd': 'xxxxxxxxx',
            'rememberPwd': '0',
        }
        try:
            r = requests.post(url, headers=headers, data=payload)
            print(self.getCurrentTime(), u'连上了...现在开始看连接是否正常')
        except:
            print("error")

    # 判断当前是否可以连网
    def canConnect(self):
        try:
            q = requests.get("http://www.baidu.com")
            m = re.search(r'STATUS OK', q.text)
            if m:
                return True
            else:
                return False
        except:
            print('error')

    # 获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))

    # 主函数
    def main(self):
        print(self.getCurrentTime(), u"Hi，欢迎使用自动登陆系统")
        text_create()
        text_write(self.getCurrentTime() + '已启动\n')
        while True:
            self.login()
            while True:
                can_connect = self.canConnect()
                if not can_connect:
                    print(self.getCurrentTime(), u"断网了...")
                    text_write(self.getCurrentTime() + '侦测到网络中断\n')
                    self.login()
                else:
                    print(self.getCurrentTime(), u"一切正常...")
                    text_write(self.getCurrentTime() + '正常\n')
                time.sleep(self.every)
            time.sleep(self.every)


login = Login()
login.main()
