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
        password[i] -= 3
        password[i] = str(password[i])
    password = ''.join(password)
    return password
        

if __name__ == '__main__':
    print(encoder("12345555"))
    print(decoder(encoder('12345555')
