from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import ToDo #needed
# Create your views here.
def home(request): #neededHttpResponse
    objects = ToDo.objects.all()
    content = {"todos":objects} #making the dictionary data to pass on templates
    return render(request,"index.html",context=content)
#this is for writing the data from create page to the backend...
def create(request):
    if request.method =="POST": 
       
        name=request.POST.get("name") #this is from create.html
        description=request.POST.get("description")
        status=request.POST.get("status")

        ToDo.objects.create(name=name,description=description,status=status)
        return redirect("home")

    return render(request,"create.html")