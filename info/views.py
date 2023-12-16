from django.shortcuts import render
import csv
from django.http import HttpResponse
from .models import stock_data
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from account.models import portfolio
from .map import MAP
from .assign import assign

# Create your views here.
@api_view(['GET'])
def Allstock(request):
    x = stock_data.objects.all()
    for i in x:
        print({i.symbol})
        print({i.name})
    return Response( {'message': 'User profile not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def User_portfolio(request, username):
    hold = []
    x = portfolio.objects.filter(username=username)
    stocks = {}
    
    for y in x:
        hold.append(y.companyname) 
    return Response({'stocks': hold}, status=status.HTTP_200_OK)
    
    
@api_view(['GET'])
def Personal_recommend(request, username):
    small_cap = 0
    large_cap = 0
    mid_cap = 0
    hold = []
    x = portfolio.objects.filter(username=username)
    for y in x:
        hold.append(y.companyname)
        f_cap = stock_data.objects.get(symbol=y.companyname) 
        if float(f_cap.cap) ==1:
            small_cap += 1
        elif float(f_cap.cap) == 2:
            mid_cap += 1
        else:
            large_cap += 1   
    sc, mc, lc = MAP(small_cap, mid_cap, large_cap)
    stock = assign(sc,mc,lc,hold)
    print(stock)    
    if small_cap > mid_cap and small_cap > large_cap:
        z = "sc"
    elif mid_cap >small_cap and mid_cap > large_cap:
        z = "mc"
    else: 
        z = "lc"

    
        
    return Response( {'message': 'User profile not found.'}, status=status.HTTP_404_NOT_FOUND)
# def fillstock(request):
#     file = r'D:\stock\stock\info\output.csv'
#     i = 0
#     with open(file, 'r', newline='', encoding='utf-8') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         for row in csv_reader:
#             if row['marketCap'] =='' or float(row['marketCap'])== 0.0 :
#                 pass
#             else:
#                 if row['yearHigh']=='' or row['price']=='':
#                     x = 'NA'
#                 else:
#                     x = ((float(row['yearHigh'])-float(row['price']))/float(row['yearHigh']))*100
#                 if row['priceAvg50'] =='' or row['priceAvg200']=='':
#                     y = False
#                 elif float(row['priceAvg50'])>float(row['priceAvg200']):
#                     y = True
#                 else: y = False
#                 if float(row['marketCap'])<2000000000:
#                     z= 1
#                 elif float(row['marketCap'])>2000000000 and  float(row['marketCap'])<10000000000:
#                     z = 2
#                 else:
#                     z = 3
#                 instance = stock_data(
#                     symbol=row['symbol'],
#                     name=row['name'],
#                     price=row['price'],
#                     changesPercentage=row['changesPercentage'],
#                     change=row['change'],
#                     dayLow=row['dayLow'],
#                     dayHigh=row['dayHigh'],
#                     yearHigh =row['yearHigh'],
#                     yearLow=row['yearLow'],
#                     potential = x,
#                     marketcap=row['marketCap'],
#                     cap= z,
#                     priceAvg50=row['priceAvg50'],
#                     priceAvg200=row['priceAvg200'],
#                     goldenratio= y,
#                     exchange=row['exchange'],
#                     volume=row['volume'],
#                     avgVolume=row['avgVolume'],
#                     open=row['open'],
#                     previousClose=row['previousClose'],
#                     pe=row['pe'],
#                     earningsAnnouncement=row['earningsAnnouncement'],
#                     sharesOutstanding=row['sharesOutstanding'],
#                 )
#                 instance.save()
#             i += 1
#     return HttpResponse("Values saved successfully.")

# def remove(request):
#     x = stock_data.objects.all()
#     x.delete()
#     return HttpResponse("delete successfully.")
        