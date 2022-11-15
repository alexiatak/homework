#ex1.4 CIPHER
def encrypt(text,s):
    result = ""
    for i in range(len(text)):
      char = text[i]   
      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      else:
        result += chr((ord(char) + s - 97) % 26 + 97)
    return result
text = "hey you"
s = 2

print ("Plain Text : " + text)
print ("Shift : " + str(s))
print (encrypt(text,s))
def decrypt(text,s):
    result = ""
    for i in range(len(text)):
      char = text[i]   
      if (char.isupper()):
         result += chr((ord(char) - s-65) % 26 + 65)
      else:
        result += chr((ord(char) - s - 97) % 26 + 97)
    return result
text = "jgapaqw"
s = 2

print ("Encrypted Text : " + text)
print ("Shift : " + str(s))
print (decrypt(text,s))
