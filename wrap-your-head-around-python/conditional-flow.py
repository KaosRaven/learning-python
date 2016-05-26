customer = "John Doe"
pickupLocation = "350 5th Ave"
package = customer + pickupLocation

if "350 5th Ave" in package:
   print("customer found")

# what if there are more customers?

customer2 = "Jane Doe"
pickupLocation2 = "100 7th Ave"
package = customer2 + pickupLocation2

customer3 = "Joe Daniels"
pickupLocation3 = "11 1st Ave"
package = customer3 + pickupLocation3

if "350 5th Ave" in package:
    print("customer 1 found")
elif "100 7th Ave" in package:
    print("customer 2 found")
else:
    print("unknown customer found")

# what if we want to find ranges of street numbers on the same street?
# emphasis on ordering for this example. Will start with 100, 200, 300 first.

streetNumber = 689

if streetNumber >= 0 and streetNumber < 200:
    print("Customer found in 0 to 100 block")
elif streetNumber >= 200 and streetNumber < 300:
    print("Customer found in 200 block")
elif streetNumber >= 300 and streetNumber < 400:
    print("Customer found in 300 block")
else:
    print("Customer found in 400 and above block")