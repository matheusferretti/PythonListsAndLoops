chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    new_list = []
    for x in chunk_one:
        new_list.append(x)

    for z in chunk_two:
        new_list.append(z)
    return new_list

print(merge_list(chunk_one, chunk_two))
