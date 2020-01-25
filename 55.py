def aradd(arr,i,size):
    if  i < size:
        arr.append(int(input()))
        i += 1
        aradd(arr,i,size)

    return arr


arr = []
i = 0
size = int(input("Enter array size? "))
lst = aradd(arr,i,size)
index = int(input("Please enter the elements index to delete "))
if index < len(lst):
    print("Array Before Deletion",lst)
    lst.remove(lst[index])
    print(lst)
else:
    print("Index out of range")

