from django.forms import ModelForm
from places.models import Place


class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ['name',
                  'price',
                  'type_of_place',
                  'description',
                  'meters']
