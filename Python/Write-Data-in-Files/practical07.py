file1 = open("myfile.txt", "w")
list = ["This is Delhi\n", "This is Mumbai\n", "This is Chennai\n"]
file1.write("Hello\n")
file1.writelines(list)
file1.close()
# to change file access mode
file1 = open("myfile.txt", "rt")
print(file1.read())
file1.close()
