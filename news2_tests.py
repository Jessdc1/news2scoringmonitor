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
risk_level
)



#tests
print(show_score(45, RESPRATE_BANDS)) #predict 3
print(show_score(22, RESPRATE_BANDS)) #predict 2
print(show_score(8, RESPRATE_BANDS)) #predict 3
print(show_score(9, RESPRATE_BANDS)) #predict 1

print(show_score(56, PULSE_BANDS))   #predict 0
print(show_score(105, PULSE_BANDS))  #predict 1
print(show_score(130, PULSE_BANDS))  #predict 2
print(show_score(131, PULSE_BANDS))  #predict 3

print(show_score(120, BP_BANDS))     #predict 0
print(show_score(105, BP_BANDS))     #predict 1
print(show_score(90, BP_BANDS))      #predict 3
print(show_score(91, BP_BANDS))      #predict 2

print(show_score(98, SPO2_SCALE1_BANDS))   #predict 0
print(show_score(90, SPO2_SCALE1_BANDS))   #predict 3
print(show_score(95, SPO2_SCALE1_BANDS))   #predict 1
print(show_score(96, SPO2_SCALE1_BANDS))   #predict 0

print(show_score(37.0, TEMPERATURE_BANDS))    #predict 0
print(show_score(40.0, TEMPERATURE_BANDS))    #predict 2
print(show_score(35.0, TEMPERATURE_BANDS))    #predict 3
print(show_score(35.1, TEMPERATURE_BANDS))    #predict 1
print(show_score(36.1, TEMPERATURE_BANDS))   #predict 0

print(CONSCIOUSNESS_SCORES["A"])   #predict 0
print(CONSCIOUSNESS_SCORES["U"])   #predict 3

print(oxygen_score(True))    #predict 2
print(oxygen_score(False))   #predict 0

print(show_score(95, SPO2_SCALE2_AIR_BANDS))   #predict 0
print(show_score(95, SPO2_SCALE2_OXYGEN_BANDS))    #predict 2
print(show_score(90, SPO2_SCALE2_OXYGEN_BANDS))    #predict 0
print(show_score(85, SPO2_SCALE2_AIR_BANDS))   #predict 2

print(show_score(95, pick_spo2_band(1, False)))   #predict 1
print(show_score(95, pick_spo2_band(2, False)))   #predict 0
print(show_score(95, pick_spo2_band(2, True)))    #predict 2

p001 = score_all(18, 98, False, 120, 56, "A", 37.0)    #patient scores
p002 = score_all(45, 90, True, 180, 90, "U", 40.0)
p003 = score_all(18, 90, False, 120, 56, "A", 37.0)
p004 = score_all(22, 95, False, 105, 105, "A", 38.5)

print(sum(p001.values()))   #predict 0
print(sum(p002.values()))   #predict 13
print(sum(p003.values()))   #predict 3
print(sum(p004.values()))   #predict 6

print(risk_level(p001))   #predict Low
print(risk_level(p002))   #predict High
print(risk_level(p003))   #predict Low-medium
print(risk_level(p004))   #predict Medium