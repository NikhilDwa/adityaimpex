from django.shortcuts import render
from .models import Brand


def index(request):
    return render(request, 'homepage.html')


def home(request):
    brand_details = Brand.objects.all().order_by('brand_piece').reverse()
    return render(request, '../templates/home.html', {'brand_details': brand_details})
