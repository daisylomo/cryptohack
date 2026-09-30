# pwntools library has a convenient xor() function that can XOR together data of different types and lengths

word = 'label'

for i in word:
    num = ord(i)
    result = num ^ 13
    char = chr(result)
    print(char)
