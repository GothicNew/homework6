# Работа со словарями:
my_dict = {'Junior': 700, 'Middle': 1500, 'Senior': 3000}
print(my_dict)
print(my_dict['Middle'])
my_dict.update({'Trainee': 250,
                'Team_Lead': 5000})

jun_of = my_dict.pop('Junior')
print(jun_of)
print(my_dict)

# Работа с множествами:
my_set = {5, 'Harry_Potter',4.4, 'Python', 5, 11, 'Python', (1,1,2), 11}
print(my_set)
my_set.update([32, 'Moskow'])
my_set.remove(5)
print(my_set)