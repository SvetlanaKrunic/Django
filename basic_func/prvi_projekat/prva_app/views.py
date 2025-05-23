from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDosItems

# Create your views here.
def home(request):
    #return render(request,"home.html")
    return HttpResponse("Hello World!")

def todos(request):
    #query them from DB
    items = ToDosItems.objects.all()

                                      #pass the python dictionary that contsaines
                                      #variables with key mapping pairs that we want
                                      #to see in todo.html
    return render(request, "todo.html",{"todos":items})
