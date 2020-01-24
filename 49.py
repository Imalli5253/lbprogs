def aradd(arr,i,size):
    if  i < size:
        arr.append(input())
        i += 1
        aradd(arr,i,size)
    
    return arr

arr = []
i = 0
size = int(input("Enter array size? "))
print(aradd(arr,i,size))

