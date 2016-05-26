fileContent = 'John Doe;\n350 5th Ave\n|\nJane Doe;\n100 7th Ave\n|\nJoe Daniels;\n11 1st Ave\n'

# create an empty dictionary
packages = {}
# split the existing string by a separator and then limit the no. of splits
newStr = fileContent.split('|',3)
print(newStr)

# use a loop to go through the string, replace new lines and split into 2 variables by the ;
for s in newStr:
    (a,b) = s.replace('\n','').split(';',1)     # split the string
    print(a + '==' + b)
    packages[a] = b     # populate the dictionary

print(packages)
# show the dictionary keys and values separately
print(packages.keys())
print(packages.values())