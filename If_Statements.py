
#******* If statements in python************

# If statements are special programming structure which helps us to take decisions.
# Using if statements we can execute certain code when certain  conditions are true and execute other code when other coditions are true.

is_male=True
is_tall=False
if is_male or is_tall:  # 'and' is also used in if statement 
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but a tall person")
else:
    print("You are not a tall male")


# In case of multiple conditions we can use 'elif' statements. It will check the each statement until the condition is satisfied.

.

# and
# or
# not