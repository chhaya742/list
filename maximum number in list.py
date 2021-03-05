'''maximum'''
list1=[56,98,78,5,80, 120,56,76,78,70,34,100]
i=0
max=list1[0]
while i<len(list1):
    if max<list1[i]:
        max=list1[i]
    i+=1
print("maximum number",max)