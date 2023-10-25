def encoder(password):
    a = ""
    for i in range (0,len(password)):
        b = int(password[i])
        b += 3
        b %= 10
        b = str(b)
        a = a+b
    return a

if __name__ == '__main__':
    print(encoder("12345555"))