# GmCryptoMail
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
