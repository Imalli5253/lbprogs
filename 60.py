#Function for adding array elements
def aradd(arr,i,size):
    if  i < size:
        print("element no :",i)
        arr.append(int(input()))
        i += 1
        aradd(arr,i,size)

    return arr


#Function for deliting duplicate values
def unqn(list1): 
    list_set = set(list1) 
    # convert the set to the list 
    unique_list = (list(list_set))
    print(len(list1)-len(unique_list))


arr = []
i = 0
size = int(input("Enter array size? "))
lst = aradd(arr,i,size)
print(lst)
print("Number of Duplicate values") 
unqn(lst)
