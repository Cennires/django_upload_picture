from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models
import uuid
import os
# Create your models here.
# 创建的对象必须继承Model

def path_and_rename(instance,filename):
    upload_to = 'image'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10],ext)
    return os.path.join(upload_to,filename)


class Photo(models.Model):
    img = models.ImageField('图片', default='',upload_to=path_and_rename,blank=True)
    title = models.CharField('标题', max_length=128,)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('MytestApp:pic_detail',args=[str(self.pk)])
