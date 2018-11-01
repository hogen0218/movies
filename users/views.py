from django.shortcuts import render, get_object_or_404
from users.models import User
from django.views.generic import FormView
from users.forms import UserRegisterForm
from django.core.urlresolvers import reverse_lazy


# Create your views here.



class Register(FormView):
    """用户注册"""
    form_class = UserRegisterForm()
    success_url = reverse_lazy('movie_index')

    def form_valid(self, form):
        data = form.cleaned_data
        User.objects.create_user(**data)
        return super().form_valid(form)






# def CheckUser(request):
#     username = request.POST['Username']
#     password = request.POST['Password']
#     res = get_object_or_404(User, {'username': username, 'password': password})
