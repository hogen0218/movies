from django.db import models
from users.models import User
from movie_details.models import Movie
from django.utils.timezone import now

# Create your models here.


class Comments(models.Model):
    content = models.TextField(null=False, blank=False, verbose_name='评论内容')
    # 一对多  一个用户可以评论多个电影， 一部电影可以有多个用户评论
    user = models.ForeignKey(User, verbose_name="评论的用户")
    # 一对一
    # user1 = models.OneToOneField
    #被评论电影
    movie = models.ForeignKey(Movie, verbose_name='评论的电影')
    comment_time = models.DateTimeField(default=now, verbose_name='评论时间')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content
