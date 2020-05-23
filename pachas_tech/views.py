from django.http import HttpResponse
from django.shortcuts import render




def test(request):
    return render (request, 'pachas_tech/index.html')
# Create your views here.
