students = {}

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    students[roll] = {"Name": name, "Marks": marks}
    print("Student Added Successfully")

def view_student():
    if not students:
        print("No Records Found")
    else:
        for roll, data in students.items():
            print(roll, data)

def update_student():
    roll = input("Enter Roll No to Update: ")
    if roll in students:
        students[roll]["Name"] = input("Enter New Name: ")
        students[roll]["Marks"] = input("Enter New Marks: ")
        print("Student Updated")
    else:
        print("Student Not Found")

def delete_student():
    roll = input("Enter Roll No to Delete: ")
    if roll in students:
        del students[roll]
        print("Student Deleted")
    else:
        print("Student Not Found")

while True:
    print("\n1.Add 2.View 3.Update 4.Delete 5.Exit")
    choice = input("Enter Choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_student()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        break
    else:
        print("Invalid Choice")
