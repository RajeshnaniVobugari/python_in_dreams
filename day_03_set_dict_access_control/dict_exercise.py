number_of_keys_to_be_initiated = int(input('Enter the number :'))

dict_keys = {i:None for i in range(1,number_of_keys_to_be_initiated+1)}

print(dict_keys)

for i in dict_keys:
    while True:
        user_roles = input('Enter the roles : ')
        if user_roles not in dict_keys.values() and user_roles!= "":
            dict_keys[i] = user_roles
            
            break
        else:
            print(f'The role {user_roles} is already exist please try to re enter new key')
            

access_the_role = input('Enter the role to add the activity in the list: ')


