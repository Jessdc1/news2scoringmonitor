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
        self.QUIT = tk.Button(self, text="QUIT", fg="blue", command=self.master.destroy)
        self.QUIT.pack(pady=10)
        self.btn2 = tk.Button(self)
        self.btn2.pack(pady=10)
        self.btn2["text"] = "Enter patients ID and SPO2 scale"
root = tk.Tk()
app = Application(master=root)
app.mainloop()


