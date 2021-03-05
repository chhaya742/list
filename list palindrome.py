'''palondrome'''
t=input("enter string")
a=list(t)
i=1
b=[]
while i<=len(a):
    print(a[-i])
    b.append(a[-i])
    i+=1
if a==b:
    print("palindrome")
else:
    print("not")
