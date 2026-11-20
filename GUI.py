# GenAI acknowledgement:
# Claude Anthropic was used as an assisted reviewer 
# To explain difficult python concepts that I was unsure on. 
# It reviewed my code and highlighted errors and improvements.
# All code was written by myself with the help of lecture notes, Python coding guides and a guide to Tkinter.

"""
A GUI version of the NEWS2 ward monitor app, built using Tkinter
The main window tab has 5 buttons which allows a nurse to
1. Add a patient to the ward
2. Record patient observations
3. View all patients on the ward
4. View patients history
5. Quit the app
Each option has its own seperate window. Errors and results appear in message boxes
Scoring logic and patient classes are imported from new2_functions
Data is saved and loaded from CSV
"""

import tkinter as tk   #Tkinter builds windows,buttons and boxes
from tkinter import messagebox  #Pop up boxes for errors and results
from news2_functions import (
get_risk_rank,
CLINICAL_CONCERN,
Patient,
save_ward,
load_ward
)

#CSV file
DATA_FILE = "ward_data.csv"

class Application(tk.Frame):
    """
    Main app window from tk.Frame, the app is inside the tkinter window. It stores the ward as a dictionary.
    Contains a method for each button and window.
    """
    def __init__(self, master=None):
        """
        Sets up the app when it starts. Master is the main window the app is inside. Loads the saved data and builds main menu.
        """
        tk.Frame.__init__(self, master) #runs tk.frame own setup first
        self.pack()  #put the frame inside the window
        self.ward = load_ward(DATA_FILE) #load saved patients from csv
        self.createWidgets() #build the buttons 

    def createWidgets(self):
        """
        Builds the main menu with a title label and one button per option
        Each button has a method that runs when it is clicked
        pady=10 adds a space above and below each item
        """
        self.title = tk.Label(self, text="NEWS2 Ward Monitor App") #App title
        self.title.pack(pady=10)

        self.add_btn = tk.Button(self) #Button 1 which opens the add patient
        self.add_btn["text"] = "Add patient"
        self.add_btn["command"] = self.add_patient
        self.add_btn.pack(pady=10)

        self.record_obs_btn = tk.Button(self) #Button 2 opens the record observations
        self.record_obs_btn["text"] = "Record Observations"
        self.record_obs_btn["command"] = self.add_observations
        self.record_obs_btn.pack(pady=10)

        self.ward_btn = tk.Button(self)#Button 3 opens the ward
        self.ward_btn["text"] = "View Ward"
        self.ward_btn["command"] = self.view_ward
        self.ward_btn.pack(pady=10)

        self.history_btn = tk.Button(self)#Button 4 opens patients history
        self.history_btn["text"] = "View Patient History"
        self.history_btn["command"] = self.view_history
        self.history_btn.pack(pady=10)

        self.QUIT = tk.Button(self, text="QUIT", fg="blue", command=self.master.destroy) #Button 5 closes down the app
        self.QUIT.pack(pady=10)

    def add_patient(self):
        """
        Opens up a tab to add a new patient into the ward.
        It has a box to enter the patients ID and a selection for which SpO2 scale and a save button to save to the ward.
        """
        self.form = tk.Toplevel(self) #creates a window ontop of the main one
        self.form.title("Add Patient")

        self.id_label = tk.Label(self.form, text="Patient ID:")
        self.id_label.grid(row=0, column=0)
        self.id_entry = tk.Entry(self.form) #creates typing box inside window
        self.id_entry.grid(row=0, column=1)
        self.scale_label = tk.Label(self.form, text="SpO2 Scale:")
        self.scale_label.grid(row=1, column=0)
        #Only one button can be selected as they share  scale_var
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
        """
        Checks the add patient and will reject a blank or a duplicate ID.
        Adds the patient to the ward.
        """
        patient_id = self.id_entry.get().strip().upper() #upper to make patient ID uppercase
        if patient_id == "":
            messagebox.showerror("Error", "Please enter a patient ID")
            return
        if patient_id in self.ward:
            messagebox.showerror("Error", "Patient already exists")
            return
        self.ward[patient_id] = Patient(patient_id, self.scale_var.get())
        messagebox.showinfo("Patient added", "Patient added to the ward")
        self.form.destroy()


    def add_observations(self):
        """
        Opens pop up to enter patient vital signs
        """
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
        self.oxygen_check=tk.Checkbutton(self.obs_form, text="On Oxygen", variable=self.oxygen_var)
        self.oxygen_check.grid(row=3, column=1)

        self.systolic_bp_label = tk.Label(self.obs_form, text="Systolic Blood Pressure:")
        self.systolic_bp_label.grid(row=4, column=0)
        self.systolic_bp_entry = tk.Entry(self.obs_form) #creates typing box inside window
        self.systolic_bp_entry.grid(row=4, column=1)

        self.pulse_label = tk.Label(self.obs_form, text="Pulse:")
        self.pulse_label.grid(row=5, column=0)
        self.pulse_entry = tk.Entry(self.obs_form) #creates typing box inside window
        self.pulse_entry.grid(row=5, column=1)

        #The drop down option allows for only ACVPU to be selected
        self.consciousness_label=tk.Label(self.obs_form, text="Consciousness (ACVPU)")
        self.consciousness_label.grid(row=6, column=0)
        self.consciousness_var=tk.StringVar(value="A")
        self.consciousness_menu=tk.OptionMenu(self.obs_form, self.consciousness_var, "A", "C", "V", "P", "U")
        self.consciousness_menu.grid(row=6, column=1)

        self.temperature_label = tk.Label(self.obs_form, text="Temperature (degrees celsius):")
        self.temperature_label.grid(row=7, column=0)
        self.temperature_entry = tk.Entry(self.obs_form) #creates typing box inside window
        self.temperature_entry.grid(row=7, column=1)

        self.save_obs_btn = tk.Button(self.obs_form)
        self.save_obs_btn["text"] = "Save"
        self.save_obs_btn["command"] = self.save_observation
        self.save_obs_btn.grid(row=8, column=1)

    def save_observation(self):
        """
        Adds the observation to the patient, saves the ward and shows the score, risk level and clinical response.
        """
        patient_id=self.obs_id_entry.get().strip().upper()
        if patient_id == "":
            messagebox.showerror("Error", "Please enter a patient ID")
            return
        if patient_id not in self.ward:
            messagebox.showerror("Error", "Patient not found")
            return
        patient = self.ward[patient_id]

        #check number returns None if a value is invalid from the range
        resp_rate = self.check_number(self.resp_rate_entry, "Respiration Rate", 4, 50)
        if resp_rate is None:
            return
        spo2 = self.check_number(self.spo2_entry, "SpO2", 70, 100)
        if spo2 is None:
            return
        systolic_bp = self.check_number(self.systolic_bp_entry, "Systolic Blood Pressure", 50, 250)
        if systolic_bp is None:
            return
        pulse = self.check_number(self.pulse_entry, "Pulse", 30, 220)
        if pulse is None:
            return
        temperature = self.check_number(self.temperature_entry, "Temperature", 28.0, 43.0, decimal=True)
        if temperature is None:
            return
        on_oxygen = self.oxygen_var.get()
        consciousness = self.consciousness_var.get()
        #the patient class calculates the score and risk level
        patient.add_observation(resp_rate,spo2,on_oxygen,systolic_bp,pulse,consciousness,temperature)
        latest = patient.latest_observation()
        save_ward(self.ward, DATA_FILE)

        messagebox.showinfo("Observation saved", f"Total score: {latest['total']}\nRisk level: {latest['risk']}\nClinical response: {CLINICAL_CONCERN[latest['risk']]}")
        self.obs_form.destroy()


    def check_number(self, entry, name, low, high, decimal=False):
        """
        Checks that a typing box has a number between high and low. If a decimal is true they are accepted and rounded to 1 d.p
        Returns the number or None if the number was invalid
        """
        try:
            answer = entry.get()
            if decimal:
                value = round(float(answer), 1)
            else:
                value = int(answer)
            if low <= value <= high:
                return value
            else:
                messagebox.showerror("Error", f"{name} must be between {low} and {high}")
                return None
        except ValueError:
            #text couldnt be converted into a number
            messagebox.showerror("Error", f"{name} must be a number")
            return None
        

    def view_ward(self):
        """
        Opens a window which lists all of the patient IDs, latest score and risk level.
        Sorted highest to lowest risk
        """
        if len(self.ward) == 0:
            messagebox.showinfo("View Ward", "No patients visible on the ward")
            return
        self.ward_window= tk.Toplevel(self)
        self.ward_window.title("Ward Overview")
        self.ward_list = tk.Listbox(self.ward_window, width=40)
        self.ward_list.pack(padx=10, pady=10)
        for patient in sorted(self.ward.values(), key= get_risk_rank, reverse=True):
            latest = patient.latest_observation()
            #latest is None if no observations have been recorded yet
            if latest is None:
                self.ward_list.insert(tk.END,f"{patient.patient_id} - no current observations")
            else:
                self.ward_list.insert(tk.END,f"{patient.patient_id} - Score: {latest['total']} - Risk: {latest['risk']}")

    def view_history(self):
        """
        Opens a window where a patient ID can be entered and it shows their history
        """
        self.history_window = tk.Toplevel(self)
        self.history_window.title("Patient History")
        self.history_id_label = tk.Label(self.history_window, text="Patient ID:")
        self.history_id_label.grid(row=0, column=0)
        self.history_id_entry = tk.Entry(self.history_window) 
        self.history_id_entry.grid(row=0, column=1)

        self.show_btn = tk.Button(self.history_window)
        self.show_btn["text"] = "Show"
        self.show_btn["command"] = self.show_history
        self.show_btn.grid(row=0, column=2)
        self.history_list = tk.Listbox(self.history_window, width=40)
        self.history_list.grid(row=1, column=0, columnspan=3)

    def show_history(self):
        """
        Fills the history with date, time, score and risk level for the chosen patient
        """
        patient_id=self.history_id_entry.get().strip().upper()
        if patient_id == "":
            messagebox.showerror("Error", "Please enter a patient ID")
            return
        if patient_id not in self.ward:
            messagebox.showerror("Error", "Patient not found")
            return
        patient = self.ward[patient_id]
        #clears the previous results before showing a new patient
        self.history_list.delete(0, tk.END)
        if len(patient.history) == 0:
            self.history_list.insert(tk.END,"No patient observations are recorded yet")
            return
        for observation in patient.history:
            self.history_list.insert(tk.END,f"{observation['recorded_at'].strftime('%d/%m/%Y %H:%M')} - Score: {observation['total']} - Risk: {observation['risk']}")
    



root = tk.Tk()
root.title("NEWS2 Ward Monitor")
app = Application(master=root)
app.mainloop()





