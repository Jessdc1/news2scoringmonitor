#bands definitions
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

#dictionary
CONSCIOUSNESS_SCORES = {
    "A": 0,
    "C": 3,
    "V": 3,
    "P": 3,
    "U": 3,
}

#functions
def show_score(value, bands):              #TO SHOW THE SCORE FOR THE VALUE AND BANDS
    for low, high, score in bands:
        if low <= value <= high:
            return score

def oxygen_score(on_oxygen):           #IF ON OXYGEN WILL RETURN 2, IF NOT WILL RETURN 0
    if on_oxygen:
        return 2
    return 0        

def pick_spo2_band(scale, on_oxygen):   #TO DECIDE WHICH SP02 SCALE TO USE
    if scale == 1:                           #ALWAYS USE SCALE 1 AND ELIF USED FOR IF OON OXYGEN THEN USE SCALE 2
        return SPO2_SCALE1_BANDS
    elif on_oxygen:
        return SPO2_SCALE2_OXYGEN_BANDS
    else:
        return SPO2_SCALE2_AIR_BANDS

def score_all(resp_rate, spo2, on_oxygen, systolic_bp, pulse, consciousness, temp, scale=1):  #scale 1 is scale for all healthy patients
    scores = {                                                                                #would use scale 2 for patients with respiratory condition
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
the risk level function takes the sum of the scores from the definitions and returns the risk level based on 
"""
def risk_level(scores):
    total = sum(scores.values())
    any_score_3 = 3 in scores.values()

    if total >= 7:
        return "High"
    elif total >= 5:    #ELIF IS USED FOR IF THE CHECKS ABOVE WERE FALSE THEN USE THE NEXT VALUE
        return "Medium"
    elif any_score_3:
        return "Low-medium"
    else:
        return "Low"                 #IF NONE WERE TRUE 
     

