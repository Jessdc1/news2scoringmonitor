"""
NEWS2 scoring system in python. Containing band definitions, scoring functions and a patient class to store the patients history.
"""
from datetime import datetime

import csv

# ===== BAND DEFINITIONS =====
#The band definitions are defined as a list containing tuples. 
#Each tuple contains first the lower limit, then the upper limit and the score given for that range.

RESPRATE_BANDS = [
    (4, 8, 3),
    (9, 11, 1),
    (12, 20, 0),
    (21, 24, 2),  
    (25, 50, 3),  
]   

PULSE_BANDS = [
    (30, 40, 3),
    (41, 50, 1),
    (51, 90, 0),
    (91, 110, 1),
    (111, 130, 2),
    (131, 220, 3),
]

BP_BANDS = [
    (50, 90, 3),
    (91, 100, 2),
    (101, 110, 1),
    (111, 219, 0),
    (220, 250, 3),
]

SPO2_SCALE1_BANDS = [
    (70, 91, 3),
    (92, 93, 2),
    (94, 95, 1),
    (96, 100, 0),
]

TEMPERATURE_BANDS = [
    (28.0, 35.0, 3),
    (35.1, 36.0, 1),
    (36.1, 38.0, 0),
    (38.1, 39.0, 1),
    (39.1, 43.0, 2),
]

SPO2_SCALE2_AIR_BANDS = [
    (70, 83, 3),
    (84, 85, 2),
    (86, 87, 1),
    (88, 100, 0),
]

SPO2_SCALE2_OXYGEN_BANDS = [
    (70, 83, 3),
    (84, 85, 2),
    (86, 87, 1),
    (88, 92, 0),
    (93, 94, 1),
    (95, 96, 2),
    (97, 100, 3),
]

# ===== CONSCIOUSNESS SCORES =====
#The dictionary is used to store the scores for each consciousness level.
CONSCIOUSNESS_SCORES = {
    "A": 0,
    "C": 3,
    "V": 3,
    "P": 3,
    "U": 3,
}

# ==== CLINICAL CONCERN =====
CLINICAL_CONCERN = {
    "Low": "ward-based response",
    "Low-medium": "Urgent ward-based response",
    "Medium": "Key threshold for urgent response",
    "High": "Urgent or emergency response"
}

# ===== RISK RANKING =====
RISK_RANKING = {
    "High": 4,
    "Medium": 3,
    "Low-medium": 2,
    "Low": 1
}

# ===== CSV COLUMNS =====
CSV_COLUMNS = ["patient_id", "spo2_scale", "recorded_at", "resp_rate", "spo2", "on_oxygen", "systolic_bp", "pulse", "consciousness", "temperature", "total", "risk"]

# ===== FUNCTIONS =====
#The functions are used to calculate the scores from each paramater and returns the total score and risk level.

def show_score(value, bands):              
    """
    show score takes the value and the bands as an input and returns the score for the value based on the bands given.
    """
    for low, high, score in bands:
        if low <= value <= high:
            return score
        

def oxygen_score(on_oxygen):           
    """
    oxygen score takes a boolean value indicating whether the person is on oxygen and returns a score of 2 if true and 0 if false.
    """
    if on_oxygen:
        return 2
    return 0        


def pick_spo2_band(scale, on_oxygen):   
    """
    pick spo2 band takes the scale and a boolean indicating whether the person is on oxygen and returns the correct bands.
    """
    if scale == 1:                           
        return SPO2_SCALE1_BANDS  
    elif on_oxygen:                  
        return SPO2_SCALE2_OXYGEN_BANDS
    else:
        return SPO2_SCALE2_AIR_BANDS  
    

def score_all(resp_rate, spo2, on_oxygen, systolic_bp, pulse, consciousness, temperature, scale=1):  
    """
    score all takes the values for each of the paramaters and returns a dictionary containing the scores for each.
    """
    scores = {                                                                              
        "resp_rate": show_score(resp_rate, RESPRATE_BANDS), 
        "spo2": show_score(spo2, pick_spo2_band(scale, on_oxygen)),
        "on_oxygen": oxygen_score(on_oxygen),                          
        "systolic_bp": show_score(systolic_bp, BP_BANDS),
        "pulse": show_score(pulse, PULSE_BANDS),
        "consciousness": CONSCIOUSNESS_SCORES[consciousness],
        "temperature": show_score(temperature, TEMPERATURE_BANDS),
    }

    return scores


def risk_level(scores):                           
    """
    The risk level function takes the sum of the scores from the definitions and returns the risk level based on the total score and also looks for any score of 3.
    """
    total = sum(scores.values())
    any_score_3 = 3 in scores.values()     

    if total >= 7:
        return "High"
    elif total >= 5:    
        return "Medium"
    elif any_score_3:
        return "Low-medium"
    else:
        return "Low"      
     
def get_risk_rank(patient):
    """
    get risk rank will give a number for how serious the patients condition is will return 0 if the patient has no observations.
    """
    latest = patient.latest_observation()
    if latest is None:
        return 0
    else:
        return RISK_RANKING[latest['risk']]

def save_ward(ward, filename):
    """
    save ward will save patient observations onto a csv
    """
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        for patient in ward.values():
            for observation in patient.history:
                row = { 
                    "patient_id": patient.patient_id,
                    "spo2_scale": patient.spo2_scale,
                    "recorded_at": observation["recorded_at"],
                    "resp_rate": observation["resp_rate"],
                    "spo2": observation["spo2"],
                    "on_oxygen": observation["on_oxygen"],
                    "systolic_bp": observation["systolic_bp"],
                    "pulse": observation["pulse"],
                    "consciousness": observation["consciousness"],
                    "temperature": observation["temperature"],
                    "total": observation["total"],
                    "risk": observation["risk"]
                }
                writer.writerow(row)



# ===== PATIENT CLASS =====
class Patient:
    """
    patient class is used to create a patient with an id and spo2 scale. History is also created as an empty list to store patient history.
    """
    def __init__(self, patient_id, spo2_scale):
        self.patient_id = patient_id
        self.spo2_scale = spo2_scale
        self.history = []

    def add_observation(self, resp_rate, spo2, on_oxygen, systolic_bp, pulse, consciousness, temperature, recorded_at=None):
        """
        add observation takes the values for the parameters and adds them to the patients history.
        """

        scores = score_all(resp_rate, spo2, on_oxygen, systolic_bp, pulse, consciousness, temperature, self.spo2_scale)
        
        #scores are calculated using score all function
        
        risk = risk_level(scores)
        
        #risk level is calculated using the risk level function created
        
        if recorded_at is None:
                recorded_at = datetime.now()

        observation = {
            "recorded_at": recorded_at,
            "resp_rate": resp_rate,
            "spo2": spo2,
            "on_oxygen": on_oxygen,
            "systolic_bp": systolic_bp,
            "pulse": pulse,
            "consciousness": consciousness,
            "temperature": temperature,
            "scores": scores,
            "total": sum(scores.values()),
            "risk": risk,
        }

        self.history.append(observation)


    def latest_observation(self):
        """
        latest observation returns the last observation in the patients history.
        """
        if len(self.history) == 0:
            return None   #if no history is present then the function returns none
        return self.history[-1] #if history is present it will return the last observation


