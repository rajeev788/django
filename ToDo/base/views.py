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
    content={"method":"create"}

    return render(request,"create.html",context=content)
def edit(request,pk):
    todo = ToDo.objects.get(id=pk)
    if request.method =='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        status=request.POST.get('status')
        todo.name=name
        todo.description=description
        todo.status=status
        todo.save()#this save is a method
        return redirect('home')
    content={"method":"edit",'todo':todo}
    return render (request,"create.html",context=content)
def delete(request,pk):
    todo=ToDo.objects.get(id=pk)
    todo.delete() #thhis delete is also a method
    return redirect('home')