import os

print('''

|\     /||\     /|(  __  \\__   __/
| )   ( || )   ( || (  \  )  ) (   
| (___) || |   | || |   ) |  | |   
|  ___  |( (   ) )| |   | |  | |   
| (   ) | \ \_/ / | |   ) |  | |   
| )   ( |  \   /  | (__/  )  | |   
|/     \|   \_/   (______/   )_(   ''')


print('''
Choose the encryption you want to decrypt
1.md5
2.sha1
3.sha512
4.sha384
5.sha224
6.sha256 \n''')

option_number = int(input("Enter the option number : "))

if option_number == 1:
    os.system("python md5decoder.py")
elif option_number == 2:
    os.system("pythonsha1decoder.py")
elif option_number == 3:
    os.system("python sha512decoder.py")
elif option_number == 4:
    os.system("python sha384decoder.py")
elif option_number == 5:
    os.system("python sha224decoder.py")
elif option_number == 6:
    os.system("python sha256decoder.py")            
else:
    print("You entered wrong option number")        
    quit()


