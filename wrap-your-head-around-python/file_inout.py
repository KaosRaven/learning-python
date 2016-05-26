# create handle to file ... open('pathtofile','operator')
fileOutput = open('file_io.txt','wt')

# create variable for the contents I want to put in the file
fileContent = 'John Doe:\n350 5th Ave\n|\nJane Doe:\n100 7th Ave\n|\nJoe Daniels:\n11 1st Ave\n'

# write the content to the file and then close the file
fileOutput.write(fileContent)
fileOutput.close()

# create a new handle and read back the file content
fileInput = open('file_io.txt','rt')
# workaround for testing here rather than in IDLE - set read contents to a variable and print that to the console
viewit = fileInput.read()
print(viewit)
# close the file as we are now finished with it
fileInput.close()