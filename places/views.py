from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from places.models import Place
from places.forms import PlaceForm


@login_required(login_url="/signin")
def home(request):
    context = {
        'places': Place.objects.all()
    }
    return render(request, 'places.html', context)


def new_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        print request.POST
        if form.is_valid():
            form.save()
            return redirect(reverse('places:home'))
        else:
            print("fallo")
            return render(request, 'create_place.html', {'place_form': form})

    form = PlaceForm()
    return render(request, 'create_place.html', {'place_form': form})
