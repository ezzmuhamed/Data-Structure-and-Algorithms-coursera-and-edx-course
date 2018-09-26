
#uses python2

def largest_number(a):
    
    nums = map(str, a)
    lst = []
    
     
    
    for i in range (len(a)):
        if a[i]>10:
            lst.append(a[i] / 10)
            lst.append(a[i]%10)
        elif a[i] == 10:
            lst.append(a[i] / 10)
            lst.append(0)
        else:
            lst.append(a[i])
            
    if (len(lst)) == (len(a)*2):
        a.sort(reverse=True)
        return a
    else:
        lst.sort(reverse=True)
        
        return lst
    
    
        

   


a = int(input())
data = raw_input()
data =[int (x) for x in data.split()]
a = data[0:]
largest = largest_number(a)
txt = ''
for x in largest:
    txt += str(x)
print txt    
