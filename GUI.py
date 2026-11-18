import tkinter as tk
from tkinter import messagebox
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
        self.form = tk.Toplevel(self)
        self.form.title("Add Patient")
        self.id_label = tk.Label(self.form, text="Patient ID:")
        self.id_label.grid(row=0, column=0)
        self.id_entry = tk.Entry(self.form) #creates typing box inside window
        self.id_entry.grid(row=0, column=1)
        self.scale_label = tk.Label(self.form, text="SPO2 Scale:")
        self.scale_label.grid(row=1, column=0)
        self.scale_var = tk.IntVar(value=1)
        self.scale1= tk.Radiobutton(self.form, text="1", variable=self.scale_var, value=1)
        self.scale1.grid(row=1, column=1)
        self.scale2= tk.Radiobutton(self.form, text="2", variable=self.scale_var, value=2)
        self.scale2.grid(row=1, column=2)
        self.save_btn = tk.Button(self.form)
        self.save_btn["text"] = "Save"
        self.save_btn["command"] = self.save_new_patient
        self.save_btn.grid(row=2, column=1)

    def save_new_patient(self):
        patient_id=self.id_entry.get().strip().upper()
        if patient_id in self.ward:
            messagebox.showerror("Error", "Patient already exists")
            return
        if patient_id == "":
            messagebox.showerror("Error", "Please enter a patient ID")
            return
        messagebox.showinfo("Patient added", "Patient added to the ward")
        self.form.destroy()


    def add_observations(self):
        self.obs_form = tk.Toplevel(self)
        self.obs_form.title("Record Observations")
        self.obs_id_label = tk.Label(self.obs_form, text="Patient ID:")
        self.obs_id_label.grid(row=0, column=0)
        self.obs_id_entry = tk.Entry(self.obs_form) #creates typing box inside window
        self.obs_id_entry.grid(row=0, column=1)

        self.resp_rate_label = tk.Label(self.obs_form, text="Respiration Rate:")
        self.resp_rate_label.grid(row=1, column=0)
        self.resp_rate_entry = tk.Entry(self.obs_form) #creates typing box inside window
        self.resp_rate_entry.grid(row=1, column=1)

        self.spo2_label = tk.Label(self.obs_form, text="SpO2:")
        self.spo2_label.grid(row=2, column=0)
        self.spo2_entry = tk.Entry(self.obs_form) #creates typing box inside window
        self.spo2_entry.grid(row=2, column=1)

        self.oxygen_var=tk.BooleanVar(value=False)
        self.oxygen_check=tk.Checkbutton(self.obs_form, text="On Oxygen, variable=self.oxygen_var")
        self.oxygen_check.grid(row=3, column=1)

        self.systolic_bp_label = tk.Label(self.obs_form, text="Systolic Blood Pressure:")
        self.systolic_bp_label.grid(row=4, column=0)
        self.systolic_bp_entry = tk.Entry(self.obs_form) #creates typing box inside window
        self.systolic_bp_entry.grid(row=4, column=1)

        self.pulse_label = tk.Label(self.obs_form, text="Pulse:")
        self.pulse_label.grid(row=5, column=0)
        self.pulse_entry = tk.Entry(self.obs_form) #creates typing box inside window
        self.pulse_entry.grid(row=5, column=1)

        self.consciousness_label=tk.Label(self.obs_form, text="Consciousness (ACVPU)")
        self.consciousness_label.grid(row=6, column=0)
        self.consciousness_var=tk.StringVar(value="A")
        self.consciousness_menu=tk.OptionMenu(self.obs_form, self.consciousness_var, "A", "C", "V", "P", "U")
        self.consciousness_menu.grid(row=6, column=1)

        self.temperature_label = tk.Label(self.obs_form, text="Temperature (degrees celcius):")
        self.temperature_label.grid(row=7, column=0)
        self.temperature_entry = tk.Entry(self.obs_form) #creates typing box inside window
        self.temperature_entry.grid(row=7, column=1)

        self.save_obs_btn = tk.Button(self.obs_form)
        self.save_obs_btn["text"] = "Save"
        self.save_obs_btn["command"] = self.save_observation
        self.save_obs_btn.grid(row=8, column=1)

    def save_observation(self):
        print("save observation clicked")
        

    def view_ward(self):
        print("View ward clicked")

    def view_history(self):
        print("View patients history clicked")


root = tk.Tk()
app = Application(master=root)
app.mainloop()




