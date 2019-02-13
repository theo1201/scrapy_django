from django.db import models

# Create your models here.

class Person(models.Model):
    title = models.CharField(max_length=255,help_text="标题")
    content = models.TextField(help_text="内容")
    link = models.URLField(help_text="链接")
    editor = models.CharField(max_length=120,help_text="作者")
    publishtime = models.CharField(max_length=120,help_text="发表日期")

