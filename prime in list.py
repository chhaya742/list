a=[4,7,5,23,12,9,6,45,15,55,1]
index=0
l=len(a)
while index<l:
    j=1
    f=0
    while j<=a[index]:
        if a[index]%j==0:
            f+=1
        j+=1
    if f==2:
        print(a[index],"prime")  
    else:
        print(a[index],"not prime")
    index+=1
        