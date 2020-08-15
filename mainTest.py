height=float(input("Please input your height (in meters):"))
weight=float(input("Please input your weight (in kilograms)："))
bmi=weight/(height*height)
print("Your Body Mass Index is："+str(bmi))
if bmi>18.5 and bmi<24.9:
    print("You are underweight ~@_@~")
if bmi>=24.9 and bmi<29.9:
    print("Your weight is normal (-_-)")
if bmi>=29.9:
    print("You are overweight ^@_@^")