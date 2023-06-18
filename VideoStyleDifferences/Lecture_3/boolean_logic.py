''' You are hosting a massive party and need to book a banquet that can
hold at least 300 guests. Banquet costs are proportional to their
capacity, so you must pick a banquet wisely.

Write a program that takes a list 'banquet_capacities', and tries to find a
banquet that can host 300 guests, and is as low as possible. If such a 
banquet exists, print its capacaity. If no such banquet exists, print an
appropriate statement.

NOTE THAT WE HANDLE THE USER INPUT FOR YOU, AND YOU CAN WORK ON THE
banquet_capacities LIST DIRECTLY 

If the banquet capacities are: 150, 290, 310, 303, 340, 302
The expected output is: 302

Don't forget to check your code by running a few examples, including the one
given above. '''

''' USER INPUT CODE '''
banquet_capacities = []
user_prompt = 'Please enter banquet capacity, type \'N\' to stop: '
while (True):
    user_input = input(user_prompt)
    if (user_input == 'N'):
        break
    banquet_capacities.append (int (user_input))

''' PLEASE WRITE BELOW THIS COMMENT '''

''' We are testing elemental for loop, boolean logic, if else'''

banquet_exists = False
for capacity in banquet_capacities:
    if (capacity >= 300):
        if (not banquet_exists):
            banquet_exists = True
            best_banquet = capacity
        else:
            best_banquet = min (best_banquet, capacity)

if (banquet_exists):
    print (best_banquet)
else:
    print ('None of the banquets can host 300 guests')
        