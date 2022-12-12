#Day-3 leap year checker 
    #by supar

print("welcome to leap year checker, \n by supar")

year = int(input("enter a year "))

if year % 4 == 0:
    print(f"{year} is a leap year")
elif year % 100 != 0:
        print(f"{year} is not a leap year")
elif year % 400 == 0 :
        print (f"{year} is not a leap year")
else:
    print(f"{year} is not a leap year")
