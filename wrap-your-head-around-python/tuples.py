customer1 = "John Doe"
pickupLocation1 = "350 5th Ave"
package1 = customer1 + ';' + pickupLocation1

customer2 = "Jane Doe"
pickupLocation2 = "100 7th Ave"
package2 = customer2 + ';' + pickupLocation2

customer3 = "Joe Daniels"
pickupLocation3 = "11 1st Ave"
package3 = customer3 + ';' + pickupLocation3

packages = {customer1:pickupLocation1, customer2:pickupLocation2, customer3:pickupLocation3}

# a tuple allows you to take multiple values and assign them into a single variable set
a,b = package1.split(';',1)
print(a)
print(b)

tuplePackage = package1.split(';',1)
print(tuplePackage[0])

# a dictionary is actually a tuple value pair (key and value)
for k,v in packages.items():
    print(k + ' address= ' + v)

# create a tuple
numbers = (1,)
print(numbers[0])

# create tuple list
streets = ('1st Street','2nd Street','3rd Street','4th Street')
print(streets[1:4])

# this is a tuple, not a list, so values can not be reassigned, only overwritten
test = (1,2,3,4,5)
print(test[1:3])
# test[0] = 22 ... doesn't work with a tuple type variable
test = (22,33,44,55,66) # does work, as whole tuple is being overwritten
print(test[0])