# -*- coding:utf-8 -*-
import re
import sys
from os.path import abspath, dirname

__author__ = 'pf'
import time
import requests


def text_create():
    log_path = dirname(abspath(sys.argv[0]))  # �´�����txt�ļ��Ĵ��·��
    full_path = log_path + '\\log' + '.txt'  # Ҳ���Դ���һ��.doc��word�ĵ�
    file = open(full_path, 'w')
    file.close()


def text_write(content):
    log_path = dirname(abspath(sys.argv[0]))  # �´�����txt�ļ��Ĵ��·��
    full_path = log_path + '\\log' + '.txt'  # Ҳ���Դ���һ��.doc��word�ĵ�
    file = open(full_path, 'r+')
    file.read()
    file.write(content)
    file.close()


class Login:
    # ��ʼ��
    def __init__(self):
        # �����ʱ�䣬��λΪ��
        self.every = 60

    # ģ���¼
    def login(self):
        print(self.getCurrentTime(), u"ƴ��������...")
        url = "http://10.91.200.211/ac_portal/login.php"
        # ��Ϣͷ
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
        # �ύ����Ϣ
        payload = {
            'opr': 'pwdLogin',
            'userName': 'xxxxxxxxx',
            'pwd': 'xxxxxxxxx',
            'rememberPwd': '0',
        }
        try:
            r = requests.post(url, headers=headers, data=payload)
            print(self.getCurrentTime(), u'������...���ڿ�ʼ�������Ƿ�����')
        except:
            print("error")

    # �жϵ�ǰ�Ƿ��������
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

    # ��ȡ��ǰʱ��
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))

    # ������
    def main(self):
        print(self.getCurrentTime(), u"Hi����ӭʹ���Զ���½ϵͳ")
        text_create()
        text_write(self.getCurrentTime() + '������\n')
        while True:
            self.login()
            while True:
                can_connect = self.canConnect()
                if not can_connect:
                    print(self.getCurrentTime(), u"������...")
                    text_write(self.getCurrentTime() + '��⵽�����ж�\n')
                    self.login()
                else:
                    print(self.getCurrentTime(), u"һ������...")
                    text_write(self.getCurrentTime() + '����\n')
                time.sleep(self.every)
            time.sleep(self.every)


login = Login()
login.main()
