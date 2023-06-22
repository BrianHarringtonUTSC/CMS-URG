''' You want to make a cGPA calculator to calculate the average GPA over
the 6 required courses in your first year. 

Write a program that takes the GPA for 6 courses from the user, and prints
the average of those GPAs. Don't forget to indicate to the user how they
should input the GPAs by using a prompt when asking for input, as follows:
    input("some prompt for the user")

If the GPAs given by the user are: 4.0, 4.0, 3.0, 3.0, 3.0, 3.1
The expected output is: 3.35

Don't forget to check your code by running a few examples, including the one
given above. '''

''' PLEASE WRITE BELOW THIS COMMENT '''

total_GPA = 0
for i in range (0, 6, 1):
    user_prompt = "Enter course GPA: "
    user_input = input (user_prompt)
    course_GPA = float (user_input)
    total_GPA = total_GPA + course_GPA
cGPA = total_GPA / 6
output_string = "Your cGPA is: " + str (cGPA)
print (output_string)