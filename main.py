def encoder(password):
    a = ""
    for i in range (0,len(password)):
        b = int(password[i])
        b += 3
        b %= 10
        b = str(b)
        a = a+b
    return a

def decoder(password):
    password = list(password)
    for i in range(len(password)):
        password[i] = int(password[i])
        password[i] += 7
        password[i] %= 10
        password[i] = str(password[i])
    password = ''.join(password)
    return password
        


def main():
    global password, encoded_password
    quit_program = False
    while not quit_program:
        menu = 'Menu'
        print(menu)
        print('-' * len(menu))
        print('1. Encode\n2. Decode\n3. Quit')
        menu_option = input('Please enter an option: ')
        if menu_option == '1':
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!')
        elif menu_option == '2':
            print(f'The encoded password is {encoded_password}, and the original password is {password}.')
        elif menu_option == '3':
            quit_program = True


if __name__ == '__main__':
    main()