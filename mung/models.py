from django.db import models

class user(models.Model):
    user_id = models.CharField(max_length=50)
    user_pwd = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'