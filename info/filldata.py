import csv 
from django.core.management.base import BaseCommand  
from .models import stock_data

import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        file = 'D:\stock\stock\info\output.csv'
        i = 0
        with open(file, 'r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                print(row[0])
                if i == 0:
                    continue
                else:
                    stocks_data.objects.create(symbol = row[0], name = row[1], price = row[2], changesPercentage = row[3], change = row[4], dayLow = row[5], dayHigh =row[6],  yearHigh =row[7], yearLow =row[8],marketcap= row[9],  priceAvg50 = row[10], priceAvg200 =row[11], exchange = row[12], volume = row[13], avgVolume = row[14], open =row[15], previousClose = row[16], pe = row[17], earningsAnnouncement = row[18], sharesOutstanding = row[19])
                i += 1
       