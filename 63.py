#Program to merge the two arrays in new array
def aradd(size,i,arr):
    if  int(i) < size:
        arr.append(int(input()))
        i += 1
        aradd(size,i,arr)

    return arr


#arr = []
#i = 0
size = int(input("Enter array1 size? "))
list1=aradd(size,i=0, arr=[])
size = int(input("Enter array2 size? "))
list2=aradd(size,i=0, arr=[])
print(list1,list2)
#This will only work in python3.6 and above
list3=[*list1, *list2]
print("Array After merging\n",list3)

