# I am Prerak Patel and my number is 000736376, I have designed this
# program by myself and I have not shared this anyone. My professor's name is
# TIfanfull_length,Antopoloski

Code_of_Course = "DONE"
total_hours = 0
quotient = 0
count = 0
import math
while Code_of_Course != "done" : 
    Code_of_Course = input("Please enter the Course Code (or done if finshed): ")
    Code_of_Course = Code_of_Course.lower()
    count += 1
    if (Code_of_Course == "done" and count == 1):
        break
    
    elif Code_of_Course != "done":
        hours = float(input("How many credit hours was " + str(Code_of_Course) + "?"))
        grade = float(input("What grade did you earn in " + str(Code_of_Course) + "?"))    
        total_hours = total_hours + hours
        quotient = quotient + (grade*hours)
        Course_Average = quotient/total_hours
        second_year = float((total_hours/88)*100)
        third_year = float((total_hours/130)*100)
        print("Course:" , Code_of_Course ,"Weight:" , hours , "hours Grade:" , grade ) 

second = (math.ceil(second_year*100)/100)
third = (math.ceil(third_year*100)/100)
Average = (math.ceil(Course_Average*100)/100)

if count == 1:
    print("You have not entered any data yet")
else:
    print("You have earned the cummulative average of " , Average , "and have \
completed " , second , "of the 2 year program and " , third , " of the 3 year program")
