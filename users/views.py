from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from users.models import UserProfile
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from places.forms import PlaceForm
from places.models import Place


class UserLogin(FormView):
    form_class = AuthenticationForm
    template_name = "signin.html"
    success_url = "/list_place"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(self.get_success_url())
        else:
            return super(UserLogin, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(UserLogin, self).form_valid(form)


class UserCreate(CreateView):
    model = User
    template_name = "user_form.html"
    form = PlaceForm
    fields = ['first_name',
              'last_name',
              'email',
              'username',
              'password', ]

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.set_password(form.cleaned_data['password'])
        obj.save()
        return redirect("/signin")


def logout_view(request):
    logout(request)
    return redirect('/')
