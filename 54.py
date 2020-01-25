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
ch=input("Please insert new element to this Array")
print(lst)
lst.append(int(ch))
print(lst)




