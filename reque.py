
import base64
import random
s = 1;
def printitle():
    print('''   
      

            *******             *****            ********     **********
            ********           *******          **********    **********
            ***    ***        ***   ***         ****          **
            *********        ***     ***         ****         **********
            ********        *************         ****        **********
            ***    ***     ***************          ****      **
            *********     ***           ***    **********     **********
            ******       ***             ***    ********      **********


                                                     
                                  ****             *
                                **    **        **  **
                                **             **   **
                                ******        **    **  
                                **    **     *********
                                **    **            **  
                                  ****              **
                                    
                                ENCRYPTOR AND DEENCRYPTOR
                                           ;)
      
          ''')
    
def op():
    print('''
    
    1) Enter password to encode it to base64
    2) Decode a password to single words
    3) Generate a password random in base64
    4) Exit
    
          


    5) Read about it.. 
    
    ''')

# string a base64
def codebase64(passwordS):
    prossCodeBase64 = True;
    while prossCodeBase64:
        try:
            pass64 = base64.b64encode(passwordS.encode()).decode()
            print()
            print("     P A S S W O R D S ENCODE: ")
            print("===================================")
            print()
            print("     " + pass64)
            print()
            print("===================================")
            prossCodeBase64 = False;
            break;
        except ValueError as Error:
            print('ERROR, ONLY CHARACTERS VALID: ' , Error)

# de base64 a string
def code64(password64):
    prossCode64 = True;
    while prossCode64:
        try:
            string_deco = base64.b64decode(password64).decode('utf-8')
            print()
            print("     P A S S W O R D  DECODE: ")
            print("===================================")
            print();
            print("     " + string_deco)
            print();
            print("===================================")
            prossCode64 = False;
            break;
        except ValueError as Error:
            print("ERROR: " , Error)

#CREATE RANDOM PASS 
def randomString64(randomString):
    global s 
    passRandom64 = base64.b64encode(randomString.encode()).decode()
    print(s ,"--->"," ", passRandom64)
    s += 1

    


