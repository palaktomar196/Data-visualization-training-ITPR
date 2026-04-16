def extract_students():
    f1 = open("student.txt", "r")
    f2 = open("newfile.txt", "w")

    for line in f1:
        name, marks, city = line.strip().split(",")
        if int(marks) > 75:
            f2.write(line)

    f1.close()
    f2.close()

    print("Records copied successfully")

extract_students()
