n=[10,11,12,13,14,17,18,19]
i=0
l=len(n)
c=[]
while i<l:
    j=0
    while n[j]<n[i]:
        if n[i]+n[j]==30:
            c.append([n[j],n[i]])
        j+=1   
    i+=1
print(c)