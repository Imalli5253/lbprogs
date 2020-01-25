#Program to Count even and Odd numbers in array
def aradd(size,i,arr):
    if  int(i) < size:
        arr.append(int(input()))
        i += 1
        aradd(size,i,arr)

    return arr

def count(list1):
    e_count = 0
    o_count = 0
    print(list1)
    for n in list1:
        if (n % 2) == 0:
            e_count +=1
        else:
            o_count +=1
            
        
    print("Count of even numbers", e_count)
    print("Count of odd numbers", o_count)



size = int(input("Enter array1 size? "))
list1=aradd(size,i=0, arr=[])
count(list1)