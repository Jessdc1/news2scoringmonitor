from news2_functions import (
RESPRATE_BANDS, 
PULSE_BANDS, 
BP_BANDS, 
SPO2_SCALE1_BANDS, 
TEMPERATURE_BANDS, 
SPO2_SCALE2_AIR_BANDS, 
SPO2_SCALE2_OXYGEN_BANDS, 
CONSCIOUSNESS_SCORES, 
show_score, 
oxygen_score,
pick_spo2_band,
score_all, 
risk_level,
Patient
)

ward = {}

def validate_number(text, low, high, decimal=False):
    """
    validate number takes the text to be displayed, the high and low values for the input and returns a valid number within the range.
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
    def record observation asks the nurse to input the patients id and spo2 scale along with the vital scores, it checks them against the validation functions.
    """
    patientid = input("what is the patients id number?").strip().upper()


    SPO2scale = validate_number(
        "What SPO2 scale is the patient on? (1 or 2)", 1,2
    )

    resprate= validate_number(
        "What is the patients respiratory rate? ", 4, 50
    )

    spo2level= validate_number(
        "What is the patients SPO2 level? ", 70, 100
    )

    on_oxygen = ask_yes_no("Is the patient on oxygen? (yes or no) ")

    bloodpressure= validate_number(
        "What is the patients systolic blood pressure? ", 50, 250
    )

    pulse= validate_number(
        "What is the patients pulse rate? ", 30, 220
    )

    consciousness= ask_consciousness("What is the patients level of consciousness? (alert, confusion, voice, pain, unresponsive) ")

    temperature= validate_number("What is the patients temperature? (in degrees Celsius)", 28.0, 43.0, decimal=True)
                
    y = score_all(resprate,spo2level,on_oxygen,bloodpressure,pulse,consciousness,temperature)


def add_patient():
    """
    add patient will ask the nurse for the patientss id and spo2 scale and will check the patient doesnt already exist. It will then create a new patient.
    """
    patient_id = input("What is the patients id? e.g. P001").strip().upper()
    if patient_id in ward:
        print("Patient already exists")
        return
    spo2_scale = validate_number("What SPO2 scale is the patient on? (1 or 2) ", 1,2)
    new_patient = Patient(patient_id, spo2_scale)
    ward[patient_id] = new_patient
    print(f"Patient {patient_id} added to the ward.")


running=True
while running:
    print("NEWS2 SCORES")
    print("1.Add patient")
    print("2.Add observations")
    print("3.View patient ward")
    print("4.View patients history")
    print("5.Close")
    choice=input("Choose an option from 1-5:").strip()

    if choice == "1": add_patient()
    elif choice == "2": record_observation()
    elif choice == "3": print("Ward view")
    elif choice == "4": print("Patients history")
    elif choice == "5": 
        print ("Goodbye") 
        running=False
    else: print ("Please choose from options 1-5")

