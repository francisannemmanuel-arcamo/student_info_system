from tkinter import *
from tkinter import messagebox
import csv
from misc import SISMisc


class DeleteStudentFrame:
    def __init__(self, frame, table):
        self.delete_frame = frame
        self.display_table = table

        self.id_no = StringVar()
        self.name = StringVar()
        self.course = StringVar()
        self.year = StringVar()
        self.gender = StringVar()
        self.rows = []

        # Delete Frame
        self.del_stud_name = Label(self.delete_frame, fg="black", bg="white", font=("Bebas Neue", 16), anchor='w')
        self.del_stud_id = Label(self.delete_frame, fg="black", bg="white", font=("Bebas Neue", 16), anchor='w')
        self.del_stud_year = Label(self.delete_frame, fg="black", bg="white", font=("Bebas Neue", 16), anchor='w')
        self.del_stud_course = Label(self.delete_frame, fg="black", bg="white", font=("Bebas Neue", 16),
                                     anchor='w')
        self.del_stud_gender = Label(self.delete_frame, fg="black", bg="white", font=("Bebas Neue", 16),
                                     anchor='w')

        self.delete_frame.place(x=20, y=120, width=400, height=410)
        choose_lbl = Label(self.delete_frame, text="Select Student to Delete", anchor='w', fg="#A51d23", bg="white",
                           font=("Oswald", 14))
        choose_lbl.place(x=20, y=30, width=220, height=30)
        choose_stud_btn = Button(self.delete_frame, command=self.select_stud,
                                 text="Select", bg="#A51d23", fg="white", font=("Bebas Neue", 20))
        choose_stud_btn.place(x=280, y=30, width=90, height=30)

        name_label = Label(self.delete_frame, text="Name:", font=("Bebas Neue", 20), bg="#A51d23", fg="white")
        name_label.place(x=20, y=80, width=90, height=40)
        id_no_label = Label(self.delete_frame, text="ID No.:", font=("Bebas Neue", 20), bg="#A51d23", fg="white")
        id_no_label.place(x=20, y=130, width=90, height=40)
        year_label = Label(self.delete_frame, text="Year:", font=("Bebas Neue", 20), bg="#A51d23", fg="white")
        year_label.place(x=20, y=180, width=90, height=40)
        course_label = Label(self.delete_frame, text="Course:", font=("Bebas Neue", 20), bg="#A51d23", fg="white")
        course_label.place(x=20, y=230, width=90, height=40)
        gender_label = Label(self.delete_frame, text="Gender:", font=("Bebas Neue", 20), bg="#A51d23", fg="white")
        gender_label.place(x=20, y=280, width=90, height=40)

        delete_button = Button(self.delete_frame, command=self.delete_student, text="Delete", bg="#A51d23", fg="white",
                               font=("Bebas Neue", 20))
        delete_button.place(x=280, y=350, width=90, height=30)

        self.del_stud_name.place(x=115, y=80, width=90, height=40)
        self.del_stud_id.place(x=115, y=130, width=90, height=40)
        self.del_stud_year.place(x=115, y=180, width=90, height=40)
        self.del_stud_course.place(x=115, y=230, width=90, height=40)
        self.del_stud_gender.place(x=115, y=280, width=90, height=40)

    def clear_data(self):
        self.del_stud_name.config(text="")
        self.del_stud_id.config(text="")
        self.del_stud_course.config(text="")
        self.del_stud_year.config(text="")
        self.del_stud_gender.config(text="")

    def delete_student(self):
        msg = messagebox.askquestion('Delete Student', 'Are you sure you want to delete the student')
        if msg == "yes":
            list = []
            with open('studentlist.csv', "r", encoding="utf-8") as StudData:
                data = csv.reader(StudData, delimiter=",")
                for stud in data:
                    if stud != self.rows:
                        list.append(stud)
                with open('studentlist.csv', 'w+', newline='') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerows(list)
                    self.clear_data()
                    messagebox.showinfo("Success!", "Student has been deleted!")
                    SISMisc.display_student_table(self.display_table)
            return
        else:
            return

    def select_stud(self):
        cursor_row = self.display_table.focus()
        contents = self.display_table.item(cursor_row)
        rows = contents['values']
        self.clear_data()
        try:
            self.del_stud_name.config(text=rows[1])
            self.del_stud_id.config(text=rows[0])
            self.del_stud_year.config(text=rows[3])
            self.del_stud_course.config(text=rows[2])
            self.del_stud_gender.config(text=rows[4])
            self.rows = rows
            return
        except IndexError:
            messagebox.showerror("Error", "Select a student first")
            return
