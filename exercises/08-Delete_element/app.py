people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    for i in people:
        if i == person_name:
            people.remove(i)
            return people
        else:
            return people

    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))