# function that checks if each integer within a list is even or odd
def even_or_odd(integer_list):
    for integer in integer_list:
        if integer % 2 == 0:
            print(f"{integer} even")
        else:
            print(f"{integer} odd")

# create list of integers
integers = [0,1,2,3,4,5,6,7,8,9]

# run function on list of integers
even_or_odd(integers)
