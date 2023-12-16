from .models import stock_data
def assign(s, m, l, x, ): 
    sc = s
    mc = m 
    lc = l
    short = []
    ps = []
    pg = []
    mid = []
    pm = []
    ph = []
    large =[]
    pl =[]
    pi= []
    assigned_stock = []  
    
    sc_stock = stock_data.objects.filter(cap = 1)  
    mc_stock =  stock_data.objects.filter(cap = 2)  
    lc_stock = stock_data.objects.filter(cap = 3)    
     
    for i in sc_stock:
        short.append(i.symbol)
        a = stock_data.objects.get(symbol = i.symbol)  
        ps.append(float(a.potential))
        pg.append(a.goldenratio)
        
    for j in mc_stock:
        mid.append(j.symbol)
        a = stock_data.objects.get(symbol = i.symbol)  
        pm.append(float(a.potential))
        ph.append(a.goldenratio)
    for k in lc_stock: 
        large.append(k.symbol) 
        a = stock_data.objects.get(symbol = i.symbol)  
        pl.append(float(a.potential))
        ph.append(a.goldenratio)
        
    
    while(sc>0): 
        try:
            max1 = max(pl)
            a = pl.index(max1)
            assigned_stock.append()
            pl.remove(max1)  
            
            
            
            
    except: pass
    
        
        
    return d