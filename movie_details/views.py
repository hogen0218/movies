from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from users.forms import UserRegisterForm, UserLoginForm
from .models import Movie
# Create your views here.


class Index(TemplateView):
    """电影首页展示"""
    template_name = 'movies/index.html'
    user_register_form = UserRegisterForm()
    user_login_form = UserLoginForm()

    def get_context_data(self, **kwargs):
        kwargs['user_register_form'] = self.user_register_form
        kwargs['user_login_form'] = self.user_login_form
        kwargs['movies'] = Movie.objects.all()
        kwargs['featured_movies'] = Movie.objects.filter(hotkind__name='featured')
        kwargs['top_view'] = Movie.objects.filter(hotkind__name='Top View')
        kwargs['Top_Rating'] = Movie.objects.filter(hotkind__name='Top Rating')
        kwargs['Recently_Added'] = Movie.objects.filter(hotkind__name='Recently Added')
        return super().get_context_data(**kwargs)



class Single(DetailView):
    template_name = 'movies/single.html'
    model = Movie
    context_object_name = 'single_detail'

    # def get_context_data(self, **kwargs):
    #     kwargs['movies'] = Movie.objects.all()
    #     return super().get_context_data(**kwargs)

