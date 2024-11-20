from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    area = models.Area.objects.all()
    context = {
        'area': area
    }
    return render(request, 'app/index.html', context)