# GmCryptoMail
!!因为项目规划改了决定抛弃网站改成做服务器端和客户端软件，所以这个半成品作废。

学校的任务罢了, 配环境大概也麻烦的很, 虽然用的MIT许可但是应该没人能用得动


基于国密算法的安全电子邮件网站

使用前先配置```./mailsite/settings.py```里的设置
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'example@qq.com'
EMAIL_HOST_PASSWORD = 'example'
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'example@qq.com'
```
