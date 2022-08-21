#BMI 

w = int(input("Weight(kg):"))
h = float(input("Height(m):"))

BMI = w / h / h
print("%.2f BMI is" %BMI)

if BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normalweight")
elif BMI < 30:
    print("Overweight")
else :
    print("Obesity")

#cq

user = input("user:")
password = input("password:")

if user == "admin":
    if password == "Ad13n@23t":
        print("Welcome, admin")
    else:
        print("You are not admin")

else :
    print("You are not admin")
