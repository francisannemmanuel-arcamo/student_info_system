from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
import os

from AddStudent import AddStudentFrame
from SearchStudent import SearchStudentFrame


class Student:
    def __init__(self, frame):
        self.frame = frame
        self.frame.title("Student Information System")
        self.frame.geometry("1155x650+95+25")
        self.frame.resizable(False, False)
        self.data = dict()
        self.temp = dict()
        self.filename = 'studentlist.csv'

        # variables for student data
        self.id_no = StringVar()
        self.name = StringVar()
        self.course = StringVar()
        self.year = StringVar()
        self.gender = StringVar()
        self.rows = []

        with open(self.filename, 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows([["ID Number", "Name", "Course", "Year Level", "Gender"]])

        # background frames
        bg_frame = Frame(self.frame, bg="#A51d23")
        bg1_frame = Frame(self.frame, bg="#FA9412")
        bg_frame.place(x=0, y=0, width=1155, height=650)
        bg1_frame.place(x=7.5, y=7.5, width=1140, height=635)

        #  Layout for left frame
        self.left_frame = Frame(bg1_frame, bd=2, bg="#FA9412")
        self.left_frame.place(x=15, y=80, width=450, height=550)
        self.sis_label = Label(bg1_frame, text="STUDENT INFORMATION SYSTEM", bg="white", fg="#A51d23")
        self.home_img = PhotoImage(file=r"home_button_img.png")
        self.home_button = Button(bg1_frame, command=self.homepage, image=self.home_img, bg="#A51d23")

        self.bg_box = Label(self.left_frame, bg="#A51d23", highlightbackground="#A51d23", highlightthickness=2)
        self.bg_box.place(x=25, y=145, width=400, height=390)
        self.fg_box = Frame(self.left_frame, bg="white", highlightbackground="#A51d23", highlightthickness=2)

        self.add_frame = Frame(self.left_frame, bg="white", highlightbackground="#A51d23", highlightthickness=2)
        self.edit_frame = Frame(self.left_frame, bg="white", highlightbackground="#A51d23", highlightthickness=2)
        self.delete_frame = Frame(self.left_frame, bg="white", highlightbackground="#A51d23", highlightthickness=2)
        self.search_frame = Frame(self.left_frame, bg="white", highlightbackground="#A51d23", highlightthickness=2)

        self.head_bldsgn_img = PhotoImage(file=r"label_design.png")
        self.heading_label = Label(self.left_frame, bg="#A51d23", fg="white", anchor='sw', font=("Bebas Neue", 24))
        self.heading_lbldsgn = Label(self.left_frame, image=self.head_bldsgn_img, bg="#A51d23",
                                     fg="white", anchor='sw', font=("Bebas Neue", 24))

        # Navigation buttons
        self.add_button_img = PhotoImage(file=r"addstudent.png").subsample(4, 4)
        self.edit_button_img = PhotoImage(file=r"editstudent.png").subsample(4, 4)
        self.delete_button_img = PhotoImage(file=r"deletestudent.png").subsample(4, 4)
        self.search_button_img = PhotoImage(file=r"searchstudent.png").subsample(4, 4)
        self.add_stud_button = Button(self.left_frame, image=self.add_button_img, bg="white",
                                      command=self.add_student_gui)
        self.edit_stud_button = Button(self.left_frame, image=self.edit_button_img, bg="white",
                                       command=lambda: [self.edit_student_gui(), self.clear_data()])
        self.delete_stud_button = Button(self.left_frame, image=self.delete_button_img, bg="white",
                                         command=lambda: [self.delete_student_gui(), self.clear_data()])
        self.search_stud_button = Button(self.left_frame, image=self.search_button_img, bg="white",
                                         command=lambda: [self.search_student_gui(), self.clear_data()])

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

        # Delete Frame
        self.del_stud_name = Label(self.delete_frame, fg="black", bg="white", font=("Bebas Neue", 16), anchor='w')
        self.del_stud_id = Label(self.delete_frame, fg="black", bg="white", font=("Bebas Neue", 16), anchor='w')
        self.del_stud_year = Label(self.delete_frame, fg="black", bg="white", font=("Bebas Neue", 16), anchor='w')
        self.del_stud_course = Label(self.delete_frame, fg="black", bg="white", font=("Bebas Neue", 16),
                                     anchor='w')
        self.del_stud_gender = Label(self.delete_frame, fg="black", bg="white", font=("Bebas Neue", 16),
                                     anchor='w')

        # right_frame
        self.right_frame = Frame(bg1_frame, bg="#FA9412")
        self.right_frame.place(x=465, y=100, width=675, height=550)
        self.display_label = Label(self.right_frame, bg="#A51d23", fg="white", anchor='w', font=("Bebas Neue", 24),)
        self.display_lbldsgn = Label(self.right_frame, image=self.head_bldsgn_img, bg="#A51d23", fg="white",
                                     anchor='sw')
        self.display_table_frame = Frame(self.right_frame, bg="white", highlightbackground="#A51d23",
                                         highlightthickness=2)
        self.about_bg = Label(self.display_table_frame, bg="#A51d23")
        about = "this project is a simple student information system \nthat lets the user \n\n\u2713 add new students" \
                "\n\u2713 edit a student, \n\u2713 delete a student, and \n\u2713 search a student by id number. \n\n" \
                "it also displays the list of students using a \ntreeview. please download 'Oswald' and " \
                "'Bebas Neue' \nfirst for an amazing layout experience."
        self.about = Text(self.display_table_frame, bg="white", fg="#A51d23", highlightcolor="black",
                          highlightthickness=0, font=("Courier New", 13), relief=FLAT)
        self.about.insert(INSERT, about)
        self.about.config(state=DISABLED)
        self.author = Label(self.display_table_frame, fg="#A51d23", bg="white", font=("Oswald", 12),
                            text="\u00A9 Francis Ann Emmanuel Arcamo", anchor='w')

        # Display data frame
        scroll_x = Scrollbar(self.display_table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.display_table_frame, orient=VERTICAL)
        self.display_table = ttk.Treeview(self.display_table_frame, xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set,  columns=("id_no", "name", "course", "year",
                                                                                 "gender"))
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.display_table.xview)
        scroll_y.config(command=self.display_table.yview)
        self.display_table.heading("id_no", text="ID Number")
        self.display_table.heading("name", text="Name")
        self.display_table.heading("course", text="Course")
        self.display_table.heading("year", text="Year")
        self.display_table.heading("gender", text="Gender")
        self.display_table['show'] = 'headings'
        self.display_table.column("id_no", width=120)
        self.display_table.column("name", width=210)
        self.display_table.column("course", width=120)
        self.display_table.column("year", width=80)
        self.display_table.column("gender", width=95)

        self.homepage()

    # Code for homepage
    def homepage(self):
        self.home_button.place_forget()
        self.hide_widgets()
        self.sis_label.config(font=("Bebas Neue", 50), fg="#FA9412", borderwidth=2, highlightcolor="Red")
        self.sis_label.pack(anchor=CENTER, pady=20)
        self.heading_label.config(text="   Features")
        self.fg_box.place(x=20, y=120, width=400, height=410)
        self.heading_label.place(x=20, y=100, width=400)
        self.heading_lbldsgn.place(x=310, y=100, width=100, height=40)
        self.add_stud_button.place(x=60, y=180, width=125, height=125)
        self.edit_stud_button.place(x=250, y=180, width=125, height=125)
        self.delete_stud_button.place(x=60, y=350, width=125, height=125)
        self.search_stud_button.place(x=250, y=350, width=125, height=125)
        self.display_table_frame.place(x=10, y=121, width=650, height=390)
        self.display_label.place(x=10, y=81, width=650, height=40)
        self.display_label.config(text="    About this Project", font=("Bebas Neue", 20))
        self.display_lbldsgn.place(x=550, y=81, width=100, height=40)
        self.about.place(x=40, y=25, width=550, height=280)
        self.author.place(x=30, y=320, width=250, height=40)
        self.display_table.pack_forget()

    # Display attributes common to different frames
    def display_attributes(self):
        self.sis_label.config(font=("Bebas Neue", 30), fg="#A51d23")
        self.sis_label.place(x=80, y=10, height=50)
        self.home_button.place(x=30, y=10, width=50, height=50)
        self.display_table_frame.place(x=10, y=55, width=650, height=455)
        self.display_label.config(text="  List of Students")
        self.display_lbldsgn.place(x=550, y=15, width=100, height=40)
        self.display_label.place(x=10, y=15, width=650, height=40)
        self.display_table.pack(fill=BOTH, expand=1)

    # buttons
        self.add_stud_button.place(x=30, y=10, width=75, height=75)
        self.edit_stud_button.place(x=130, y=10, width=75, height=75)
        self.delete_stud_button.place(x=230, y=10, width=75, height=75)
        self.search_stud_button.place(x=330, y=10, width=75, height=75)

    # Hide frames whenever using another
    def hide_widgets(self):
        self.add_frame.place_forget()
        self.edit_frame.place_forget()
        self.delete_frame.place_forget()
        self.search_frame.place_forget()

    def add_student_gui(self):
        self.heading_label.config(text="   ADD STUDENT")
        self.hide_widgets()
        self.display_attributes()
        AddStudentFrame(self.add_frame)

    def edit_student_gui(self):
        # edit_student_interface
        self.heading_label.config(text="   EDIT STUDENT")
        self.hide_widgets()
        self.display_attributes()
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

    def search_student_gui(self):
        self.heading_label.config(text="   SEARCH STUDENT")
        self.display_attributes()
        self.hide_widgets()
        SearchStudentFrame(self.search_frame)

    def delete_student_gui(self):
        self.clear_data()
        self.heading_label.config(text="    DELETE STUDENT")
        self.display_attributes()
        self.hide_widgets()
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

    def display_student_table(self):
        self.display_table.delete(*self.display_table.get_children())
        with open('studentlist.csv', "r", encoding="utf-8") as StudData:
            stud_data = csv.reader(StudData, delimiter=",")
            next(stud_data)
            for stud in stud_data:
                data = []
                if len(stud) > 1:
                    for i in stud:
                        data.append(i)
                    self.display_table.insert('', 'end', values=data)

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
            self.display_student_table()
            return
        else:
            return

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
            self.display_student_table()
            return
        else:
            return

    def clear_data(self):
        self.edit_id_entry.delete(0, END)
        self.edit_name_entry.delete(0, END)
        self.edit_year_combo.delete(0, END)
        self.edit_course_entry.delete(0, END)
        self.edit_gender_combo.delete(0, END)
        self.del_stud_name.config(text="")
        self.del_stud_id.config(text="")
        self.del_stud_course.config(text="")
        self.del_stud_year.config(text="")
        self.del_stud_gender.config(text="")

    def select_stud(self):
        cursor_row = self.display_table.focus()
        contents = self.display_table.item(cursor_row)
        rows = contents['values']
        self.clear_data()
        try:
            self.edit_name_entry.insert(0, rows[1])
            self.edit_id_entry.insert(0, rows[0])
            self.edit_year_combo.insert(0, rows[3])
            self.edit_course_entry.insert(0, rows[2])
            self.edit_gender_combo.insert(0, rows[4])
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


root = Tk()
ob = Student(root)
root.mainloop()
