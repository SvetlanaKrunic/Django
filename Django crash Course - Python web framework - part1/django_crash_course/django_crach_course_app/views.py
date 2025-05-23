from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import ReservationForm

# Create your views here.
def home(request):
    #imported Reservation Form form forms.py
    form = ReservationForm()

    #check if the user have submited the form
    if request.method == 'POST':
        #IF HE DID, redefine our form variable 
        #pass what user put in to ReservationForm
        #request.POST contains info that user inputed
        #pass that info to our form class
        form = ReservationForm(request.POST)
        #check if info is valid
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
        
    #need to pass in this varialbe to index.html file
    return render(request, "index.html", {'form': form})

