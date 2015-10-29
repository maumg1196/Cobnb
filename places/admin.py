from django.contrib import admin
from places.models import Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'city',
                    'place_available',
                    'get_image',
                    'created',
                    'modified',
                    'price',
                    'tipo',
                    'payout_method',)
