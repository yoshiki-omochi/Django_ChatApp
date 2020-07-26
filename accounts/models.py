from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """拡張ユーザモデル"""

    class Meta:
        verbose_name_plural = 'CustomUser'
        db_table = 'singnupuser'

    def __str__(self):
        return str(self.username)




class SignUpUser(models.Model):
    """sign upしたユーザ"""

    class Meta(object):
        db_table = 'upuser'
    
    username = models.CharField(verbose_name='名前', max_length = 100, null = True, blank = True)
    email = models.EmailField(verbose_name='メールアドレス',max_length = 100, null = False, blank = False)
    password = models.CharField(verbose_name='パスワード', max_length = 100, null = False, blank = False)

    def __str__(self):
        return str(self.username)


class LoginUser(models.Model):
    
    """log inするユーザ"""
    class Meta(object):
        db_table = 'loginuser'

    username = models.CharField(verbose_name='名前', max_length = 100, null = True, blank = True)
    password = models.CharField(verbose_name='パスワード', max_length = 100, null = False, blank = False)

    def __str__(self):
        return str(self.username)