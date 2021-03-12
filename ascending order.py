a=[3,7,5,4,5,9,2,6,4,8]
i=0
l=len(a)
while i<l:
    j=0
    while j<l:
        if a[i]<a[j]:
            tem=a[i]
            a[i]=a[j]
            a[j]=tem
        j+=1
    i+=1
print(a)




