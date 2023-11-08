from django.shortcuts import render, HttpResponse

from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from app01.models import *
# Create your views here.



# Create your views here.

#主页
def index(request):
    if request.method == "GET":
        return render(request, 'index-temp.html')
    if request.method == 'POST':
        sender = request.POST.get('sender')
        stmp_code = request.POST.get('stmp-code')
        receiver = request.POST.get('receiver')
        subject = request.POST.get('subject')
        content = request.POST.get('content')

        send_mail(
            subject,
            content,
            sender,
            [receiver],
            auth_user=sender,  # 使用发件人邮箱作为用户名
            auth_password=stmp_code,  # 使用用户输入的授权码作为密码
            fail_silently=False,
        )
    return HttpResponse('发送成功')

#注册
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')

            # 创建User对象并保存到数据库中
            user = User(username=username, password=password, email=email)
            user.save()
            return render(request, 'register_success.html')           
        except:
            return render(request, 'register_failed.html')

        
# #登录
# def login(request):
#     if request.method == 'GET':
#         return render(request,'login.html')
    
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 使用Django内置的authenticate函数检查用户名和密码是否匹配
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            # 使用Django内置的login函数进行用户登录
            login(request, user)
            return render(request, 'index.html') # 登录成功后重定向到主页
        else:
            # 如果用户名或密码不匹配，返回错误信息给用户
            error_msg = "用户名或密码错误，请重新输入！"
            return render(request, 'login.html', {'error_msg': error_msg})


#关于我们
def about(request):
    if request.method == 'GET':
        return render(request, 'about.html')




def user_index(request):
    return render(request, 'user_index.html')
