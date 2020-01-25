# Program for Sorting Integer array in Descending order

def aradd(size,i,arr):
    if  int(i) < size:
        arr.append(int(input()))
        i += 1
        aradd(size,i,arr)

    return arr


size = int(input("Enter array1 size? "))
lst = aradd(size,i=0, arr=[])
print("Array elements ",lst)
lst.sort(reverse=True)
print("Array element in Descending order ",lst)