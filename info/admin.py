from django.contrib import admin
from .models import stock_data

# Register your models here.
class displayres(admin.ModelAdmin):
    list_display = ['symbol', 'name', 'price', 'marketcap'] 
    
admin.site.register(stock_data, displayres)

