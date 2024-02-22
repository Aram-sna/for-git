print("my first python program for git")
while True:
    print("select your options:? \n\t1)Encrupt\n\t2)Decrypt\n\t3)Exit")
    Choice = input("your Choice: ")
    if Choice == "1":
        plain_text = input("text: ")
        encrypted_text = ""
        for c in plain_text:
            x = ord(c) * 2 + 5
            encrypted_text += chr(x)
        print("encrypted_text: ", encrypted_text)
        print("*" * 40 + "\n")

    elif Choice == "2":
        encrypted_text = input("encrypted text: ")
        plain_text = ""
        for c in encrypted_text:
            x = (ord(c) - 5) // 2
            plain_text += chr(x)
        print("plain text: ", plain_text)
        print("*" * 40 + "\n")

    elif Choice == "3":
        print("goodbye")
        print("*" * 40 + "\n")
        break
    else:
        print("your choice is wrong:! ")
        print("*" * 40 + "\n")
    
    print("enjoy")