#Implementing the BMI formula
#The function takes weight and height as arguments and returns the BMI

def bmi_calculator(weight, height):
    return weight/(height ** 2)


#This function classifies different BMI's as either underweight, normal weight,\
#overweight or obese
#It takes the BMI as an argument and returns the category to which the BMI belongs

def bmi_classification(bmi):
    if bmi < 18.5:
        #a bmi lesser than 18.5 is considered to be underweight
        return "Underweight."
    elif 18.5 <= bmi <= 24.9:
        #a bmi between 18.5 and 24.9 is Normal
        return "Normal Weight."
    elif 25 <= bmi <= 29.9:
        #a bmi between 25 and 29.9 is overweight
        return "Overweight."
    else:
        #a bmi greater than 29.9 is defined to be obese
        return "Obese." 


def main():
    print("\nBMI Calcularor!\n")#title
    try:
        #takes weight and height inputs from the user
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in metres: "))
    except ValueError:
        #when the user's input(s) are of the wrong type 
        print("Sorry, invalid input!!")
        return
    
    #calling 'bmi_calculator' function and passing weight and height as arguments
    #the return value(BMI) is stored in the variable named 'bmi'
    bmi = bmi_calculator(weight,height)
    #calling 'bmi_classification' function and passing 'bmi' as an argument
    #the return value(category) is stored in the variable named 'category'
    category = bmi_classification(bmi)
    
    print(f"\nBMI: {bmi:.2f}")#outputs the BMI with 2 decimal places
    print(f"Category: {category}")


# Checks if the script is being run as the main program
if __name__ == "__main__":
    main()