from tkinter import messagebox
import csv

from Student import Student


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
        stud_class = Student()
        filename = stud_class.filename

        display_table.delete(*display_table.get_children())
        with open(filename, "r", encoding="utf-8") as StudData:
            stud_data = csv.DictReader(StudData)

            for stud in stud_data:
                display_table.insert('', 'end', values=(stud['ID Number'], stud['Name'], stud['Course'],
                                                        stud['Year'], stud['Gender']))\
