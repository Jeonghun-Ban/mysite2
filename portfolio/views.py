from django.shortcuts import render
from .models import Portfolio

# Create your views here.
def gallery(request):
    portfolio = Portfolio.objects
    return render(request, 'gallery.html', {'portfolios': portfolio})