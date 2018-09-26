
#uses python2

def Money_Change_coins(n):
    #i = 0
    count = 0 
    for i in range(n): 
        if(n >= 4):
            n = n - 4
            #i= i + 4
            count = count +1
            continue
        elif (n>=3):
            n = n-3
            #i = i+3
            count = count +1
            continue
        elif (n>=1):
            n = n-1
            #i = i+1
            count = count +1
            continue
        elif (n == 0):
            break

    return count       
    
n = int(input())
print(Money_Change_coins(n))  
