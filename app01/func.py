import smtplib
from email.mime.text import MIMEText
from email.header import Header

import os
import re
import json
import time


USERS_PATH = "./users.json"



# def send_email(smtp_server:str, smtp_port:int, sender:str, smtp_code:str, receiver:str, subject:str, content:str) -> None:
#     '''
#     用来发送一封邮件
    
#     参数：
#     smtp_server: smtp服务器, str
#     smtp_port: smtp端口, int
#     sender: 发件人, str
#     smtp_code: 授权码, str
#     receiver: 收件人, str
#     subject: 邮件主题, str
#     content: 邮件内容, str

#     返回值：
#     return None

#     '''
#     # 构造邮件内容
#     message = MIMEText(content, 'plain', 'utf-8')
#     message['From'] = Header(sender)
#     message['To'] = Header(receiver, 'utf-8')
#     message['Subject'] = Header(subject, 'utf-8')

#     try:
#         # 连接SMTP服务器
#         server = smtplib.SMTP(smtp_server, smtp_port)
#         # 使用TLS加密
#         server.starttls()
#         # 登录SMTP服务器
#         server.login(sender, smtp_code)
#         # 发送邮件
#         server.sendmail(sender, receiver, message.as_string())
#         print("邮件发送成功")
#     except Exception as e:
#         print("邮件发送失败:", str(e))
#     finally:
#         # 关闭连接
#         server.quit()

def send_email(smtp_server:str, smtp_port:int, sender:str, smtp_code:str, receiver:str, subject:str, content:str) -> None:
    '''
    用来发送一封邮件
    
    参数：
    smtp_server: smtp服务器, str
    smtp_port: smtp端口, int
    sender: 发件人, str
    smtp_code: 授权码, str
    receiver: 收件人, str
    subject: 邮件主题, str
    content: 邮件内容, str

    返回值：
    return None

    '''
    # 构造邮件内容
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header(sender)
    message['To'] = Header(receiver, 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')

    try:
        # 连接SMTP服务器
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo() # 添加这一行代码
        # 使用TLS加密
        server.starttls()
        # 登录SMTP服务器
        server.login(sender, smtp_code)
        # 发送邮件
        server.sendmail(sender, receiver, message.as_string())
        print("邮件发送成功")
    except Exception as e:
        print("邮件发送失败:", str(e))
    finally:
        # 关闭连接
        server.quit()



def isEmailAddress(string:str) -> bool:
        '''
        用来判断所给的字符串是否为邮箱

        参数：
        string: 要判断是否为邮箱格式的字符串, str

        返回值：
        return bool
        '''
        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        match = re.search(pattern, string)
        return match


def loadUsers() -> dict:
    '''
    用于加载用户数据，不存在就新建一个

    参数：
    无

    返回值：
    return dict （json对象）

    '''
    if not os.path.exists(USERS_PATH):
        with open(USERS_PATH, 'w') as f:
            f.write("{}")
    with open(USERS_PATH, 'r') as f:
        users = json.load(f)
    return users


def addSender():
    '''
    用于添加一个用户数据
    
    参数：
    无

    返回值：
    return None

    '''
    while True:
        sender = input("请输入您的邮箱地址(目前只支持qq邮箱)：")
        if not isEmailAddress(sender):
            print("请输入正确的邮箱格式！")
            continue
        else:
            break
    smtp_code = input("请输入smtp授权码：")
    nickname = input("请输入为本邮箱取的昵称：")
    smtp_server = "smtp.qq.com"
    smtp_port = 25
    data = {
        "sender":sender,
        "smtp_code":smtp_code,
        "smtp_server":smtp_server,
        "smtp_port":smtp_port,
    }
    users = loadUsers()
    users[nickname] = data

    with open(USERS_PATH, 'w') as f:
        json.dump(users, f, indent=4)
    
def initialize():
    if not os.path.exists("./users.json"):
        print("初次使用，请按提示完成注册。")
        time.sleep(0.8)
        addSender()
        print("初始化完成！")
        print("加载主界面...")


def getSender(users:dict, choice:str) -> bool:
    '''
    用于判断输入的用户名是否存在

    '''
    for k in users.keys():
        if k == choice:
            return users[k]
        else:
            return None


def login() -> dict:
    '''
    用于用户登录

    '''
    while True:
        with open(USERS_PATH, 'r') as f:
            users = json.load(f)
        choice = input("请输入要登录的用户名：")
        user = getSender(users, choice)
        if user == None:
            print("输入的用户不存在，请重新输入！")

            continue
        else:
            return user
        
        


         
# # 邮件配置信息
# smtp_server = 'smtp.qq.com'   # SMTP服务器地址
# smtp_port = 25                    # SMTP服务器端口号
# sender = '2276795170@qq.com'  # 发件人邮箱
# smtp_code = 'pjxwviexmfxgeacd'         # 发件人邮箱密码
# receiver = 'egs205kk@outlook.com'  # 收件人邮箱
# subject = '6'                 # 邮件主题
# content = '6'          # 邮件正文
