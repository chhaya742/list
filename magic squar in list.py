a=[[8, 3, 4],
   [1, 5, 9],
   [6, 7, 2]]
i=0
rows=0
while i<len(a):
    j=0
    while j<len(a):
        rows+=a[i][j]
        j+=1    
    i+=1
print(rows)
i=0
colomn=0
while i<len(a):
    j=0
    while j<len(a):
        colomn+=a[i][j]
        j+=1    
    i+=1
print(colomn)
i=0
ld=0
while i<len(a):
    j=0
    n=0
    while j<len(a):
        ld+=a[j][n]
        j+=1
        n+=1
    i+=1
print(ld)   
i=0
rd=0
while i<len(a):
    j=1
    n=1
    while j<=len(a):
        rd+=a[-j][-n]
        j+=1
        n+=1
    i+=1
print(rd)
if rows==colomn==ld==rd:
    print("magic squar")
else:
    print("not magic squar")
    

