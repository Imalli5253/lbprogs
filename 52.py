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
lst.sort()
print("Second lagest number of array is ",lst[len(lst)-2])
#rint(large)
#print("Second largest of Array ",lst," is ",max(lst.remove(int(max(lst)))))
