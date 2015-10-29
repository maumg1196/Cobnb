from django.db import models
from users.models import UserProfile


class Place(models.Model):
    # Owners
    owners = models.ManyToManyField(UserProfile)

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
    place_image = models.ImageField(upload_to="place_media", null=True, blank=True)

    def get_image(self):
        try:
            return """<img src="{}" style="display: block; width: 60px;"/>""".format(self.event_image.url)
        except:
            return "<h3>No image</h3>"
    get_image.allow_tags = True

    # Money
    price = models.IntegerField(default=0)
    payout_method = models.CharField(max_length=2225)

    # Place's Attributes
    name = models.CharField(max_length=1000, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    meters = models.IntegerField(default=0)
    tipo = models.CharField(max_length=255)

    # Available
    place_available = models.BooleanField(default=True)
