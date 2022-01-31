n=int(input("enter the limit:"))
list=[]
for i in range(n):
 a=int(input("enter the number:"))
 list.append(a)
print(list)
list1=[x**2 for x in list]
print(list1)
