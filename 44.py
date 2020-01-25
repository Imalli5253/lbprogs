num=int(input("Enter any positive integer number : "))
flag = 0
for x in range(1,num+1):
    if (num % x) == 0:
        flag +=1

print(flag)
if flag == 2:
    print(num," is prime number")
else:
    print(num," is not a prime number")