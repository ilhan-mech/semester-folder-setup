# Semester Folder Setup (Python)

I got tired of messy folders on my Desktop and the random chaos that happens every semester.
So I wrote a small Python script that creates a clean semester structure automatically.

It’s intentionally simple: 
1. One run
2. Folders are ready
3. I stop thinking about it.

## What it does
- Creates a semester folder on your Desktop (or any chosen base path)
- Creates one folder per course
- Creates subfolders inside each course (e.g. Notes, Assignments, Exam, etc.)
- Safe to run multiple times (it won’t crash if folders already exist)

## Example folder structure
Desktop/
└── Semester_4/
├── M4STI1-01/
│ ├── Undervisning/
│ ├── Opgaver/
│ ├── Eksamen/
│ └── Noter/
└── ...

## How to run
1. Open `src/Mappestruktur.py`
2. Set:
   - `adresse` (where you want the semester folder created)
   - `semester` (e.g. `Semester 4`)
   - `subjects` (your courses)
   - `subfolders` (your subfolder structure)
3. Run:
   ```bash
   python src/Mappestruktur.py

## Why this exists

This is my first “real” automation script: small, useful, and built from daily irritation.
I’m learning Python automation and building practical tools as I go.

