import random
import datetime
import time

print("welcome to student grade calculator")

num_1= float(input("enter your 1st number :"))
num_2= float(input("enter your 2nd number:"))
num_3= float(input("enter your 3rd number:"))
num_4= float(input("enter your 4th number:"))
num_5= float(input("enter your 5th number:"))

percentage = (num_1+num_2+num_3+num_4+num_5)/5

# finding maximum score without using max()
highest = num_1

if num_2 > highest:
    highest = num_2
if num_3 > highest:
    highest = num_3
if num_4 > highest:
    highest = num_4
if num_5 > highest:
    highest = num_5

# finding minimum score without using min()
lowest = num_1

if num_2 < lowest:
    lowest = num_2
if num_3 < lowest:
    lowest = num_3
if num_4 < lowest:
    lowest = num_4
if num_5 < lowest:
    lowest = num_5

print("highest score attained:", highest)
print("lowest score attained:", lowest)

if percentage  <=100 and percentage >=90:
    print("your grade is:","Grade A")
elif percentage  <=90 and percentage>=80:
    print("your grade is:", "Grade B")
elif percentage  <=80 and percentage>=70:
    print("your grade is:", "Grade C")
elif percentage  <=70 and percentage>=60:
    print("your grade is:","Grade D")
elif percentage  <=60 and percentage>=50:
    print("your grade is:","Grade E")
else :
    print("your grade is:","Grade F ", "fail")

messages = ["good job!", "keep it up!", "nice work!", "keep learning!"]
print(random.choice(messages))

date = datetime.datetime.now()
print("date:", date.strftime("%d-%m-%Y"))

time.sleep(1)

print("thank you for using the grade calculator")