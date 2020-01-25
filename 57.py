#Program to find Negitive elements in Integer array
def aradd(size,i,arr):
    if  int(i) < size:
        arr.append(int(input()))
        i += 1
        aradd(size,i,arr)

    return arr


def nlist(list1):
    print("Negitive elements in an Array")
    for num in list1:
        if num < 0:
            print(num)


size = int(input("Enter array1 size? "))
lst = aradd(size,i=0, arr=[])
#calling negitive values function
nlist(lst)