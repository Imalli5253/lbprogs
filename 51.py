def aradd(arr,i,size):
    if  i < size:
        print("element no :",i)
        arr.append(int(input()))
        i += 1
        aradd(arr,i,size)
    
    return arr, max(arr)


arr = []
i = 0
size = int(input("Enter array size? "))
lst, sm = aradd(arr,i,size)
print(lst)

print("Max of array ",lst," is ",  sm)
print("Min of array",lst," is ",  min(arr))
