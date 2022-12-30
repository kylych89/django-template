from django.db import models


class User(models.Model):
    username = models.CharField(max_length=55)
    password = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
