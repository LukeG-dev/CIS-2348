#  Luke Gilin

user_password = str(input())
j = 0
for i in user_password:

    if user_password[j] == 'i':
        print('!', end='')
    elif user_password[j] == 'a':
        print('@', end='')
    elif user_password[j] == 'm':
        print('M', end='')
    elif user_password[j] == 'B':
        print('8', end='')
    elif user_password[j] == 'o':
        print('.', end='')
    else:
        print(user_password[j], end='')
    j += 1

print('q*s')
