from news2_functions import (
get_risk_rank,
CLINICAL_CONCERN,
Patient,
save_ward
)

ward = {}
DATA_FILE = "ward_data.csv"

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
    patient_id = input("what is the patients id number?").strip().upper()
    if patient_id not in ward:
        print("Patient does not exist in the ward")
        return
    patient = ward[patient_id]

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
                
    patient.add_observation(resprate,spo2level,on_oxygen,bloodpressure,pulse,consciousness,temperature)

    latest = patient.latest_observation()
    print(f"Your patients total score is {latest['total']}")
    print(f"Risk level:{latest['risk']}")
    print(f"Clinical response: {CLINICAL_CONCERN[latest['risk']]}")
    save_ward(ward, DATA_FILE)

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

def view_ward():
    """
    view ward will show the nurse thr patients id,overall score and risk level and a message if no patient is present.
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
    elif choice == "3": view_ward()
    elif choice == "4": view_history()
    elif choice == "5": 
        print ("Goodbye") 
        running=False
    else: print ("Please choose from options 1-5")



