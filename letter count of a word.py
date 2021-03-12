name=["missippi"]
i=0
a=list(name[i])
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i+=1
j=0
while j<len(b):
    k=0
    count=0
    while k<len(a):
        if b[j]==a[k]:
            count+=1
        k+=1
    print(b[j],"=",count) 
    j+=1


