from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcomePage(request):
    return render(request,"clashofclans/welcome.html")