print("''''''🙏WELCOME🙏''''''")
print()
question=[
    "How many continents are there?",       
    "What is the capital of India?",            
    "NG mei kaun se course padhaya jaata hai?"  
]
option=[
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh","bhopal","Delhi","chennai"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
solution=[3,3,1]
l=len(question)
index=0
tem1=0
tem2=1
count = 0
amount=10000
tem3=1
while index<l:
    print(question[index])
    j=0
    num=1
    while j<len(option[index]):
        print(num,".",option[index][j])
        num+=1
        j+=1    
    # solution=[3,3,1]
    m=["3.seven","4.eight","2.bhopal","3.delhi","1.Software Engineering", "2.Counseling"]
    user_input_1=input("do  you want life line you  have one life line,yes or no..")
    if user_input_1=="yes":
        print("50-50")
        if count == 0:
            print(m[index+tem1])
            print(m[index+tem2])
            user_input_2=int(input("enter answer"))
            if solution[index]==user_input_2:
                print("right👏👏👏")
                print()
                count = count + 1
            else:
                print("wrong😢😢")
                break
        else:
            print("you already used lifeline.")
            u=int(input("enter answer"))
            if solution[index]==u:
                print("right👏👏👏")
                print()
            else:
                print("wrong😔😔")
                break
    elif user_input_1=="no":
        user_input_2=int(input("enter answer"))
        if solution[index]==user_input_2:
            print("right👏👏👏")
            print()
        else:
            print("wrong😔😔")
            break
    else:
        print("something went wrong")
        break
    index+=1
    tem1+=1
    tem2+=1
    print("congratulation you won",amount,"amount\n🎊 🎉🎊 🎉")
    print()
    tem3+=1
    amount*=tem3

        






    







        

    



    


    

    


    




    

    
    







    

