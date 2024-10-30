from django.shortcuts import render

from smartphones.models import Manufacturer
from smartphones.forms import SmartphoneForm

# Create your views here.

def smartphone_index(request):
    manufacturer = Manufacturer.objects.all()

    context = {
        'manufacturer': manufacturer
    }

    return render(request,'smartphone/smartphones.html', context)


def register_smartphone(request):
    if request.method == "POST":
        form = SmartphoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manufacturer')
    else:
       form = SmartphoneForm()

    context = {
           'form': form
    }

    return render(request, 'smartphone/register_smartphone.html', context)