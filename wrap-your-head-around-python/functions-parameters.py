# simple variable by calculation as sample data
result = 1 + 3
print(result)

# define function called add to do the same thing as above
def add(n1,n2):
    result = (n1 + n2)
    return result

# call the function with parameters and print result
print(add(1,3))

# use a lambda to assign a function into a variable which we can then execute - it's kind of an inline function
myfuncresult = lambda n1, n2: n1+n2
print(myfuncresult(1,3))

# a map uses lambda with a list of data to execute the function for each item in the list
myfuncresult2 = map(lambda x:x*2, [1,4,20])
print(list(myfuncresult2))

def calculateFee(miles):
    result = miles * .5 + 2.50
    return result

print(calculateFee(10))

# define the same function, but provide an initial value for the rate, in case one isn't called in the function
def calculateFee(miles, initialRate = 2.50):
    result = miles * .5 + initialRate
    return result

print(calculateFee(10,3))

# define multiple input function
def calculateMultiCustomerRate(*miles):
    rate = []   # create empty list
    for m in miles:     # loop through parameter list
        rate.append(m * 2.50)   # perform operation
    return rate     # return calculated result

# call function and put results into a list
rates = calculateMultiCustomerRate(10,20,30)
# loop list to show all results
i = 1
for r in rates:
    print('customer %d = $%d' % (i,r))  # %d is an indexer
    i = i + 1