'''greater than lessthan'''
list2=[67,89,45,37,34,23,30,41,38]
i=0
sum=0
while i<len(list2):
    if list2[i]>20 and list2[i]<40:
        print(list2[i])
        sum=sum+1
    i+=1
print("sum",sum)