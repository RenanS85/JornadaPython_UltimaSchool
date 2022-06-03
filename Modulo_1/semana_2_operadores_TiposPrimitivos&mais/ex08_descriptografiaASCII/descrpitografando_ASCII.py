mensagem_criptografada = \
    ['8', '5', '-1', '7', '6', '-1', '8', '4', '-1', '7', '3', '-1', '7', '7', '-1', '6', '5', '-1']

list = []

s=''
for string in mensagem_criptografada:
    if string != '-1':
        s+=string
    else:
        print(chr(int(s)),end='')
        s=''







