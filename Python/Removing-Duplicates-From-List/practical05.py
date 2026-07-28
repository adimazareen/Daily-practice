 #initialising the list
list_valuel =[12,15, 11,12,8, 15,3,3]
print("The initialized list is: ", list_valuel)
res_list=[]
for i in list_valuel:
    if i not in res_list:
        res_list.append(i)
#printing the list after removing the duplicate elements
print("The resultant list after removing the duplicates is ",res_list)
