from django.db import models

# Create your models here.


class User(models.Model):

    class Meta(object):
        db_table = 'user'
    """投稿者のモデル"""

    name = models.CharField(verbose_name='名前', max_length = 100, null = True, blank = True)
    email = models.EmailField(verbose_name='メールアドレス',max_length = 100, null = True, blank = True)
    comment = models.TextField(verbose_name='コメント',blank = True, null = True, max_length = 1000,)
    #created_at = models.DateTimeField(verbose_name = '作成日時',auto_now_add = True)

    def __str__(self):
        return str(self.name)