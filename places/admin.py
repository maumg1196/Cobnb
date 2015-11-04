from django.contrib import admin
from places.models import Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'city',
                    'place_available',
                    'get_image',
                    'created',
                    'modified',
                    'price',
                    'type_of_place',
                    'payout_method',)

    list_display_links = ('name',)
    list_filter = ('city', 'place_available',)
    list_editable = ('payout_method', 'price')
    readonly_fields = ('get_image',)
