def_password = '1a2b3c'
def_username = 'Can'
while True:
    username = input('User Name:')
    password = input('Password:')
    if username == def_username and password == def_password:
        print('Welcome')
        break
    else:
        continue