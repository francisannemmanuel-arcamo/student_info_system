from tkinter import *
from tkinter import ttk
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