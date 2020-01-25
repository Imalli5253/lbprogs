def arm(num,res):
    while num > 0:
        i = num % 10
        res = res + (i ** 3)
        num = num // 10
    
    return res


num=int(input("Enter any positive integer number : "))
res=0
if num == arm(num,res):
    print(num," is an amstrong number")
else:
    print(num," is not an amstrong number")