''' positive nagative'''
li=[5,-6,4,0,-7,0,-9,-5]
i=0
b=[]
while i<len(li):
    if li[i]>0:
        print("positive",li[i])
    elif li[i]<0:
        print("negitive",li[i])
    else:
        print("zero",li[i])
    i+=1

# count negetive positive from user 

user1=int(input("size of list"))
i=0
list2=[]
while i<user1:
    u=int(input("enter number"))
    list2.append(u)
    i+=1
print(list2)
j=0
p=[]
n=[]
z=[]
new_list=[]
while j<len(list2):
    if list2[j]==0:
        z.append(list2[j])
    elif list2[j]<0:
        n.append(list2[j])
    else:
        p.append(list2[j])
    j+=1
# print("zero",z)
# print("negetive",n)
# print("positive",p)
new_list.append(z)
new_list.append(n)
new_list.append(p)
print(new_list)






