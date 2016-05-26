customer1 = "John Doe"
pickupLocation1 = "350 5th Ave"
package1 = customer1 + pickupLocation1

customer2 = "Jane Doe"
pickupLocation2 = "100 7th Ave"
package2 = customer2 + pickupLocation2

customer3 = "Joe Daniels"
pickupLocation3 = "11 1st Ave"
package3 = customer3 + pickupLocation3

customerList = [customer1, customer2, customer3]

chargePerMile = .5      # global variable

def calculateFee(miles):
    result = miles * chargePerMile + 2.50  # result is a local variable
    return result

myresult = calculateFee(10)     # global variable
print(myresult)
print(chargePerMile)

add = lambda n1, n2: n1+n2    # n1 and n2 are local to the lambda function
print(add(1,3))

calculateFee2 = lambda miles: miles * chargePerMile + 2.50
print(calculateFee2(10))

def calculateFee3(miles):
    resultTemplate = lambda miles: miles * chargePerMile + 2.50
    return resultTemplate(miles)

print(calculateFee3(10))

myint = 10
myint2 = 9
print('myint %d' % (myint))
print('myint2 %d' % (myint2))

def changeGlobal():
    myint = 20      # not the same variable as outside the function
    global myint2   # force global use even tho inside a function
    myint2 = 15
    print('in changeGlobal(), myint %d' % (myint))
    return

changeGlobal()
print('after changeGlobal(), myint %d' % (myint))
print('after changeGlobal(), myint2 %d' % (myint2))