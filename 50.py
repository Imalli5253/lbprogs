def aradd(arr,i,size):
    if  i < size:
        print("element no :",i)
        arr.append(int(input()))
        i += 1
        aradd(arr,i,size)
    
    return arr, sum(arr)


arr = []
i = 0
size = int(input("Enter array size? "))
lst, sm = aradd(arr,i,size)
print(lst)

print("Sum of array ",lst," is ",  sm)

