# Program for fibonacci_series
def fibi(count): 
    if count < 2:
        return [0,1]
    else:
        fl = fibi(count-1)
        fl.append(fl[len(fl)-1]+fl[len(fl)-2])
        return fl

        

n=int(input("Enter your index : "))
print(fibi(n)) 
