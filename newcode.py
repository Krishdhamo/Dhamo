# Type_of_Studnet = input("Enter the type of student (MESD/MESH/MGSH/MGSDS): ")

# tution_fee = float(input("Enter the tuition fee : "))

# Bus_fee = float(input("Enter the bus fee  : "))

# hostel_fee = float(input("Enter the hostel fee  : "))

# if Type_of_Studnet == "MESD":
#     total_fee = tution_fee + Bus_fee
#     print("Total fee for Merit Seat Day Scholar student is: ", total_fee)
# elif Type_of_Studnet == "MESH":
#     total_fee = tution_fee + hostel_fee
#     print("Total fee for Merit Seat Hostler student is: ", total_fee)
# elif Type_of_Studnet == "MGSH":
#     total_fee = (tution_fee*1.5)+ hostel_fee
#     print("Total fee for Management Seat Hostler student is: ", total_fee)
# elif Type_of_Studnet == "MGSDS":
#     total_fee = (tution_fee*1.5)+ Bus_fee
#     print("Total fee for Management Seat Day Scholar is: ", total_fee)
# else:
#     print("Invalid type of student. Please enter MSD, MGSH, or MGSDS.")


# ATM Withdrawal Check 
# Limit = 10000
# account_balance = float(input("Enter the account balance : "))
# withdrawel_amount = float(input("Enter the withdrawel amount : "))

# if withdrawel_amount > account_balance:
#     print("Insufficient funds")
# elif withdrawel_amount > Limit:
#     print("Withdrawal amount exceeds the limit")
# else :
#     print("withdraw = ",withdrawel_amount)

# account_balance = 10000
# ATM_Pin = int(input("Enter the PIN = "))
# if ATM_Pin == 4073:
#     print("continue")
#     withdrawel_amount = float(input("Enter the withdrawel amount : "))
#     if (withdrawel_amount > account_balance) and (withdrawel_amount > 0):
#         print("Insufficient funds or Wrong input")
#     elif withdrawel_amount < 0:
#         print("Invalid Amount")
#     else :
#         print("withdraw Successfull = ",withdrawel_amount)
#         print("Account balance =",account_balance - withdrawel_amount)
# else :
#     print("Wrong PIN")

# print("PVR Cinimas / INOX Leisure Limited")
# Age = int(input("Enter the Age : "))
# showtime = input("SHOWTIME (Morning/Evening) = ")
# if Age < 5:
#     print("Free Entry")
# elif Age < 17:
#     print("Child Ticket")
#     if showtime == "Morning":
#         print("Ticket Price: ",150-(150*0.5))
#     else:
#         print("Ticket Price: ",150)
# elif Age < 60:
#     print("Adult Ticket")
#     if showtime == "Morning":
#         print("Ticket Price: ",250-(250*0.5))
#     else:
#         print("Ticket Price: ",250)
# else:  
#     print("Senior Citizen Ticket")
#     if showtime == "Morning":
#         print("Ticket Price: ",200-(200*0.5))
#     else:
#         print("Ticket Price: ",200)

# loop
# n =100
# i = 0
# sum = 0
# while i <= n:
#     if i % 2 != 0:
#         sum = sum + i
#         print("odd number: ", i)
#     i = i + 1
# # for i in range(1, n+1):
# #     if i % 2 != 0:
# #         sum = sum + i
# #         print("odd number: ", i)
# print("Sum of odd numbers from 1 to 100 is: ", sum)

# for i in range(1, n+1, 2):
#     sum = sum + i
#     print("odd number: ", i)
# print("Sum of odd numbers from 1 to 100 is: ", sum)

# for i in range(2, n+1,2):
#     sum = sum + i
#     print("even number: ", i)
# print("Sum of even numbers from 1 to 100 is: ", sum)

# for i in range(1, 11):
#     print("5 x", i, "=", 5*i)

# eng = int(input("Enter the marks of English : "))
# maths = int(input("Enter the marks of Maths : "))
# science = int(input("Enter the marks of Science : "))   
# social = int(input("Enter the marks of Social : "))
# tamil = int(input("Enter the marks of Tamil : "))

# total_marks = eng + maths + science + social + tamil
# average_marks = total_marks / 5
# print("Total Marks: ", total_marks)
# print("Average Marks: ", average_marks)

# n = int(input("Enter the number of rows for the pattern: "))
# for i in range(1, n+1):
#     print("*"*i)
# for i in range(1,n+1):
#     print("*"*(n-i+1))

# while n > 0:
#     print("*"*n)
#     n = n - 1
# i = 0
# while i <= n:
#     i = i + 1
#     print("*"*i)


# n =100
# i = 0
# sum = 0
# while i <= n:
#     if i % 2 == 0:
#         sum = sum + i
#         print("even number: ", i)
#     i = i + 1
# print("Sum of even numbers from 1 to 100 is: ", sum)

i = 1
n = int(input("Enter the total number of seats: "))
while (n>0):
    seatno = str(i)
    passenger_name = input("Enter the name of the Passenger: ")
    print("seatno ",seatno,"booked for",passenger_name)
    n -= 1
    i += 1
else:
    print("All seats are booked.")