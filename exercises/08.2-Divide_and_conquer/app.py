list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


#Your code here:
def merge_two_list(listing):
    odd_array = []
    even_array = []
    both_arrays = []
    for x in listing:
        if x % 2 == 0:
            even_array.append(x)
        else:
            odd_array.append(x)
    both_arrays.append(odd_array)
    both_arrays.append(even_array)
    return both_arrays


print(merge_two_list(list_of_numbers))

