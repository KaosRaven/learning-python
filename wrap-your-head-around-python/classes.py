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

# create a customer class
class Customer:
    name = ''
    pickupLocation = ''

    def getPackage(self):
        return self.name + ', ' + self.pickupLocation

# create an instance of the class
cust1 = Customer()
cust1.name = 'Joe Blow'
cust1.pickupLocation = '1st Ave'
# show contents of the instance we just populated
print(cust1.name)
print(cust1.getPackage())

class Person:
    firstName = ''
    lastName = ''
    streetAddress = ''
    city = ''
    state = ''
    zipcode = ''

    # initialise class calling self from within
    def __init__(self, fname, lname, streetAddress, city, state, zipcode):
        self.firstName = fname
        self.lastName = lname
        self.streetAddress = streetAddress
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def printName(self):
        print('First name is %s' % (self.firstName))
        # indexer is %s in this case, as we are dealing with strings, not integers, this time

p1 = Person('Jim', 'Jones', '100 1st Street', 'Newport Beach', 'CA', '92661')
p1.printName()

class Customer2(Person):
    name = ''
    pickupLocation = ''

    def __init__(self, name, pickupLocation, custId):
        self.name = name
        self.pickupLocation = pickupLocation
        self.__customerId = custId
        return

    def getPackage(self):
        return self.name + ', ' + self.pickupLocation

    def getPackage2(self, delimiter):
        return '%s %s %s. Customer ID = %d' % (self.name, delimiter, self.pickupLocation, self.__customerId)

  #  def printName(self):
  #      print('Name is %s' % (self.name))

    __customerId = 0    # scoped at class level, but not outside. Private variable

cus1 = Customer2('Joe Blow', '350 5th Ave', 20)
cus1.firstName = 'Jim'
cus1.city = 'Newport Beach'     # Person attributes also available here cos called when we defined the Customer2 class
cus1.state = 'CA'
print('From Customer2() class: ' + cus1.name)
print(cus1.getPackage())
print(cus1.getPackage2(':'))

cus1.printName()
print(cus1.city)
print(cus1.state)