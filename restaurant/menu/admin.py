from django.contrib import admin
from .models import Menu, Lunch, Dinner

# Register your models here.


class MenuAdmin(admin.ModelAdmin):
  list_display = ["name", "desc", "price", "category"]
  search_fields = ["name"]

admin.site.register(Menu, MenuAdmin)

@admin.register(Lunch)
class LunchAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name', 'category')

@admin.register(Dinner)
class DinnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name', 'category')