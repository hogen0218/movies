from django.shortcuts import render
from django.views.generic import TemplateView
from users.forms import UserRegisterForm

# Create your views here.


class Index(TemplateView):
    """电影首页展示"""
    template_name = 'movies/index.html'
    user_register_form = UserRegisterForm()


    def get_context_data(self, **kwargs):

        kwargs['user_register'] = self.user_register_form
        return super().get_context_data(**kwargs)






