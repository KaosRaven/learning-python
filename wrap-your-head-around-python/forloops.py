customer1 = "John Doe"
pickupLocation1 = "350 5th Ave"
package1 = customer1 + pickupLocation1

customer2 = "Jane Doe"
pickupLocation2 = "100 7th Ave"
package2 = customer2 + pickupLocation2

customer3 = "Joe Daniels"
pickupLocation3 = "11 1st Ave"
package3 = customer3 + pickupLocation3

# create list of packages, and dictionary of customers with locations
packages = [package1, package2, package3]
packages2 = {customer1:pickupLocation1, customer2:pickupLocation2, customer3:pickupLocation3}

# list looping
for p in packages:
    print(p)

# dictionary looping (k is key, v is value)
for k,v in packages2.items():
    print(k + ' address= ' + v)

# dictionary with just key values
print('==================')
for k in packages2.keys():
    print(k)