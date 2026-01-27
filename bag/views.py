from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def view_bag(request):
    return render(request, 'bag/bag.html')