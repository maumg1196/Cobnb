from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from places.models import Place
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView, DetailView
from users.models import UserProfile
from django.contrib.auth.models import User


class ListPlace(ListView):
    model = Place
    template_name = "place_list.html"


class CreatePlace(CreateView):
    model = Place
    template_name = "place_form.html"
    fields = ['name',
              'price',
              'type_of_place',
              'description',
              'meters',
              'place_image', ]

    success_url = '/list_place'

    @method_decorator(login_required(login_url="/signin/"))
    def dispatch(self, *args, **kwargs):
        return super(CreatePlace, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        user_django = User.objects.get(id=self.request.user.id)
        form.instance.owner = user_django
        return super(CreatePlace, self).form_valid(form)


class PlaceDetail(DetailView):
    model = Place
    template_name = "place_detail.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PlaceDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PlaceDetail, self).get_context_data(**kwargs)
        return context
