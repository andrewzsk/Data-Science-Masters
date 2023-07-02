def add_multiple_numbers():
    lst1=[]
    total=0
    user_input=int(input("How many numbers do you want to add?: "))
    for i in range(user_input):
        user_num=int(input(f"Enter number {i+1}: "))
        lst1.append(user_num)
    #print(lst1)
    total=sum(lst1)
    return total

result =add_multiple_numbers()

print("The sum of the numbers entered by you is: ",result)

