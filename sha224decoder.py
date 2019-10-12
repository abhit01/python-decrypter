import hashlib


print('''       __         ___  ___  __ __         __                    __         
   _____/ /_  ____ |__ \|__ \/ // /    ____/ /__  _________  ____/ /__  _____
  / ___/ __ \/ __ `/_/ /__/ / // /_   / __  / _ \/ ___/ __ \/ __  / _ \/ ___/
 (__  ) / / / /_/ / __// __/__  __/  / /_/ /  __/ /__/ /_/ / /_/ /  __/ /    
/____/_/ /_/\__,_/____/____/ /_/     \__,_/\___/\___/\____/\__,_/\___/_/     ''')
flag = 0

pass_hash = input("Enter sha224 hash: ")

worldlist = input("File name: ")

try:
    pass_file = open (worldlist, "r")
except:
    print("No file found")
    quit()

for word in pass_file:

    enc_word = word.encode('utf-8')
    digest = hashlib.sha224(enc_word.strip()).hexdigest()


    if digest == pass_hash:
        print("password found") 
        print("password is " + word)
        flag = 1
        break

if flag == 0:
    print("password is not in the list")
    