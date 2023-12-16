from django.db import models

# Create your models here.
class stock_data(models.Model):
    symbol = models.CharField(max_length= 20, blank=True, null=True)
    name = models.CharField(max_length= 1000, blank=True, null=True)
    price = models.CharField(max_length= 30,blank=True, null=True)
    changesPercentage = models.CharField(max_length= 30,blank=True, null=True)
    change = models.CharField(max_length= 30,blank=True, null=True) 
    dayLow = models.CharField(max_length= 30,blank=True, null=True) 
    dayHigh = models.CharField(max_length= 30,blank=True, null=True)
    yearHigh = models.CharField(max_length= 30,blank=True, null=True)
    yearLow = models.CharField(max_length= 30,blank=True, null=True) 
    potential = models.CharField(max_length= 30,blank=True, null=True) 
    marketcap = models.CharField(max_length= 30,blank=True, null=True) 
    cap = models.CharField(max_length= 1,default=False)
    priceAvg50 = models.CharField(max_length= 30,blank=True, null=True) 
    priceAvg200 = models.CharField(max_length= 30,blank=True, null=True) 
    goldenratio = models.BooleanField(default= False)
    exchange = models.CharField(max_length= 30,blank=True, null=True)
    volume = models.CharField(max_length= 30,blank=True, null=True)
    avgVolume = models.CharField(max_length= 30,blank=True, null=True) 
    open = models.CharField(max_length= 30,blank=True, null=True) 
    previousClose = models.CharField(max_length= 30,blank=True, null=True) 
    pe = models.CharField(max_length= 30,blank=True, null=True)
    earningsAnnouncement = models.CharField(max_length= 30,blank=True, null=True)
    sharesOutstanding = models.CharField(max_length= 30,blank=True, null=True) 
    
    def __str__(self) -> str:
        return str(self.symbol)
   
 

# from .filldata import Command    
# obj = Command()
# obj.handle()
    
    
