
register_data = []

user_login = input("Enter your LOGIN: ")
user_password = input("Enter your PASSWORD: ")

register_data.append(user_login)
register_data.append(user_password)

print(register_data)

if len(user_login) < 5:
    print('Error')
elif len(user_password) > 10:
    print('Error')
else:
    print('Welcome, ', user_login, '!')
