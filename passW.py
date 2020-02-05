def isDigitPresent(x, d,name): 
    # Breal loop if d is present as digit
    temp = 0
    while (d > 0):
        #print(d)
        r = d % 10
        #print(r)
        if (r == x):
            temp = x
            break
        elif r < x:
            if r > temp:
                temp = r
            else:
                temp = temp
                #return temp
                #print("is",temp)
        elif not(r > x and r < x and r == x):
            temp = temp
        d = d // 10
    #print(temp)
    return temp


def passChar(dic):
    res = ""
    for name, number in dic.items(): 
        #print(len(name),":",number)
        a = isDigitPresent(len(name),number,name)
        #print(a)
        if a != 0:
            res = res + res.join(name[a-1])
        else:
            res = res + res.join('X')

    print(res)

    #print(res)


#main Program
n = int(input("Enter input size : "))
d = {}

for i in range(n):
    keys = input("Enter employee name : ") # here i have taken keys as strings
    values = int(input("Enter employee number : ")) # here i have taken values as integers
    d[keys] = values

passChar(d)
