# NEWS2 Ward Monitor

> **GenAI acknowledgement:** I acknowledge the use of Claude (Opus 5.5, Anthropic, https://claude.ai/) to help write this README and to help me learn Git and GitHub. This is allowed under the 'Full GenAI co-creation' category for Assessment 2.
>
> The Python code is Assessment 1 work, which follows the stricter GenAI-Assisted Reviewer rules. Each code file has its own GenAI acknowledgement at the top.

## What is this project?

This is a Python app that works out **NEWS2 scores** for patients on a hospital ward.

NEWS2 (National Early Warning Score 2) is a scoring system used in the NHS to spot patients who are getting more unwell. Nurses measure seven vital signs, each one gets a score, and the total shows how concerned staff should be about the patient.

The app comes in **two versions that do the same things**:

- **Text version**: runs in the terminal using a numbered menu
- **GUI version**: has windows and buttons, built with Tkinter

## Features

In both versions, a nurse can:

1. **Add a patient**: enter a patient ID and choose SpO2 Scale 1 or Scale 2
2. **Record observations**: enter the seven vital signs:
   - respiration rate
   - oxygen saturation (SpO2)
   - whether the patient is on oxygen
   - systolic blood pressure
   - pulse
   - level of consciousness (ACVPU)
   - temperature
3. **See the result straight away**: total score, risk level (Low, Low-medium, Medium or High) and the clinical response
4. **View the ward**: all patients listed with the highest risk at the top
5. **View a patient's history**: every observation for one patient, with the date and time

The app also:

- **checks inputs**: it rejects words where a number is needed, numbers outside a set range and blank or repeated patient IDs
- **saves automatically**: observations are stored in `ward_data.csv` and loaded again next time the app opens

## What is needed

- **Python 3.10 or newer** (this project was built and tested with Python 3.14.7)
- **Nothing else to install.** The app only uses tools that come with Python (`tkinter`, `csv` and `datetime`), so there is no `requirements.txt`.

Tkinter is included when you install Python on Windows or Mac.

## How to install

1. Download the project, either:
   - with Git:
     ```
     git clone https://github.com/Jessdc1/news2scoringmonitor.git
     ```
   - or on GitHub, click **Code and Download ZIP**, then unzip it
2. Open a terminal inside the project folder:
   ```
   cd news2scoringmonitor
   ```

## How to run it

**Text version**
```
python text_app.py
```
Type a number from 1 to 5 to choose an option, then answer the questions asked.

**GUI version**
```
python GUI.py
```
Click a button on the main window. Each option opens in its own window.

**Tests**
```
python news2_tests.py
```
If everything works, it prints `All tests passed`. If a test fails, Python stops and shows which test it was.

## What each file does

| File | What it does |
| `news2_functions.py` | The scoring logic used by both versions: score bands, scoring functions, the `Patient` class, and saving and loading the CSV |
| `text_app.py` | The text version |
| `GUI.py` | The GUI version |
| `news2_tests.py` | Automatic tests that check the scoring is correct |
| `.gitignore` | Tells Git not to track files that shouldn't be uploaded, like `__pycache__/`, virtual environments and `ward_data.csv` |
| `README.md` | This file |

`ward_data.csv` is created automatically the first time you save an observation. It is kept off GitHub on purpose so no patient data is uploaded.

## Known limitations

- A patient is only saved once they have at least one observation. If you add a patient and close the app without recording anything, that patient is lost.
- The allowed ranges for each vital sign are based on published sources but have not been checked by clinicians.


