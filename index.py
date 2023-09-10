
import reque 
import base64
import random
import string
pross = True
while (pross):
    reque.printitle()
    print("________________________________________________________________________________ ")
    reque.op()
    try:
        enter = int(input());
        if enter == 1:
            try:
                print()
                print("     ENTER YOUR PASSWORD")
                print()
                passwordS = input()
                reque.codebase64(passwordS)
            except ValueError:
                print("     Enter only valid characters")
        elif enter == 2:
            try:
                print()
                print("     ENTER YOUR PASSWORD")
                print()
                password64 = input()
                reque.code64(password64)
            except ValueError:
                print("     Enter only valid characters")
        elif enter == 3:
            long = 10
            print()
            print("     GENERATION OF YOUR PASSWORDS")
            print("===================================")
            print()
            for a in range(5):
                randomString = ''.join(random.choice(string.ascii_lowercase and
                string.ascii_uppercase) for _b in range(long))
                reque.randomString64(randomString)
            print()
            print("===================================")
        elif enter == 4:
            print('''     
                       
                   Goobye... ;) 
                  ''')
            pross = False;
            break;
        elif enter == 5:
            print(''' 
        I started developing this tool on September 8 at 3 AM and finished it on September 9 at 5 AM, it only
        has 3 hours of work, but really outside of trying to assume a hacker role encrypting or decrypting
        words , only for sport I developed it, I wanted to see if I understood some aspect about the language.
        Its use is at the free will of anyone.
        If I come up with more ideas I will update the tool.
                  
        By Amaro ;)

            ''')
        else:
            print()
            print("     ENTER VALID OPTIONS. ")
            print()
    except ValueError as Error:
        print("Enter only valid characters: ", Error)

