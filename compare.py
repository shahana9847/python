list_1=list(map(int,input("enter list1:").split()))
list_2=list(map(int,input("enter list2").split()))
print("same length:",len(list_1)==len(list_2))
print("sum equal:",sum(list_1)==sum(list_2))
common=False
for x in list_1:
    if x in list_2:
        common=True
        break
print("common present:",common)