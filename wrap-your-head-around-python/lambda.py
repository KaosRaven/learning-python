def calculateFee(miles):
    result = miles * .5 + 2.50
    return result

print(calculateFee(10))

add = lambda n1, n2: n1+n2
print(add(1,3))

calculateFee2 = lambda miles: miles * .5 + 2.50
print(calculateFee2(10))

def calculateFee3(miles):
    resultTemplate = lambda miles: miles * .5 + 2.50
    return resultTemplate(miles)

print(calculateFee3(10))