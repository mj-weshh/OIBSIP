# BMI Calculator
This Python script implements a Body Mass Index (BMI) calculator. The BMI is a measure of body fat based on weight and height. The script includes functions to calculate the BMI and classify it into different categories such as underweight, normal weight, overweight, or obese.

## BMI Calculation Formula
The main function bmi_calculator takes weight and height as arguments and returns the BMI using the formula:

```
BMI = weight / (height ** 2)
```

## BMI Classification

The script classifies the BMI into the following categories:

- **Underweight**: BMI less than 18.5
- **Normal Weight**: BMI between 18.5 and 24.9
- **Overweight**: BMI between 25 and 29.9
- **Obese**: BMI greater than or equal to 30

## How to Use

1. Run the script in a Python environment.
2. Enter your weight in kilograms when prompted.
3. Enter your height in meters when prompted.
4. The script will calculate your BMI and classify it into one of the categories mentioned above.


```bash
python bmi_calculator.py
```

## Input Validation

The script validates user inputs to ensure they are numeric. If the inputs are not valid (e.g., non-numeric or negative values), it displays an error message and exits.

## Example

```bash
BMI Calculator!

Enter your weight in kilograms: 70
Enter your height in meters: 1.75

BMI: 22.86
Category: Normal Weight
```
