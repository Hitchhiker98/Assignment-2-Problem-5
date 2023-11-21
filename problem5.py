# function to check if a number is divisible by 11
def is_divisible_by_11(number):
# check if the input is a valid number
    if not str(number).isdigit():
        return False

# convert the number to a string to iterate through its digits
    number_str = str(number)
    alternating_sum = 0

# calculate the alternating sum of digits
    for i, digit_str in enumerate(number_str):
        digit = int(digit_str)
        if i % 2 == 0:
            alternating_sum += digit
        else:
            alternating_sum -= digit

# check if the alternating sum is divisible by 11
    if alternating_sum % 11 == 0:
        return True
    else:
        return False

# prompt the user for input
user_input = input("Enter a number: ")

# check if the input is a valid number and if it's divisible by 11
if is_divisible_by_11(user_input):
    print("This is divisible by 11.")
else:
    print("This is not divisible by 11.")