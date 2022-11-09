###############################################
## Employee CREATE, READ, UPDATE, DELETE App ##
###############################################
import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


def dbc():
    with mysql.connector.connect(host="127.0.0.1", user="root", passwd=database_password, database='ECRUD_1') as mydb:
        print(mydb)
        myC = mydb.cursor()


def gui():
    a_window = Tk()
    a_window.geometry("600x270")
    a_window.title("Employee CRUD App")

    l_empId = Label(a_window, text="Employee ID", font=("Serif", 12))
    l_empId.place(x=20, y=30)

    l_empName = Label(a_window, text="Employee Name", font=("Serif", 12))
    l_empName.place(x=20, y=60)

    l_empDept = Label(a_window, text="Employee Dept", font=("Serif", 12))
    l_empDept.place(x=20, y=90)

    enterId = Entry(a_window)
    enterId.place(x=170, y=30)

    enterName = Entry(a_window)
    enterName.place(x=170, y=60)

    enterDept = Entry(a_window)
    enterDept.place(x=170, y=90)
    database_password = input("Please, enter database password:")

    def clearFields():
        enterId.delete(0, "end")
        enterName.delete(0, "end")
        enterDept.delete(0, "end")

    def insertData():
        id = enterId.get()
        name = enterName.get()
        dept = enterDept.get()
        if not all([id, name, dept]):
            messagebox.showwarning(
                "Cannot insert", "All of the fields must be filled!")
        else:
            with mysql.connector.connect(host="127.0.0.1", user="root", passwd=database_password, database='ECRUD_1') as mydb:
                myC = mydb.cursor()
                myC.execute(
                    f"insert into empDetails values('{id}', '{name}', '{dept}')")
                mydb.commit()

                clearFields()
                messagebox.showinfo(
                    "Insert Status", "Data Inserted Successfully")
                show()

    def updateData():
        id = enterId.get()
        name = enterName.get()
        dept = enterDept.get()
        if not all([id, name, dept]):
            messagebox.showwarning(
                "Cannot Update", "All of the fields must be filled!")
        else:
            with mysql.connector.connect(host="127.0.0.1", user="root", passwd=database_password, database='ECRUD_1') as mydb:
                myC = mydb.cursor()
                myC.execute(
                    f"update empDetails set empName='{name}', empDept='{dept}' where empId='{id}'")
                mydb.commit()

                clearFields()
                messagebox.showinfo(
                    "Update Status", "Data Updated Successfully")
                show()

    def getData():
        id = enterId.get()
        if not id:
            messagebox.showwarning(
                "Fetch Status", "Please provide Employee ID to fetch the data")
        else:
            with mysql.connector.connect(host="127.0.0.1", user="root", passwd=database_password, database='ECRUD_1') as mydb:
                myC = mydb.cursor()
                myC.execute(f"select * from empDetails where empId='{id}'")
                rows = myC.fetchall()

                for row in rows:
                    enterName.insert(0, row[1])
                    enterDept.insert(0, row[2])

    def deleteData():
        id = enterId.get()
        if not id:
            messagebox.showwarning(
                "Delete Status", "Please provide Employee ID to delete the data")
        else:
            with mysql.connector.connect(host="127.0.0.1", user="root", passwd=database_password, database='ECRUD_1') as mydb:
                myC = mydb.cursor()
                myC.execute(f"delete from empDetails where empId='{id}'")
                mydb.commit()

                clearFields()
                messagebox.showinfo(
                    "Delete Status", "Data Deleted Successfully")
                show()

    def show():
        with mysql.connector.connect(host="127.0.0.1", user="root", passwd=database_password, database='ECRUD_1') as mydb:
            myC = mydb.cursor()
            myC.execute(f"select * from empDetails")
            rows = myC.fetchall()
            showData.delete(0, showData.size())

            for row in rows:
                addData = f"{row[0]} {row[1]} {row[2]}"
                showData.insert(showData.size() + 1, addData)

    insertBtn = Button(a_window, text="Insert", font=(
        "Sans", 12), bg="white", command=insertData)
    insertBtn.place(x=20, y=160)

    updateBtn = Button(a_window, text="Update", font=(
        "Sans", 12), bg="white", command=updateData)
    updateBtn.place(x=80, y=160)

    getBtn = Button(a_window, text="Fetch", font=(
        "Sans", 12), bg="white", command=getData)
    getBtn.place(x=150, y=160)

    deleteBtn = Button(a_window, text="Delete", font=(
        "Sans", 12), bg="white", command=deleteData)
    deleteBtn.place(x=210, y=160)

    resetBtn = Button(a_window, text="Reset", font=(
        "Sans", 12), bg="white", command=clearFields)
    resetBtn.place(x=20, y=210)

    showData = Listbox(a_window)
    showData.place(x=330, y=30)
    show()

    a_window.mainloop()


if __name__ == '__main__':
    gui()
