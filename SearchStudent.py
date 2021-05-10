from tkinter import *
from tkinter import ttk
import csv

from misc import SISMisc


class SearchStudentFrame:
    def __init__(self, frame):
        self.search_frame = frame

        # Search Frame
        self.search_bar_entry = Entry(self.search_frame, highlightthickness=2, highlightbackground="#A51d23",
                                      font=("Bebas Neue", 18))

        self.srch_btn_img = PhotoImage(file=r"search_button_img.png")
        self.srch_result_msg = Label(self.search_frame, text="", bg="white", fg="#A51d23", font=("Oswald", 12))
        self.search_result_frame = Frame(self.search_frame, bg="white", highlightthickness=2,
                                         highlightbackground="black")

        self.search_bar_entry.delete(0, END)

        # search results table for
        scrll_x = Scrollbar(self.search_result_frame, orient=HORIZONTAL)
        self.results_table = ttk.Treeview(self.search_result_frame, xscrollcommand=scrll_x.set,
                                          columns=("name", "course", "year", "gender"))
        scrll_x.pack(side=BOTTOM, fill=X)
        scrll_x.config(command=self.results_table.xview)
        self.results_table.heading("name", text="Name")
        self.results_table.heading("course", text="Course")
        self.results_table.heading("year", text="Year")
        self.results_table.heading("gender", text="Gender")
        self.results_table['show'] = 'headings'
        self.results_table.column("name", width=140)
        self.results_table.column("course", width=60)
        self.results_table.column("year", width=60)
        self.results_table.column("gender", width=50)
        self.srchrslts_label = Label(self.search_frame, text="  Search Result", anchor='w', bg="#A51d23", fg="white",
                                     font=("Bebas Neue", 18))

        self.search_frame.place(x=20, y=120, width=400, height=410)
        id_no_label = Label(self.search_frame, text="ID #", bg="#A51d23", fg="white", font=("Bebas Neue", 20))
        id_no_label.place(x=30, y=45, width=50, height=40)
        self.search_bar_entry.place(x=80, y=45, width=250, height=40)
        search_button = Button(self.search_frame, command=self.search_student,
                               image=self.srch_btn_img, bg="#A51d23", fg="white", font=("Bebas Neue", 20))
        search_button.place(x=330, y=45, width=40, height=40)
        self.srchrslts_label.place_forget()
        self.search_result_frame.place_forget()
        self.srch_result_msg.place_forget()

    def search_student(self):
        if SISMisc.id_checker(self.search_bar_entry.get()):
            self.srchrslts_label.place_forget()
            self.search_result_frame.place_forget()
            self.srch_result_msg.place(x=30, y=100, height=20, width=100)

            with open('studentlist.csv', "r", encoding="utf-8") as StudData:
                studinfo = csv.reader(StudData)
                for stud in studinfo:
                    if len(stud) > 0:
                        if stud[0] == self.search_bar_entry.get():
                            self.results_table.delete(*self.results_table.get_children())
                            self.srch_result_msg.config(text="1 record found")
                            self.srchrslts_label.place(x=30, y=130, width=340, height=35)
                            self.search_result_frame.place(x=30, y=160, width=340, height=200)
                            self.results_table.insert('', 'end', values=[stud[1], stud[2], stud[3], stud[4]])
                            self.results_table.pack(fill=BOTH, expand=1)
                            return
                self.srch_result_msg.config(text="No records found")
