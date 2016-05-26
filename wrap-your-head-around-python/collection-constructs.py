customer1 = "John Doe"
pickupLocation1 = "350 5th Ave"
package1 = customer1 + pickupLocation1

customer2 = "Jane Doe"
pickupLocation2 = "100 7th Ave"
package2 = customer2 + pickupLocation2

customer3 = "Joe Daniels"
pickupLocation3 = "11 1st Ave"
package3 = customer3 + pickupLocation3

# create a list of customers
customerList = [customer1, customer2, customer3]
print(customerList[1])

# add new customer and append to list
customer4 = "Jason Bourne"
pickupLocation4 = "333 Lexington Ave"
package4 = customer4 + pickupLocation4

customerList.append(customer4)
print(customerList)

# remove a customer from the list
customerList.remove(customer4)
print(customerList)

# reassign a customer in the list (but not the original variable that was created)
customerList[0] = "John Doe II"
print(customerList[0])
print(customer1)

# create dictionary of addresses
addressList = {customer1:pickupLocation1, customer2:pickupLocation2, customer3:pickupLocation3}
print(len(addressList))
print(len(customerList))
print(addressList[customer2])