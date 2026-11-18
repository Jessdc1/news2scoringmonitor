import tkinter as tk
from news2_functions import (
get_risk_rank,
CLINICAL_CONCERN,
Patient,
save_ward,
load_ward
)

DATA_FILE = "ward_data.csv"

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.ward = load_ward(DATA_FILE)
        self.createWidgets()

    def createWidgets(self):
        self.title = tk.Label(self, text="NEWS2 Ward Monitor App")
        self.title.pack(pady=10)
        self.add_btn = tk.Button(self)
        self.add_btn["text"] = "Add patient"
        self.add_btn["command"] = self.add_patient
        self.add_btn.pack(pady=10)
        self.record_obs_btn = tk.Button(self)
        self.record_obs_btn["text"] = "Record Observations"
        self.record_obs_btn["command"] = self.add_observations
        self.record_obs_btn.pack(pady=10)
        self.ward_btn = tk.Button(self)
        self.ward_btn["text"] = "View Ward"
        self.ward_btn["command"] = self.view_ward
        self.ward_btn.pack(pady=10)
        self.history_btn = tk.Button(self)
        self.history_btn["text"] = "View Patient History"
        self.history_btn["command"] = self.view_history
        self.history_btn.pack(pady=10)
        self.QUIT = tk.Button(self, text="QUIT", fg="blue", command=self.master.destroy)
        self.QUIT.pack(pady=10)

    def add_patient(self):
        print("Add patient clicked")

    def add_observations(self):
        print("Add observations clicked")

    def view_ward(self):
        print("View ward clicked")

    def view_history(self):
        print("View patients history clicked")


root = tk.Tk()
app = Application(master=root)
app.mainloop()




