#Function for adding array elements
def aradd(arr,i,size):
    if  i < size:
        arr.append(int(input()))
        i += 1
        aradd(arr,i,size)

    return arr


def scount(list1):
    n_count = 0
    
    for num in list1:
   # checking condition
        if num < 0:
            n_count += 1


    return n_count

arr = []
i = 0
size = int(input("Enter array size? "))
lst = aradd(arr,i,size)
print(lst)
if scount(lst) > 0:
    print("Number of Nagitive elements are",scount(lst))
else:
    print("There is negitive elements in the list")
