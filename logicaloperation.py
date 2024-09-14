#logical operators

temp = int(input("what is the temp?"))

if not(temp >= 0 and temp <=30):
    print("the temp is good today!")
elif not(temp < 0 or temp > 30):
    print("the temp is bad")



