''' You are hosting a massive party and need to book a banquet hall that can
hold at least 300 guests.

Write a program that takes a list of banquet hall capacities, called 'capacities',
and prints the size of the smallest banquet hall that can host 300 guests.

You may assume that no banquet hall capcity is larger than 1000, and that
a valid banquet hall exists in the list.

NOTE: WE HAVE PROVIDED AN INITIALIZATION OF THE LIST AS FOLLOWS
    capacities = [1000, 500, 400, 200, 100]
The expected result is based on these capacities is 400.

Don't forget to check your code by running a few examples, including the one
given above. '''

capacities = [1000, 500, 400, 200, 100] # Feel free to add elements for testing

''' PLEASE WRITE BELOW THIS COMMENT '''
best_banquet_capacity = 1000
for capacity in capacities:
    if (capacity >= 300):
        if (capacity < best_banquet_capacity):
            best_banquet_capacity = capacity
output_string = 'The smallest banquet that can host 300 guests has capacity: ' + str(best_banquet_capacity)
print (output_string)