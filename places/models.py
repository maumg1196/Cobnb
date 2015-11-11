from django.db import models
from django.contrib.auth.models import User
from users.models import UserProfile


CHOICE_PLACES = (
    ('F', 'Food'),
    ('T', 'Technologic'),
    ('M', 'Medicin'),
    ('S', 'School'),
)

CHOICE_PAYOUT = (
    ('D', 'Tarjeta de Debito'),
    ('C', 'Tarjeta de Credito'),
    ('E', 'Efectivo'),
    ('P', 'PayPal'),
)


class Place(models.Model):

    owner = models.ForeignKey(User, null=True, blank=True)

    # Place's Address
    city = models.CharField(max_length=255)
    number = models.CharField(max_length=10)
    state = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    suite = models.CharField(max_length=15, null=True, blank=True)
    zip_code = models.CharField(max_length=8)

    # Meta Data
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # Image
    place_image = models.ImageField(upload_to="static/img/place_media", null=True, blank=True)

    # Money
    price = models.FloatField(default=0.0)
    payout_method = models.CharField(max_length=2225, choices=CHOICE_PAYOUT, null=True, blank=True)

    # Place's Attributes
    name = models.CharField(max_length=1000, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    meters = models.IntegerField(default=0)
    type_of_place = models.CharField(max_length=255, choices=CHOICE_PLACES, null=True, blank=True)

    # Available
    place_available = models.BooleanField(default=True)

    def get_image(self):
        try:
            return u'<img src="%s" style="display: block; width: 60px;"/>' % self.place_image.url
        except:
            return "<h3>No image</h3>"
    get_image.allow_tags = True
