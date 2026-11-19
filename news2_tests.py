"""
Tests for functions file to ensure all code works
"""

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
Patient,
)


#Respiration rate 
assert show_score(45, RESPRATE_BANDS) == 3, "RR 45"
assert show_score(22, RESPRATE_BANDS) == 2, "RR 22"
assert show_score(8, RESPRATE_BANDS) == 3, "RR 8"
assert show_score(9, RESPRATE_BANDS) == 1, "RR 9"

#Pulse 
assert show_score(56, PULSE_BANDS) == 0, "Pulse 56"
assert show_score(105, PULSE_BANDS) == 1, "Pulse 105"
assert show_score(130, PULSE_BANDS) == 2, "Pulse 130"
assert show_score(131, PULSE_BANDS) == 3, "Pulse 131"

#Systolic BP 
assert show_score(120, BP_BANDS) == 0, "BP 120"
assert show_score(105, BP_BANDS) == 1, "BP 105"
assert show_score(90, BP_BANDS) == 3, "BP 90"
assert show_score(91, BP_BANDS) == 2, "BP 91"

#SpO2 scale 1 
assert show_score(98, SPO2_SCALE1_BANDS) == 0, "SpO2 S1 98"
assert show_score(90, SPO2_SCALE1_BANDS) == 3, "SpO2 S1 90"
assert show_score(95, SPO2_SCALE1_BANDS) == 1, "SpO2 S1 95"
assert show_score(96, SPO2_SCALE1_BANDS) == 0, "SpO2 S1 96"

#Temperature
assert show_score(37.0, TEMPERATURE_BANDS) == 0, "Temp 37.0"
assert show_score(40.0, TEMPERATURE_BANDS) == 2, "Temp 40.0"
assert show_score(35.0, TEMPERATURE_BANDS) == 3, "Temp 35.0"
assert show_score(35.1, TEMPERATURE_BANDS) == 1, "Temp 35.1"
assert show_score(36.1, TEMPERATURE_BANDS) == 0, "Temp 36.1"

#Consciousness
assert CONSCIOUSNESS_SCORES["A"] == 0, "Consciousness A"
assert CONSCIOUSNESS_SCORES["U"] == 3, "Consciousness U"

#Oxygen 
assert oxygen_score(True) == 2, "On oxygen"
assert oxygen_score(False) == 0, "On air"

#SpO2 scale 2 
assert show_score(95, SPO2_SCALE2_AIR_BANDS) == 0, "SpO2 S2 air 95"
assert show_score(95, SPO2_SCALE2_OXYGEN_BANDS) == 2, "SpO2 S2 oxygen 95"
assert show_score(90, SPO2_SCALE2_OXYGEN_BANDS) == 0, "SpO2 S2 oxygen 90"
assert show_score(85, SPO2_SCALE2_AIR_BANDS) == 2, "SpO2 S2 air 85"

#pick spo2 band 
assert show_score(95, pick_spo2_band(1, False)) == 1, "pick S1 air"
assert show_score(95, pick_spo2_band(2, False)) == 0, "pick S2 air"
assert show_score(95, pick_spo2_band(2, True)) == 2, "pick S2 oxygen"

#score all totals
p001 = score_all(18, 98, False, 120, 56, "A", 37.0)
p002 = score_all(45, 90, True, 180, 90, "U", 40.0)
p003 = score_all(18, 90, False, 120, 56, "A", 37.0)
p004 = score_all(22, 95, False, 105, 105, "A", 38.5)

assert sum(p001.values()) == 0, "p001 total"
assert sum(p002.values()) == 13, "p002 total"
assert sum(p003.values()) == 3, "p003 total"
assert sum(p004.values()) == 6, "p004 total"

#risk level 
assert risk_level(p001) == "Low", "p001 risk"
assert risk_level(p002) == "High", "p002 risk"
assert risk_level(p003) == "Low-medium", "p003 risk"
assert risk_level(p004) == "Medium", "p004 risk"

#Patient class 
test_patient = Patient("p001", 1)
assert test_patient.patient_id == "p001", "patient_id"
assert test_patient.spo2_scale == 1, "spo2_scale"
assert test_patient.history == [], "empty history"

test_patient.add_observation(18, 98, False, 120, 56, "A", 37.0)
assert len(test_patient.history) == 1, "history length"
assert test_patient.history[0]["total"] == 0, "history total"
assert test_patient.history[0]["risk"] == "Low", "history risk"

assert test_patient.latest_observation()["risk"] == "Low", "latest risk"

empty_patient = Patient("P002", 1)
assert empty_patient.latest_observation() is None, "empty latest"

print("All tests passed")
