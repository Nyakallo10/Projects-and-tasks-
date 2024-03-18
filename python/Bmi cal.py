from tkinter import *
import requests
import json

root =Tk()
root.title("body mass index calculater")
root.geometry('500x100')
root.configure( background= "yellow")

def calculate_bmi(weight,height):
    bmi = weight / (height** 2)
    return bmi

# function: categorize bmi
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# function: weight validation
def get_valid_weight():
    while True:
        try:
            weight = float(input("Enter your weight in kilograms: "))
            if weight <= 0:
                raise ValueError("Weight must be a positive number.")
            return weight
        except ValueError as e:
            print("Invalid input:", e)

# function: height validation

def get_valid_height():
    while True:
        try:
            height = float(input("Enter your height in centiemeters: "))
            if height <= 0:
                raise ValueError("Height must be a positive number.")
            return height
        except ValueError as e:
            print("Invalid input:", e)

# function: main entry point
def main():
    weight = get_valid_weight()
    height = get_valid_height()

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print("Your BMI is:", round(bmi, 2))
    print("You are classified as:", category)


