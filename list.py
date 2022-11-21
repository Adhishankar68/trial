#program to create a list
list1=[]
len=int(input("enter the number of elements in list:"))
for i in range (1,len+1):
    element=input("enter your element:")
    list1.append(element)

print("the list is:",list1)
