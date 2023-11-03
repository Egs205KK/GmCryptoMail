from django.db import models
from django.contrib.auth.models import User

class Email(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_emails')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_emails')
    subject = models.CharField(max_length=255)
    body = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

class Folder(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='folders')

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')

class Attachment(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='attachments/')
    email = models.ForeignKey(Email, on_delete=models.CASCADE, related_name='attachments')


