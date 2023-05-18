import cryptosystem
#MAIN PROGRAM TO RUN
#Python Group members: Joseph I, Bryce E, Mark C, Mohammed A

#Note: Program must start with the database.txt file encrypted already, 2 copies of file are provided.
def register(decrypted):
    
    username = input('Create username:')
    password = input('Create your password:')
    verify = input('Confirm your password:')
    print('Please enter encryption key sent to you...')
    cipherObjects = cryptosystem.keyVerification()

    if(decrypted == False): #######check for decryption
        cryptosystem.decryption(cipherObjects[1]) 

    database = open('database.txt', 'r') ##### read bytes
    d = []
    f = []
    for i in database:
        a,b = i.split(', ')
        b = b.strip()
        d.append(a)
        f.append(b)
        
    data = dict(zip(d, f))
    
    if password != verify:
        print('Passwords do not match, try again')
        cryptosystem.encryption(cipherObjects[0])
        register(False)
    else:
        if len(username)<6:
            print('username is not at least 6 characters')
            print('Please try again')
            cryptosystem.encryption(cipherObjects[0])
            register(False)
        elif len(password)<6:
            print('Password is not at least 6 characters')
            print('Please try again')
            cryptosystem.encryption(cipherObjects[0])
            register(False)
        elif username in d:
            print('Username already exists in database')
            cryptosystem.encryption(cipherObjects[0])
            register(False)
        else:
            database = open('database.txt', 'a')
            database.write(username+', '+password+'\n')
            print('User was successfully created')
            database.close() #close after done with file 
            cryptosystem.encryption(cipherObjects[0]) ## enxrypt database
            return username, password
                    
            
            

def authentication():
    print('Before Logging in, please provide encryption key provided to you...')
    cipherObjects = cryptosystem.keyVerification()
    cryptosystem.decryption(cipherObjects[1])

    database = open('database.txt', 'r')
    username = input('Enter your username:')
    password = input('Enter your password:')
    if not len(username and password)<1:
        d = []
        f = []
        for i in database:
            a,b = i.split(', ')
            b = b.strip()
            d.append(a)
            f.append(b)
            credentialCheck = dict(zip(d, f))
        try:
            if credentialCheck[username]:
                try:
                    if password == credentialCheck[username]:
                        print('Login was successful, Hello ' +username)
                        logout()
                        
                    else:
                        print('The username or password was not correct, goodbye.')
                        cryptosystem.encryption(cipherObjects[0]) 
                except:
                    print('Incorrect password or username')
                    cryptosystem.encryption(cipherObjects[0]) 
            else:
                print('Username or password does not exist in the database, goodbye.')
                cryptosystem.encryption(cipherObjects[0]) 
        except:
            print('Username or Password does not exsit in the database, goodbye.')
            cryptosystem.encryption(cipherObjects[0]) 
    else:
        print('Please enter a valid value')
        cryptosystem.encryption(cipherObjects[0])
        authentication()
    database.close() #close after done with file
    

def logout():
    option = input("Enter 0 to logout of your account")
    if option == '0':
        cipherObjects = cryptosystem.keyVerification()
        cryptosystem.encryption(cipherObjects[0]) 
        main()
    else:
        print("Please enter a valid option")
        logout()

def main(menu=None):
    

    menu = input('Press 1 to Login, Press 2 to Register:'+'\n')
    if menu == '1':
        authentication()
    elif menu == '2':
        register(False)
        main()
    else:
        print("Please enter a valid option")
        main()

def isascii(s):
    """Check if the characters in string s are in ASCII, U+0-U+7F."""
    return len(s) == len(s.encode())

main()