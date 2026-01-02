role = input(('Enter the role : ')).lower()


activites = {}
activites_set = set()



if role == 'admin' or role == 'user' or role == 'employee':

    for i in range(5):
        activites_to_be_noted = input('Enter the activites: ')
        activites_set.add(activites_to_be_noted)

    activites['activities'] = activites_set
    print(f'''Number of activities you entered : {len(activites_set)}\nHere are  the activities are {activites}''')
else:
    print('You dont have access to enter the activities')

    