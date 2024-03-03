from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,"index.html")

def browse_index(request):
    filmler=Movies.objects.all()
    search=""
    context={

    }
    if request.GET.get("search"):
        search=request.GET.get("search")
        filmler=filmler.filter(
            Q(isim__icontains=search) |
            Q(kategori__name__icontains=search)
        )

    try:
        izleyen=Izlenenler.objects.get(user=request.user)
        izlenen=izleyen.izlenen.all()
        context={ 
        'filmler':filmler,
        "izlenen":izlenen
        }
    
    except:
        context={ 
            'filmler':filmler,
        }
    return render(request,"browse-index.html",context)