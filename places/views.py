from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from places.models import Place
from places.forms import PlaceForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'places.html'


class CreatePlace(CreateView):
    model = Place
    template_name = "place_form.html"
    fields = ['name',
              'price',
              'type_of_place',
              'description',
              'meters',
              'place_image', ]

    success_url = '/'

    @method_decorator(login_required(login_url="/signin/"))
    def dispatch(self, *args, **kwargs):
        return super(CreatePlace, self).dispatch(*args, **kwargs)

# super(CreatePlace, self)
