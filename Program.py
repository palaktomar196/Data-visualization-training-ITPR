def copy_file():
    f1 = open("file1.txt", "r")
    data = f1.read()
    f1.close()

    f2 = open("file2.txt", "w")
    f2.write(data)
    f2.close()

    print("File copied successfully")

copy_file()
