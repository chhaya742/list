char=["a","n","t","a","t","n","n","a","x","u","g","a","x"]
i=0
lit=[]
while i<len(char):
    j=0
    count=0
    while j<len(char):
        if char[i]==char[j]:
            count+=1                                                                                                                                             
        j+=1
    if char [i] in lit:
        i+=1
        continue
    lit.append (char[i])
    print(char[i],"=",count)
print(lit)


