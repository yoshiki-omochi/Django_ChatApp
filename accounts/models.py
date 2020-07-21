from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """拡張ユーザモデル"""

    class Meta:
        verbose_name_plural = 'CustomUser'





class SignUpUser(models.Model):

    class Meta(object):
        db_table = 'singnupuser'
    """sign upしたユーザ"""

    name = models.CharField(verbose_name='名前', max_length = 100, null = True, blank = True)
    email = models.EmailField(verbose_name='メールアドレス',max_length = 100, null = True, blank = True)
    password = models.CharField(verbose_name='パスワード', max_length = 100, null = True, blank = True)

    def __str__(self):
        return str(self.name)