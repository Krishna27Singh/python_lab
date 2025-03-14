def check_range(num, left_range, right_range):
    if(num>=left_range and num<=right_range):
        return True
    return False

num = int(input("Enter the number"))

left_range = int(input("Enter the left range: "))
right_range = int(input("Enter the right range: "))

if(check_range(num, left_range, right_range)):
    print("The number falls in the given range")
else:
    print("The number does not fall in the given range")
