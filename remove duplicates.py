#5.Write a Python program to remove duplicates from a list.

list1=[44,44,44,48,43,49,49,49,50]
no_dup=[]

for i in list1:
    if i not in no_dup:
        no_dup.append(i)
print(no_dup)

#new=set(list1)
#print(list(new))
#print("Now there are {} variables in the list as against {}".format(len(new),len(list1)))

