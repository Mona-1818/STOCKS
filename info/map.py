def MAP(s,m,l):
    if s==0 and m==0 : 
        sc =8
        mc = 10
        lc = 2 
    elif m ==0 and l==0:
        sc =1
        mc = 9
        lc = 10
    elif s==0 and l==0: 
        sc = 8
        mc = 8
        lc = 4
    elif  s==m and m==l:
        sc = 6
        mc = 7
        lc = 7
    elif s+m <= l:
        sc = 6
        mc = 12
        lc = 2 
    elif m+l <=s:
        sc = 10
        mc = 8
        lc = 2
    elif l+s <= m:
        sc = 6
        mc = 4
        lc = 10
    else:
        sc =2
        mc = 6
        lc = 12 
        
    return sc, mc, lc