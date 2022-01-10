
l1 = [20, 40, 30, 10, 90]
l2 = [50, 25, 40, 90]
print("length of list1:",len(l1))
print("length of list1:",len(l2))
if len(l1)==len(l2):
    print("two lists are same length")
total = sum(l1)
print("sum of the list1:", total)
total = sum(l2)
print("sum of the list2:", total)
if sum(l1) == sum(l2):
    print("two lists sum are equal")
print("commen values:")
for i in l1:
    if i in l2:
        print(i)
