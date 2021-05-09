from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# from misc import SISMisc
import csv


class EditStudentFrame:
    def __init__(self, frame):
        self.edit_frame = frame

        self.id_no = StringVar()
        self.name = StringVar()
        self.course = StringVar()
        self.year = StringVar()
        self.gender = StringVar()
        self.rows = []

        # Edit
        self.edit_name_entry = Entry(self.edit_frame, textvariable=self.name, highlightthickness=2,
                                     highlightbackground="#A51d23", font=("Bebas Neue", 20))
        self.edit_id_entry = Entry(self.edit_frame, textvariable=self.id_no, highlightthickness=2,
                                   highlightbackground="#A51d23", font=("Bebas Neue", 20))
        self.edit_year_combo = ttk.Combobox(self.edit_frame, textvariable=self.year, font=("Bebas Neue", 20),
                                            values=[
                                                "First Year",
                                                "Second Year",
                                                "Third Year",
                                                "Fourth Year",
                                                "Fifth Year"])
        self.edit_course_entry = Entry(self.edit_frame, textvariable=self.course, font=("Bebas Neue", 18),
                                       highlightthickness=2, highlightbackground="#A51d23")
        self.edit_gender_combo = ttk.Combobox(self.edit_frame, textvariable=self.gender, font=("Bebas Neue", 20),
                                              values=[
                                                  "Male",
                                                  "Female",
                                                  "Transgender Male",
                                                  "Transgender Female",
                                                  "Non-conforming",
                                                  "Other"])

        self.edit_frame.place(x=20, y=120, width=400, height=410)

        # GUI for selecting student to be updated
        choose_label = Label(self.edit_frame, text="Select Student to Edit", anchor='w', fg="#A51d23", bg="white",
                             font=("Oswald", 14))
        choose_label.place(x=20, y=28, width=220, height=30)
        choose_stud_btn = Button(self.edit_frame, command=self.select_stud,
                                 text="Select", bg="#A51d23", fg="white", font=("Bebas Neue", 20))
        choose_stud_btn.place(x=280, y=28, width=90, height=30)

        # attributes on edit student feature
        name_label = Label(self.edit_frame, text="Name:", font=("Bebas Neue", 20), bg="#A51d23", fg="white")
        name_label.place(x=20, y=80, width=90, height=40)
        self.edit_name_entry.place(x=110, y=80, width=270, height=40)
        id_no_label = Label(self.edit_frame, text="ID No.:", font=("Bebas Neue", 20), bg="#A51d23", fg="white")
        id_no_label.place(x=20, y=130, width=90, height=40)
        self.edit_id_entry.place(x=110, y=130, width=270, height=40)
        year_label = Label(self.edit_frame, text="Year:", font=("Bebas Neue", 20), bg="#A51d23", fg="white")
        year_label.place(x=20, y=180, width=90, height=40)
        self.edit_year_combo.place(x=110, y=180, width=270, height=40)
        course_label = Label(self.edit_frame, text="Course:", font=("Bebas Neue", 20), bg="#A51d23", fg="white")
        course_label.place(x=20, y=230, width=90, height=40)
        self.edit_course_entry.place(x=110, y=230, width=270, height=40)
        gender_label = Label(self.edit_frame, text="Gender:", font=("Bebas Neue", 20), bg="#A51d23", fg="white")
        gender_label.place(x=20, y=280, width=90, height=40)
        self.edit_gender_combo.place(x=110, y=280, width=270, height=40)

        # buttons for add student feature
        update_info_button = Button(self.edit_frame, command=self.update_student, text="Update", bg="#A51d23",
                                    fg="white", font=("Bebas Neue", 20))
        update_info_button.place(x=170, y=350, width=90, height=30)
        clear_info_button = Button(self.edit_frame, command=self.clear_data, text="Clear", bg="#A51d23", fg="white",
                                   font=("Bebas Neue", 20))
        clear_info_button.place(x=280, y=350, width=90, height=30)

    def clear_data(self):
        self.edit_id_entry.delete(0, END)
        self.edit_name_entry.delete(0, END)
        self.edit_year_combo.delete(0, END)
        self.edit_course_entry.delete(0, END)
        self.edit_gender_combo.delete(0, END)

    def update_student(self):
        msg = messagebox.askquestion("Update Student", "Are you sure you want to edit the student's information")
        if msg == "yes":
            list = []
            with open('studentlist.csv', "r", encoding="utf-8") as StudData:
                stud_data = csv.reader(StudData, delimiter=",")
                for stud in stud_data:
                    if stud == self.rows:
                        stud = [self.id_no.get(), self.name.get(), self.course.get(), self.year.get(),
                                self.gender.get()]
                    list.append(stud)
                with open('studentlist.csv', 'w+', newline='') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerows(list)
                    self.clear_data()
                    messagebox.showinfo("Success!", "Student information has been updated!")
            return
        else:
            return

