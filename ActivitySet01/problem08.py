 # Files
file_name = input("Enter name of file: ")
if file_name == "t":
    file_exe = open('filetext.txt')
    for lines in file_exe:
        capitalize = lines.upper()
        print(capitalize)
else:
    print("Invalid file name")