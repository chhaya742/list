binary_number=[1,0,1,0,1]
i=1
sum=0
k=0
while i<=len(binary_number):
    b=(2**k)*binary_number[-i]
    sum+=b
    i+=1
    k+=1
print(sum)
