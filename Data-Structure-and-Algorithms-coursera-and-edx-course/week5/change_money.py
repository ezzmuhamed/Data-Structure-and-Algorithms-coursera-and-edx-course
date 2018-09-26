#uses python2

# USD - $1, $3, $4
currency = [1,3,4]

# the amount to change - $120
amount = int(input())

# initialize arrays for $0
minimum_number_of_currency = [0]
#currency_composition = [[]]

for i in xrange(1, amount + 1):
    best = 10000
    #best_currency_composition = None

    for j in currency:
        if i - j > -1 and minimum_number_of_currency[i - j] + 1 < best:
            best = minimum_number_of_currency[i - j] + 1
            #best_currency_composition = currency_composition[i - j] + [j]

    minimum_number_of_currency.append(best)
    #currency_composition.append(best_currency_composition)

    #print '{0:3} {1} {2}'.format(i, best, best_currency_composition)
print best 
