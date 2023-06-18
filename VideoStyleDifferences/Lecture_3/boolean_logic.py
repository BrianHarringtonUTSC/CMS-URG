''' You are hosting a massive party and need to book a banquet hall that can
hold at least 300 guests. Banquet hall costs are proportional to their
capacity, so you must pick a banquet wisely.
Write a program that takes a list 'capacities', and tries to find a
banquet hall that can host 300 guests, and is as low as possible. If such a 
banquet hall exists, print its capacity. If no such banquet hall exists, print an
appropriate statement.
NOTE THAT WE HANDLE THE USER INPUT FOR YOU, AND YOU CAN WORK ON THE
capacities LIST DIRECTLY 
If the banquet hall capacities are: 150, 290, 310, 303, 340, 302
The expected output is: 302
Don't forget to check your code by running a few examples, including the one
given above. '''

''' USER INPUT CODE '''
capacities = []
user_prompt = 'Please enter banquet hall capacity, type \'N\' to stop: '
while (True):
    user_input = input(user_prompt)
    if (user_input == 'N'):
        break
    capacities.append (int (user_input))

''' PLEASE WRITE BELOW THIS COMMENT '''

''' We are testing elemental for loop, boolean logic, if else'''

banquet_exists = False
for capacity in capacities:
    if (capacity >= 300):
        if (not banquet_exists):
            banquet_exists = True
            best_banquet = capacity
        else:
            best_banquet = min (best_banquet, capacity)

if (banquet_exists):
    print (best_banquet)
else:
    print ('None of the banquet halls can host 300 guests')