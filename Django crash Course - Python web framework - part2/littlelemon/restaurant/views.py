# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu



# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu(request):
    #vraca svaki manu item
    menu_data = Menu.objects.all()
    return render(request, 'menu.html',{'menu': menu_data})

#menu_item je klikable
#svaki tabel has id colomn
#pk = primary key
def display_menu_item(request, pk = None):
    #if manu item exist
    if pk:
        #get tha manu item with that pk
        menu_item = Menu.objects.get(pk = pk)
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {'menu_item': menu_item})
