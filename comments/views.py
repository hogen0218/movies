from django.shortcuts import render,redirect, HttpResponse
from django.views.generic import FormView
from .forms import CommentsForm
from django.core.urlresolvers import reverse_lazy
from .models import Comments


# Create your views here.


class CommentView(FormView):
    form_class = CommentsForm
    template_name = 'movies/single.html'


    def form_valid(self, form):
        user = self.request.user  # 从request中找出user
        if not user.pk:       # 如果user 不存在,表示没有登录
            return HttpResponse('fail')
        Comments.objects.create(user=user, **form.cleaned_data)   # 如果user存在 创建一个评论到数据库  user=user 左边表示Comments的字段 右边是登录的user
        url = self.request.META['HTTP_REFERER']   # 表示返回本页面  在debug 中可以看到
        return redirect(url)

    def form_invalid(self, form):
        url = self.request.META['HTTP_REFERER']
        return redirect(url)
