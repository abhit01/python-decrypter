import hashlib


print(''' ____ ___  ____/ / ____/  ____/ /__  _________  ____/ /__  _____
  / __ `__ \/ __  /___ \   / __  / _ \/ ___/ __ \/ __  / _ \/ ___/
 / / / / / / /_/ /___/ /  / /_/ /  __/ /__/ /_/ / /_/ /  __/ /    
/_/ /_/ /_/\__,_/_____/   \__,_/\___/\___/\____/\__,_/\___/_/     
                                                               ''')
flag = 0

pass_hash = input("Enter md5 hash: ")

worldlist = input("File name: ")

try:
    pass_file = open (worldlist, "r")
except:
    print("No file found")
    quit()

for word in pass_file:

    enc_word = word.encode('utf-8')
    digest = hashlib.md5(enc_word.strip()).hexdigest()


    if digest == pass_hash:
        print("password found") 
        print("password is " + word)
        flag = 1
        break

if flag == 0:
    print("password is not in the list")
    