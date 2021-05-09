from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from misc import SISMisc
import csv


class AddStudentFrame:
    def __init__(self, frame):
        self.add_frame = frame

        #
        self.id_no = StringVar()
        self.name = StringVar()
        self.course = StringVar()
        self.year = StringVar()
        self.gender = StringVar()

        self.add_name_entry = Entry(self.add_frame, textvariable=self.name, highlightthickness=2,
                                    highlightbackground="#A51d23", font=("Bebas Neue", 20))

        self.add_id_entry = Entry(self.add_frame, textvariable=self.id_no, highlightthickness=2,
                                  highlightbackground="#A51d23", font=("Bebas Neue", 20))
        self.add_year_combo = ttk.Combobox(self.add_frame, textvariable=self.year, font=("Bebas Neue", 20),
                                           values=[
                                               "1st Year",
                                               "2nd Year",
                                               "3rd Year",
                                               "4th Year",
                                               "5th Year"])
        self.add_course_entry = Entry(self.add_frame, textvariable=self.course, highlightthickness=2,
                                      highlightbackground="#A51d23", font=("Bebas Neue", 18))
        self.add_gender_combo = ttk.Combobox(self.add_frame, textvariable=self.gender, font=("Bebas Neue", 20),
                                             values=[
                                                 "Male",
                                                 "Female",
                                                 "Transgender Male",
                                                 "Transgender Female",
                                                 "Non-conforming",
                                                 "Other"])

        # add_student_interface
        self.add_frame.place(x=20, y=120, width=400, height=410)

        # attributes of the add student feature
        name_label = Label(self.add_frame, text="Name:", font=("Bebas Neue", 20), bg="#A51d23", fg="white")
        name_label.place(x=20, y=50, width=90, height=40)
        self.add_name_entry.place(x=110, y=50, width=270, height=40)
        id_no_label = Label(self.add_frame, text="ID No.:", font=("Bebas Neue", 20), bg="#A51d23", fg="white")
        id_no_label.place(x=20, y=100, width=90, height=40)
        self.add_id_entry.place(x=110, y=100, width=270, height=40)
        year_label = Label(self.add_frame, text="Year:", font=("Bebas Neue", 20), bg="#A51d23", fg="white")
        year_label.place(x=20, y=150, width=90, height=40)
        self.add_year_combo.place(x=110, y=150, width=270, height=40)
        course_label = Label(self.add_frame, text="Course:", font=("Bebas Neue", 20), bg="#A51d23", fg="white")
        course_label.place(x=20, y=200, width=90, height=40)
        self.add_course_entry.place(x=110, y=200, width=270, height=40)
        gender_label = Label(self.add_frame, text="Gender:", font=("Bebas Neue", 20), bg="#A51d23", fg="white")
        gender_label.place(x=20, y=250, width=90, height=40)
        self.add_gender_combo.place(x=110, y=250, width=270, height=40)

        # buttons on add student
        add_info_button = Button(self.add_frame, command=self.add_student, text="Add", bg="#A51d23", fg="white",
                                 font=("Bebas Neue", 20))
        add_info_button.place(x=170, y=330, width=90, height=30)
        clear_info_button = Button(self.add_frame, command=self.clear_data, text="Clear", bg="#A51d23", fg="white",
                                   font=("Bebas Neue", 20))
        clear_info_button.place(x=280, y=330, width=90, height=30)

    def clear_data(self):
        self.add_id_entry.delete(0, END)
        self.add_name_entry.delete(0, END)
        self.add_course_entry.delete(0, END)
        self.add_year_combo.delete(0, END)
        self.add_gender_combo.delete(0, END)

    def add_student(self):
        msg = messagebox.askquestion('Add Student', 'Are you sure you want to add the student')
        if msg == "yes":
            if self.name.get() == "" or self.id_no.get() == "" or self.year == "" or self.course.get() == "" \
                    or self.gender.get() == "":
                messagebox.showerror("Error", "Please fill out all fields")
            elif SISMisc.id_checker(self.id_no.get()):
                studdata = [self.id_no.get(), self.name.get(), self.course.get(), self.year.get(), self.gender.get()]
                with open('studentlist.csv', 'a+', newline='') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerows([studdata])
                messagebox.showinfo("Success!", "Student added to database!")
                self.clear_data()
            return
        else:
            return