from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from users.models import User
from django.views.generic import FormView
from users.forms import UserRegisterForm, UserLoginForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout


# Create your views here.



class Register(FormView):
    """用户注册"""
    form_class = UserRegisterForm
    success_url = reverse_lazy('movie_index')

    def form_valid(self, form):
        data = form.cleaned_data
        User.objects.create_user(**data)
        return super().form_valid(form)



class Login(FormView):
    """用户登录"""
    form_class = UserLoginForm
    success_url = reverse_lazy('movie_index')

    def form_valid(self, form):
        data = form.cleaned_data
        user = authenticate(**data)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return super().form_valid(form)

    # def get_success_url(self):
    #     return redirect(reverse_lazy('movie_index'))

    # def form_invalid(self, form):
    #     x = form
    #     pass

def user_logout(request):
    logout(request)
    return redirect(reverse_lazy('movie_index'))
