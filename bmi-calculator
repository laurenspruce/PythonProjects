#using the metric system to calculate
#weight in kgs / height in meters squared
# cm / 100 to convert to meters

def calculate_bmi(height_cm, weight_kg):
    try:
        height_m = height_cm / 100.0
        bmi = round(weight_kg / (height_m**2), 2)
        return bmi
    except ZeroDivisionError:
        return None

def interpret_bmi(bmi):

    if bmi is None:
        return "Invalid input. Height should be greater than 0."
    
    if bmi < 18.5:
        return f"Your bmi is {bmi}, you are underweight."
    elif bmi < 24.9:
        return f"Your bmi is {bmi}, you are overweight."
    elif bmi < 34.9:
        return f"Your BMI is {bmi}, you are obese (Class I)."
    elif bmi < 39.9:
        return f"Your BMI is {bmi}, you are obese (Class II)."
    else:
        return f"Your BMI is {bmi}, you are obese (Class III)."
    
def main():

    try:
        height_cm = float(input("Please enter your height in centimeters: "))
        weight_kg = float(input("Please enter your weight in kilograms: "))

        bmi = calculate_bmi(height_cm,weight_kg)
        result = interpret_bmi(bmi)
        print(result)
    
    except ValueError:
        print("Invalid input. Please enter numerical values for height and weight.")

if __name__ == "__main__":
    main()
