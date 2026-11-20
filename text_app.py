# GenAI acknowledgement:
# Claude (Opus 5.5, Anthropic, https://claude.ai/) was used as a 'GenAI-assisted reviewer
# To provide feedback on a draft of my work.
# To explain difficult Python concepts that I was unsure on. 
# It reviewed my code and highlighted errors in spelling and grammar improvements.
# All code was written by myself with the help of lecture notes, Python coding guides.

"""
A text-based app which allows for a nurse to choose from 5 options on a menu to
1. Add a patient into their ward
2. Record the patients observations and get a score for them
3. View the patients on the ward and see which has the highest risk
4. View one of the patients full observation history
5. Close the app

All of the scoring logic code and classes are imported from news2_functions. All of the data is saved to and can be loaded from a csv file.
"""
#Imports for the code
from news2_functions import (
get_risk_rank,
CLINICAL_CONCERN,
Patient,
save_ward,
load_ward
)

#Name of CSV file where the ward is saved
DATA_FILE = "ward_data.csv"

#Load any patients saved when the app is loaded and ward is a dictionary
ward = load_ward(DATA_FILE)


def validate_number(text, low, high, decimal=False):
    """
    validate number asks the user to enter a number until it is valid, shows the high and low values for the input and returns a valid number within the range.
    """
    while True:
        try:
            answer = input(text)
            if decimal:
                value = round(float(answer), 1)
            else:
                value = int(answer)
            if low <= value <= high:
                return value
            else:
                print(f"Please enter a number between {low} and {high}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def ask_yes_no(text):
    """
    ask yes no takes the text to be displayed and returns a boolean value based on the users input.
    """
    while True:
        answer = input(text).lower()
        if answer in ["yes", "no"]:
            return answer == "yes"
        print("Please enter 'yes' or 'no'.")


def ask_consciousness(text):
    """
    ask consciousness takes the text to be displayed and returns a valid level of consciousness based on the users input.
    """
    while True:
        answer = input(text).strip().lower()
        if answer == "alert":
            return "A"
        elif answer == "confusion":
            return "C"
        elif answer == "voice":
            return "V"
        elif answer == "pain":
            return "P"
        elif answer == "unresponsive":
            return "U"
        print("Please enter a valid level of consciousness (alert, confusion, voice, pain, unresponsive).")


def record_observation():
    """
    record observation checks whether the patient exists
    asks for each vital sign, adds the observation to the patient and prints the score, risk level and clinical response,
    saves the ward to the csv
    """
    patient_id = input("what is the patients id number?").strip().upper()
    if patient_id not in ward:
        print("Patient does not exist in the ward")
        return
    patient = ward[patient_id]

    resp_rate= validate_number(
        "What is the patients respiratory rate? ", 4, 50
    )

    SpO2= validate_number(
        "What is the patients SpO2 level? ", 70, 100
    )

    on_oxygen = ask_yes_no("Is the patient on oxygen? (yes or no) ")

    systolic_bp= validate_number(
        "What is the patients systolic blood pressure? ", 50, 250
    )

    pulse= validate_number(
        "What is the patients pulse rate? ", 30, 220
    )

    consciousness= ask_consciousness("What is the patients level of consciousness? (alert, confusion, voice, pain, unresponsive) ")

    temperature= validate_number("What is the patients temperature? (in degrees Celsius)", 28.0, 43.0, decimal=True)
                
    patient.add_observation(resp_rate,SpO2,on_oxygen,systolic_bp,pulse,consciousness,temperature)

    latest = patient.latest_observation()
    print(f"Your patients total score is {latest['total']}")
    print(f"Risk level:{latest['risk']}")
    print(f"Clinical response: {CLINICAL_CONCERN[latest['risk']]}")
    save_ward(ward, DATA_FILE)

def add_patient():
    """
    add patient will ask the nurse for the patients id and spo2 scale and will check the patient doesnt already exist. It will then create a new patient.
    """
    patient_id = input("What is the patients id? e.g. P001").strip().upper()
    if patient_id == "":
        print("Please enter a patient ID")
        return
    if patient_id in ward:
        print("Patient already exists")
        return
    spo2_scale = validate_number("What SpO2 scale is the patient on? (1 or 2) ", 1,2)
    new_patient = Patient(patient_id, spo2_scale)
    ward[patient_id] = new_patient
    print(f"Patient {patient_id} added to the ward.")

def view_ward():
    """
    view ward will show the nurse the patients id,overall score and risk level and a message if no patient is present.
    """
    if len(ward) == 0:
        print("No patients are visible in the ward")
        return
    for patient in sorted(ward.values(), key= get_risk_rank, reverse=True):
        latest = patient.latest_observation()
        if latest is None:
            print(f"{patient.patient_id} - no current observations")
        else:
            print(f"{patient.patient_id} - Score: {latest['total']} - Risk: {latest['risk']}")


def view_history():
    """
    view history will show the nurse the patients previous history,scores and risk level.
    """
    patient_id = input("what is the patients id number?").strip().upper()
    if patient_id not in ward:
        print("Patient does not exist in the ward")
        return
    patient = ward[patient_id]
    if len(patient.history) == 0:
        print("No patient observations are recorded yet")
        return
    for observation in patient.history:
        print(f"{observation['recorded_at'].strftime('%d/%m/%Y %H:%M')} - Score: {observation['total']} - Risk: {observation['risk']}")



#Keeps showing the menu until the user clicks 5 to close the app
running=True
while running:
    print("NEWS2 Ward Monitor App")
    print("1.Add patient")

    print("2.Record observations")

    print("3.View ward")

    print("4.View history")

    print("5.Close")
    
    choice=input("Choose an option from 1-5:").strip()

#Runs the function that matches the users input
    if choice == "1": add_patient()
    elif choice == "2": record_observation()
    elif choice == "3": view_ward()
    elif choice == "4": view_history()
    elif choice == "5": 
        print ("Goodbye") 
        running=False  #Ends the loop so the app closes
    else: print ("Please choose from options 1-5")



