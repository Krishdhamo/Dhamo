# from datetime import date


# print("Hello, World!")
# _apple_fruit = 10
# print(_apple_fruit)

# Data type
# numeric - int,float
# sequence - list,tuple,dict,set,str
# boolean - True,False
# none - None   
#  operators
# arithmetic - +,-,*,/,%,//,**
# comparison - ==,!=,>,<,>=,<=
# logical - and,or,not  
# assignment - =,+=,-=,*=,/=,%=,//=,**=
# bitwise - &,|,^,~,<<,>>
# identity - is,is not
#  membership - in,not in


# birth_year = int(input("Enter your birth year: "))
# current_year = 2026
# age = current_year - birth_year
# print("Your age is: ", age)

# age = int(input("Enter your age: "))
# maxage = 50
# amount = int(input("Enter the amount: "))
# total = (max_age - current_age)* 365 * amount
# print("Total: ", total)

# current_age = int(input("Enter your current age: "))
# max_age = int(input("Enter the age you want to live until: "))
# litres_water_per_day = int(input("Enter the amount of water you drink per day in litres: "))
# total_water = (max_age - current_age) * 365 * litres_water_per_day
# print("You will need ", total_water, " litres of water to last you until the age of ", max_age)

# trip_distance = int(input("Enter the distance of your trip in km: "))
# car_mileage = int(input("Enter your car's mileage in km/l: "))
# fuel_needed = trip_distance / car_mileage
# print("You will need ", fuel_needed, " litres of fuel for your trip.")
# cost_per_litre = int(input("Enter the cost of fuel per litre: "))
# total_cost = fuel_needed * cost_per_litre
# print("The total cost of fuel for your trip will be: ", total_cost)

# exno3 Monthly Mobile Data Usage
# daily_usage = float(input("Daily Data Usage of Data in GB :"))
# number_of_days_valid = int(input("Enter the Number of days in month "))
# total_usage = daily_usage * number_of_days_valid
# print("The Total Data usage",total_usage, "GB")

# Shopping Discount Calculator
# OG_price = float(input("Enter the Original Price of the item: "))
# discount_percentage = float(input("Enter the Discount Percentage: "))
# discount_amount = (discount_percentage / 100) * OG_price
# final_price = OG_price - discount_amount
# print("The Final Price after Discount is: ", final_price)

# x = int(input("Enter the number for x: "))
# y = int(input("Enter the number for y: "))
# if x > y:
#     print("x is greater than y")
# elif x < y:
#     print("x is less than y")
# else:
#     print("x is equal to y")

# poem = "Two roads diverged in a yellow wood"
# for i in poem :
#     if i in "aeiouAEIOU":
#         print(i," = vowel")
#     elif i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
#         print(i," = consonant")
#     else:
#         print(i," = space/Not Alphabet")

# mark= int(input("Enter your mark: "))
# if mark >= 0 and mark <= 100:
#     if mark == 100:
#         print("Grade: S")
#     elif mark >= 90:    
#         print("Grade: A")
#     elif mark >= 80:
#         print("Grade: B")
#     elif mark >= 70:    
#         print("Grade: C")
#     elif mark >= 60:
#         print("Grade: D")
#     elif mark >= 50:    
#         print("Grade: E")
#     else:
#         print("Grade: F")
# else:
#     print("Invalid mark. Please enter a mark between 0 and 100.")

x = float(input("Enter a Total Cost of dozen of bananas in Rs. : "))
y = float(input("Enter a Sold Cost of 1 banana in Rs. : "))
profit = (y * 12) - x
if profit > 0:
    print("Profit: Rs.", profit)
elif profit < 0:
    print("Loss: Rs.", -profit)
else:
    print("No Profit No Loss")
