# Day 05 – Student Grade Sheet Generator Using Python

## Overview

This project demonstrates core Python concepts including:
**Functions** – for modular and reusable logic
**Loops** – for iterating through subjects
**Dictionaries**– for storing subject-wise marks
**Lists** – for calculating averages
**Conditional Statements** – for grading and result evaluation
**Ternary Operator** – for determining pass/fail status

The goal is to build a **mini student grade sheet system** that can:
Accept student details and subject count
Collect and validate subject-wise marks
Calculate average marks
Assign grades based on performance
Determine pass or fail status

---

## Features

**1.Subject-wise Marks Collection**
Uses a for loop to collect marks dynamically
Stores subject and marks using a dictionary

**2.Input Validation**
Ensures marks are between 0 and 100
Stops execution immediately on invalid input

**3.Average Calculation**
Converts dictionary values into a list
Calculates average marks safely

**4.Grade Assignment**
Uses if / elif / else conditions:
A → Average ≥ 80
B → Average ≥ 50
C → Average ≥ 30
F → Fail

**5.Pass / Fail Status**
Uses a ternary operator to decide result

Clean and readable decision-making logic
## Example Input
Enter the your name : Rajesh
Enter the number of subjects : 2
Enter the subject 1 : Maths
Enter the marks secured in maths : 100
Enter the subject 2 : Science
Enter the marks secured in science : 70

## Example Output

{'name': 'Rajesh', 'Marks_list': [100, 70], 'Grade': 'A', 'Average': 85.0, 'Status': 'Pass'}

