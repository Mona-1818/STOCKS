from django.contrib import admin
from .models import UserProfile, portfolio

# Register your models here.
class displayres(admin.ModelAdmin):
    list_display = [ 'name','email', 'Portfolio_amount', 'occupation'] 
 
class displayport(admin.ModelAdmin):
    list_display = ['username', 'companyname', 'quantity', 'price'] 
      
admin.site.register(UserProfile, displayres)
admin.site.register(portfolio, displayport)
