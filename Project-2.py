
userinput = input("Enter the Text: ")
shift = 3

encrypted = ""

for ch in userinput:

    if ch.isalpha():
        if ch.isupper():
            encrypted = encrypted+ chr((ord(ch)-65+shift)%26+65)
        
        else:
            encrypted = encrypted + chr((ord(ch)-97+shift)%26+97)
    
    else:
        encrypted = encrypted+ch


decrypted = ""

for ch in userinput:

    if ch.isalpha():
        if ch.isupper():
            decrypted = decrypted + chr((ord(ch)-65-shift)%26+65)

        else:
            decrypted = decrypted + chr((ord(ch)-97-shift)%26+97)
    
    else:
        decrypted = decrypted + ch

print(userinput , "<--Original Text")
print(userinput , "<--Decrypted Text")
print(encrypted , "<--Encrypted Text")