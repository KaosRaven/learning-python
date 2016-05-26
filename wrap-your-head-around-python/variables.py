customer = "John Doe"
pickupLocation = "350 5th Ave"
package = customer + pickupLocation
print(package)

package = customer + " @ " + pickupLocation
print(package)

fare = 15
tip = 2
totalFare = fare + tip
print(totalFare)

print(package + " with total of " + str(totalFare))

newfare = fare + int("2")
print(newfare)