import pandas as pd
import numpy as np


data = pd.read_csv('patient inputs.csv') # manual inptus 
print(data)





p001 = [18, 98, False, 120, 56, "A", 37.0]    #patient scores
p002 = [45, 90, True, 180, 90, "U", 40.0]
p003 = [18, 90, False, 120, 56, "A", 37.0]
p004 = [22, 95, False, 105, 105, "A", 38.5]


patient_data = np.column_stack((p001, p002, p003, p004))
print(patient_data)

np.savetxt("patient_data.csv", patient_data, delimiter=",", fmt='%s', header="Patient 1, Patient 2, Patient 3, Patient 4", comments='')