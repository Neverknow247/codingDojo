x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]


def tenToFifteen():
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j] == 10:
                x[i][j] = 15
    return x


print(tenToFifteen())


def change():
    for i in range (len(students)):
        if students[i]["last_name"] == "Jordan":
            students[i]["last_name"] = "Bryant"
    return students

print(change())


def change3():
    for i in range (len(students)):
        for _key, _value in students[i].items():
            if _value == "Jordan":
                _value = "Bryant"
    return students

print(change3())

def change2():
    for _key, value in sports_directory.items():
        for i in range(len(value)):
            if value[i] == "Messi":
                value[i] = "Andres"
    return sports_directory

print(change2())


def change4():
    for i in range(len(z)):
        if z[i]["y"] == 20:
            z[i]["y"] = 30
    return z

print(change4())


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(_dict):
    for i in range(len(students)):
        names = ""
        for key, value in students[i].items():
            names += f"{key} - {value}"
            if names == f"{key} - {value}":
                names += ", "
        print(names)


iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        for key, value in some_list[i].items():
            if key == key_name:
                print(value)


iterateDictionary2("first_name", [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
])


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(len(value), key.upper())
        for i in range(len(value)):
            print(value[i])

printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon