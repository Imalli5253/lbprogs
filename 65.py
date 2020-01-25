#Program to find element in integer array
def aradd(size,i,arr):
    if  int(i) < size:
        arr.append(input())
        i += 1
        aradd(size,i,arr)

    return arr


size = int(input("Enter array1 size? "))
lst = aradd(size,i=0, arr=[])
print(lst)
ch=input("Enter the lelement to search : ")
if ch in lst:
    print("Element exits")
else:
    print("Element not Found")