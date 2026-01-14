#This is a Python script to automatically set a file path

#Trin 1: Definere filstien (r"" fortæller Python at det er en rå streng)
adresse = r"C:\Users\ilhan\OneDrive - Aarhus universitet\Skrivebord"

#Trin 2: Definere semesteret
semester = "Semester 4"

#Trin 3: Liste over fag
subjects = ["M4MEA-01", "M4STI1-01", "M4TRM1-03", "M4PRJ4-05", "M3DYN1-03"]

#Trin 4: Oprette undermapper for alle fag ... ændres listen ændrer hele strukturen sig
subfolders = ["Undervisning", "Opgaver", "Eksamen", "Noter"]

#Trin 5: Import (her gives der adgang til filsystemet)
import os
semester_path = os.path.join(adresse, semester)
os.makedirs(semester_path, exist_ok=True)

#Os.path.join samler adresser pænt
#makedirs opretter mapper
#exist_ok=True undgår fejl hvis mappen allerede findes

#Trin 6: Struktur for hver fag -- Løkker
for subject in subjects:
    subject_path = os.path.join(semester_path, subject)
    os.makedirs(subject_path, exist_ok=True)
    for subfolder in subfolders:
        os.makedirs(os.path.join(subject_path, subfolder), exist_ok=True)

#Koden foroven siger at der oprettes en mappe for hvert fag og hver undermappe
print("Jeg har oprettet mappen her:", semester_path)
#Jeg kalder mappen for at sikre mig at den er oprettet det rigtige sted
