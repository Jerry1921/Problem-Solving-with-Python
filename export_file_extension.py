fileName = input("Write the file name : ")

file_extns = fileName.split(".")

print("The extension is " + repr(file_extns[-1]))