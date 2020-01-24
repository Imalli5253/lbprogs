#Function for adding array elements
def aradd(arr,i,size):
    if  i < size:
        arr.append(int(input()))
        i += 1
        aradd(arr,i,size)

    return arr


#Function for counting occurences
def countX(lst, x): 
    return lst.count(x) 
  

arr = []
i = 0
size = int(input("Enter array size? "))
lst = aradd(arr,i,size)
print(lst)
unique_list = list(set(lst))
#siprint("Array after deletion of duplicate values") 
for x in unique_list:
    print('{} has occurred {} times'.format(x, countX(lst, x)))
