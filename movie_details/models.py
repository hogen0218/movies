from django.db import models
from django.utils import timezone
# Create your models here.


class Kind(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='电影分类')

    class Meta:
        verbose_name = '电影分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}".format(self.name)    #在admin 系统中显示分类名字


class HotKind(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='featured分类')

    class Meta:
        verbose_name = 'featured分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}".format(self.name)


class Movie(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, unique=True, verbose_name='电影标题')
    desc = models.CharField(max_length=1024, default='现在没有电影简介', verbose_name='电影简介')
    release_date = models.DateTimeField(default=timezone.now, verbose_name='上映时间')
    find = models.ManyToManyField(Kind)
    images = models.ImageField(null=True)
    hotkind = models.ManyToManyField(HotKind)

    class Meta:
        verbose_name = '电影信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}".format(self.title)   # 在admin系统中显示电影名字
