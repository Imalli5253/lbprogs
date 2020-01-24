#Function for adding array elements
def aradd(arr,i,size):
    if  i < size:
        print("element no :",i)
        arr.append(int(input()))
        i += 1
        aradd(arr,i,size)

    return arr


#Function for deliting duplicate values
def unique(list1): 
    unique_list = [] 
      
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
    
    return unique_list  
    

arr = []
i = 0
size = int(input("Enter array size? "))
lst = aradd(arr,i,size)
print(lst)
print("Array after deletion of duplicate values") 
print(unique(lst))
