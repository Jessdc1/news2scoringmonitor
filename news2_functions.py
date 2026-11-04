"""
The band defintions are defined as a list containing tuples. Each tuple contains first the lower limit, then the upper limit and the score given for that range.
"""


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
    (96, 100,0),
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

"""
The dictionary is used to store the scores for each consciousness level.
"""

#dictionary
CONSCIOUSNESS_SCORES = {
    "A": 0,
    "C": 3,
    "V": 3,
    "P": 3,
    "U": 3,
}


"""
The functions are used to calculate the scores from each paramater and returns the total score and risk level.
"""
#functions
def show_score(value, bands):              #TO SHOW THE SCORE FOR THE VALUE AND BANDS
    for low, high, score in bands:
        if low <= value <= high:
            return score

def oxygen_score(on_oxygen):           #TAKES THE SCORE OF WHETHER THE PERSON IS ON OXYGEN OR NOT AND RETURNS A SCORE OF 2 IF TRUE AND 0 IF FALSE.
    if on_oxygen:
        return 2
    return 0        

def pick_spo2_band(scale, on_oxygen):   #TO DECIDE WHICH SP02 SCALE TO USE
    if scale == 1:                           #IF IT IS SCALE 1 THEN IT RETURNS THE VALUES FROM SCALE 1
        return SPO2_SCALE1_BANDS  
    elif on_oxygen:                  #IF STEP 1 IS FALSE AND THE PERSON IS ON OXYGEN THEN IT WILL RETURN THE VALUES FROM SCALE 2 OXYGEN LIST
        return SPO2_SCALE2_OXYGEN_BANDS
    else:
        return SPO2_SCALE2_AIR_BANDS  #IF NEITHER OF THE ABOVE ARE TRUE THEN THE VALLUES WILL BE RETURNED FROM SCALE 2 AIR LIST

def score_all(resp_rate, spo2, on_oxygen, systolic_bp, pulse, consciousness, temp, scale=1):  #SCALE 1 IS USED AS DEFAULT UNLESS OTHERWISE SPECIFIED.
    scores = {                             #DICTIONARY USED TO STORE THE SCORES FOR EACH PARAMETER                                                   
        "resp_rate": show_score(resp_rate, RESPRATE_BANDS), 
        "spo2": show_score(spo2, pick_spo2_band(scale, on_oxygen)),
        "on_oxygen": oxygen_score(on_oxygen),                          #gives a score for all paramaters and returns as a dictionary
        "systolic_bp": show_score(systolic_bp, BP_BANDS),
        "pulse": show_score(pulse, PULSE_BANDS),
        "consciousness": CONSCIOUSNESS_SCORES[consciousness],
        "temp": show_score(temp, TEMPERATURE_BANDS),
    }
    return scores


"""
the risk level function takes the sum of the scores from the definitions and returns the risk level based on the total score and also looks for any score of 3.
"""
def risk_level(scores):                           
    total = sum(scores.values())
    any_score_3 = 3 in scores.values()     #THIS CHECKS WHETHER ANY SCORE IS 3 AND THEN RETURNS A BOOLEAN VALUE.

    if total >= 7:
        return "High"
    elif total >= 5:    #ELIF IS USED FOR IF THE CHECKS ABOVE WERE FALSE THEN USE THE NEXT VALUE
        return "Medium"
    elif any_score_3:
        return "Low-medium"
    else:
        return "Low"      #IF NONE WERE TRUE THEN THE VALUE IS RETURNED AS LOW
     

#classes
class Patient:
    def __init__(self, patient_id, spo2_scale):
        self.patient_id = patient_id
        self.spo2_scale = spo2_scale
        self.history = []
