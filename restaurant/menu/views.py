from django.shortcuts import render
from .models import Menu, Lunch, Dinner

# Create your views here.
def home(request):
  menu_items = Menu.objects.all()
  lunch = Lunch.objects.all()
  dinner = Dinner.objects.all()

  context = {"menu_items" : menu_items, "lunch" : lunch, "dinner" : dinner}
  
  return render(request, "index.html", context)