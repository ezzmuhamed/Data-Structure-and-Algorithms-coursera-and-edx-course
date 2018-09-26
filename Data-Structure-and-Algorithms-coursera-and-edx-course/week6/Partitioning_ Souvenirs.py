
#uses python2
def Partitioning(values):
    total = sum(values)
    if len(values) < 3 or total % 3:  # 1
        return 0                      
    third = total // 3
    #print third
    table = [[0] * (len(values) + 1) for z in range(third + 1)]  # 2
    #print table 
    for i in range(1, third + 1):
        for j in range(1, len(values) + 1):  # 3
            ii = i - values[j - 1]  # 4
            if values[j - 1] == i or (ii > 0 and table[ii][j - 1]):  # 5
                table[i][j] = 1 if table[i][j - 1] == 0 else 2
            else:
                table[i][j] = table[i][j - 1]  # 6
 
    return 1 if table[-1][-1] == 2 else 0

n = int(input())
values = raw_input()
values = [int (x) for x in values.split()]
print (Partitioning(values))
