from tkinter import *
from tkinter import ttk
import csv
import os

from AddStudent import AddStudentFrame
from SearchStudent import SearchStudentFrame
from EditStudent import EditStudentFrame
from DeleteStudent import DeleteStudentFrame


class Student:
    def __init__(self, frame):
        self.frame = frame
        self.frame.title("Student Information System")
        self.frame.geometry("1155x650+95+25")
        self.frame.resizable(False, False)
        self.data = dict()
        self.temp = dict()
        self.filename = 'studentlist.csv'

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
                                       command=self.edit_student_gui)
        self.delete_stud_button = Button(self.left_frame, image=self.delete_button_img, bg="white",
                                         command=self.delete_student_gui)
        self.search_stud_button = Button(self.left_frame, image=self.search_button_img, bg="white",
                                         command=self.search_student_gui)

        # right_frame
        self.right_frame = Frame(bg1_frame, bg="#FA9412")
        self.right_frame.place(x=465, y=100, width=675, height=550)
        self.display_label = Label(self.right_frame, bg="#A51d23", fg="white", anchor='w', font=("Bebas Neue", 24),)
        self.display_lbldsgn = Label(self.right_frame, image=self.head_bldsgn_img, bg="#A51d23", fg="white",
                                     anchor='sw')
        self.about_frame = Frame(self.right_frame, bg="white", highlightbackground="#A51d23",
                                 highlightthickness=2)
        self.display_table_frame = Frame(self.right_frame, bg="white", highlightbackground="#A51d23",
                                         highlightthickness=2)

        self.about_bg = Label(self.about_frame, bg="#A51d23")
        about = "this project is a simple student information system \nthat lets the user \n\n\u2713 add new students" \
                "\n\u2713 edit a student, \n\u2713 delete a student, and \n\u2713 search a student by id number. \n\n" \
                "it also displays the list of students using a \ntreeview. please download 'Oswald' and " \
                "'Bebas Neue' \nfirst for an amazing layout experience."
        self.about = Text(self.about_frame, bg="white", fg="#A51d23", highlightcolor="black",
                          highlightthickness=0, font=("Courier New", 13), relief=FLAT)
        self.about.insert(INSERT, about)
        self.about.config(state=DISABLED)
        self.author = Label(self.about_frame, fg="#A51d23", bg="white", font=("Oswald", 12),
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
        self.display_table_frame.place_forget()

        self.hide_frames()

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

        self.about_frame.place(x=10, y=121, width=650, height=390)
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

        self.about_frame.place_forget()

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
    def hide_frames(self):
        self.add_frame.place_forget()
        self.edit_frame.place_forget()
        self.delete_frame.place_forget()
        self.search_frame.place_forget()

    def add_student_gui(self):
        self.heading_label.config(text="   ADD STUDENT")
        self.hide_frames()
        self.display_attributes()
        AddStudentFrame(self.add_frame, self.display_table)

    def edit_student_gui(self):
        # edit_student_interface
        self.heading_label.config(text="   EDIT STUDENT")
        self.hide_frames()
        self.display_attributes()
        EditStudentFrame(self.edit_frame, self.display_table)

    def search_student_gui(self):
        self.heading_label.config(text="   SEARCH STUDENT")
        self.display_attributes()
        self.hide_frames()
        SearchStudentFrame(self.search_frame)

    def delete_student_gui(self):
        self.heading_label.config(text="    DELETE STUDENT")
        self.hide_frames()
        self.display_attributes()
        DeleteStudentFrame(self.delete_frame, self.display_table)


root = Tk()
ob = Student(root)
root.mainloop()
