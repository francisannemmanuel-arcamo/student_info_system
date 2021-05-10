import os
import csv


class Student:
    def __init__(self):
        self.data = dict()
        self.temp = dict()
        self.filename = 'studentlist.csv'

        if not os.path.exists(self.filename):
            with open(self.filename, mode='w') as csv_file:
                fieldnames = ["ID Number", "Name", "Gender", "Course", "Year Level"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()

        else:
            with open(self.filename, newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    self.data[row["ID Number"]] = {'Name': row["Name"], 'Gender': row["Gender"],
                                                   ' Course': row["Course"], 'Year Level': row["Year Level"]}
            self.temp = self.data.copy()

    def saveData(self):
        datalist = []
        with open(self.filename, "w", newline='') as u:
            fieldnames = ["ID Number", "Name", "Course", "Year", "Gender"]
            writer = csv.DictWriter(u, fieldnames=fieldnames, lineterminator='\n')
            writer.writeheader()
            for id, val in self.data.items():
                temp = {"ID Number": id}
                for key, value in val.items():
                    temp[key] = value
                datalist.append(temp)
            writer.writerows(datalist)