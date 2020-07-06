from django.db import models

# Create your models here.


class TestUser(models.Model):
    """投稿者のモデル"""

    name = models.CharField(max_length = 100, null = True, blank = True)
    email = models.EmailField(max_length = 100, null = True, blank = True)
    comment = models.TextField(blank = True, null = True, max_length = 1000,)
    #created_at = models.DateTimeField(verbose_name = '作成日時',auto_now_add = True)

    def __str__(self):
        return self.name