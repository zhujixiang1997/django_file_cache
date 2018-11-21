import os
from random import random
from django.db import models
from django.core.files.storage import FileSystemStorage
from datetime import datetime

# 图片名字+图片格式
class ImageFileStorage(FileSystemStorage):
    # /upload_to/img/图片的名字
    def _save(self, name, content):
        old_name = name.split('/')[-1]
        # 图片后缀名
        suffix_name = old_name.split('.')[-1]
        # IMG_201811201414
        prefix_name = f"IMG_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}{str(random.randint(100000,999999))}"
        image_path = os.path.dirname(name)
        name = os.path.join(image_path,f'{prefix_name}.{suffix_name}')
        return super()._save(name,content)


class Shop(models.Model):
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=100)
    # 框架自动配置了media
    # img = models.ImageField(upload_to='shop/img/',storage=ImageFileStorage)
    # img = models.ImageField(upload_to='shop/%Y/%m/%d/')
    class Meta:
        db_table = 'shop'



class Img(models.Model):
    img = models.ImageField(upload_to='shop/img/', storage=ImageFileStorage)
    # 1 表示商品图片
    # 2 表示用户图片
    type = models.SmallIntegerField()
    name = models.ForeignKey(Shop,on_delete=models.CASCADE)
    name = models.ForeignKey(Shop,on_delete=models.CASCADE)