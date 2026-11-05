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

ID= input("what is the patients id number?")

print (ID)

SPO2 = input("What SPO2 scale is the patient on? (1 or 2)")
print(SPO2)

resprate= validate_number(
"What is the patients respiratory rate? ", 4, 50
)

spo2level= validate_number(
"What is the patients SPO2 level? ", 70, 100
)

on_oxygen= input("Is the patient on oxygen? (yes or no)")
print(on_oxygen)
if on_oxygen == "yes" or on_oxygen== "YES":
    on_oxygen = True
else: on_oxygen= False

bloodpressure= validate_number(
"What is the patients systolic blood pressure? ", 50, 250
)

pulse= validate_number(
"What is the patients pulse rate? ", 30, 200
)

conscience= input("What is the patients level of consciousness? (alert, confusion, voice, pain, unresponsive)")
if conscience== "alert" or conscience== "ALERT":
    conscience= "A"
elif conscience== "confusion" or conscience== "CONFUSION":
    conscience= "C"  
elif conscience== "voice" or conscience== "VOICE":
    conscience= "V"
elif conscience== "pain" or conscience== "PAIN":
    conscience= "P"
elif conscience== "unresponsive" or conscience== "UNRESPONSIVE":
    conscience= "U"

print(conscience)

temperature= validate_number("What is the patients temperature? (in degrees Celsius)", 28.0, 43.0, decimal=True)
                
y = score_all(resprate,spo2level,on_oxygen,bloodpressure,pulse,conscience,temperature)





#new_line = [a,b,c,d,e,f,g,h,i]
