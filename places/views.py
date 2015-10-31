from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from places.models import Place


@login_required(login_url="/signin")
def home(request):
    context = {
        'places': Place.objects.all()
    }
    return render(request, 'places.html', context)
