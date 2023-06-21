''' You are building a login system for your new app.
In order to protect the users, you require their password to have 
certain propoerties, they are listed below:
    1. Must be at least 8 characters long
    2. Must have at least 1 uppercase letter
    3. Must have at least 1 lowercase letter
    4. Must have at least 1  numeric digit
    5. Does NOT contain spaces

Write a program that takes in a password as a string,
and returns True if the password satisfies all 5 criterias. If it doesn't,
return False.

If the entered password is "ilovelasagna4", your function
should return False, as the password does not contain an uppercase letter.

Don't forget to check your code by running a few examples, including the one
given above. '''

def validate_password(password):
    ''' PLEASE WRITE BELOW THIS COMMENT '''
    length_FLAG = (length(password) >= 8)
    uppercase_FLAG = False
    lowercase_FLAG = False
    digit_FLAG = False
    no_space_FLAG = (' ' not in password)
    for letter in password:
        if (not uppercase_FLAG):
            uppercase_FLAG = isupper(letter)
        if (not lowercase_FLAG):
            lowercase_FLAG = islower(letter)
        if (not digit_FLAG):
            digit_FLAG = isdigit(letter)
    return (length_FLAG and uppercase_FLAG and lowercase_FLAG and digit_FLAG and no_space_FLAG)


