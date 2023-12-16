from .models import stock_data
def assign(s, m, l, x ): 
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
        try:
            y =float(a.potential)
        except:
            y = 0
        ps.append(y)
        pg.append(a.goldenratio)
        
    for j in mc_stock:
        mid.append(j.symbol)
        a = stock_data.objects.get(symbol = i.symbol) 
        try:
            y =float(a.potential)
        except:
            y = 0
        pm.append(y)
        ph.append(a.goldenratio)
    for k in lc_stock: 
        large.append(k.symbol) 
        a = stock_data.objects.get(symbol = i.symbol)  
        try:
            y =float(a.potential)
        except:
            y = 0
        pl.append(y)
        pi.append(a.goldenratio)
        
    
    while(sc>=0): 
        try:
            max1 = max(ps)
            a = ps.index(max1)
            if short[a] in x:
                continue
            else:
                assigned_stock.append(short[a])
            ps.remove(max1)   
            sc -=1
        except: pass
    while(mc>=0): 
        try:
            max1 = max(pm)
            a = pm.index(max1)
            if mid[a] in x:
                continue
            else:
                assigned_stock.append(mid[a])
            pm.remove(max1)   
            mc -=1
        except: pass
    while(lc>=0): 
        try:
            max1 = max(pl)
            a = pl.index(max1)
            if mid[a] in x:
                continue
            else:
                assigned_stock.append(mid[a])
            pl.remove(max1)   
            lc -=1
        except: pass
        
        
    return assigned_stock