# Program to check whether the given number is Perfect or not
def perfect(num):
    sum = 0
    for i in range(1,num):
        if (num % i) == 0:
            sum +=i
        
    if sum == num:
        print(" Given number is Perfect number")
    else:
        print(" Given number is not a Perfect number")


num=int(input("Enter any positive integer number : "))
perfect(num)