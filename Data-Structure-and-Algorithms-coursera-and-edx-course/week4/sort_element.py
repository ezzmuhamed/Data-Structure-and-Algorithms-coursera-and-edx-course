
#uses python2

x=input()
number = raw_input()
number = [int(n) for n in number.split()]
number.sort()
for i in range(len(number)):
    print number[i],
