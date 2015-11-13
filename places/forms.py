from django.forms import ModelForm
from places.models import Place


class PlaceForm(ModelForm):
    def save(self, user=None):
        self.instance.owner = user
        super(PlaceForm, self).save()

    class Meta:
        model = Place
        fields = ['name',
                  'price',
                  'type_of_place',
                  'description',
                  'meters',
                  'place_image', ]
# @gabocharles wairamexico
