from django.shortcuts import render
from django.http import HttpResponse
from.models import ToDo #needed
# Create your views here.
def home(request): #neededHttpResponse
    objects = ToDo.objects.all()
    content = {"todos":objects} #making the dictionary data to pass on templates
    return render(request,"index.html",context=content)

def create(request):
    return render(request,"create.html")