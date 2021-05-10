from tkinter import messagebox
import csv

class SISMisc:
    def id_checker(id_num):
        if len(id_num) != 9:
            messagebox.showerror("Error", "Invalid ID Number")
        elif id_num[4] != '-' or not id_num.replace("-", "").isdigit():
            messagebox.showerror("Error", "Invalid ID Number")
        else:
            return True
        return False

    def display_student_table(display_table):
        display_table.delete(*display_table.get_children())
        with open('studentlist.csv', "r", encoding="utf-8") as StudData:
            stud_data = csv.reader(StudData, delimiter=",")
            next(stud_data)
            for stud in stud_data:
                data = []
                if len(stud) > 1:
                    for i in stud:
                        data.append(i)
                    display_table.insert('', 'end', values=data)