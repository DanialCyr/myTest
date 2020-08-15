
password=int(input("Please input your original password："))
key = 7
print("\nOriginal Password：",password)
password = password<<key
print("\nAfter encryption:",password)
password = password>>key
print("\nAfter Decryption:",password)
