my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]


#Your code go from here:

def biggest_integer(listing):
    max_value = 0
    for x in my_list:
        if x > max_value:
            max_value = x
    return max_value

print(biggest_integer(my_list))