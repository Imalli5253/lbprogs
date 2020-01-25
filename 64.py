#Program to reverse array
def aradd(size,i,arr):
    if  int(i) < size:
        arr.append(int(input()))
        i += 1
        aradd(size,i,arr)

    return arr

def revlist(list1):
    list1.reverse()
    return list1



#arr = []
#i = 0
size = int(input("Enter array1 size? "))
list1=aradd(size,i=0, arr=[])
print("Array before reverse",list1)
print("Array after reverse",revlist(list1))