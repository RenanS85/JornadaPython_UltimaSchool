'''
FRASE CRIPTOGRAFADA: HVWRX HPSROJDGR FRP R FXUVR GH SBWKRQ
'''

alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def descript(phrase_txt):
    s = ''
    for letter in phrase_txt:
        if letter != ' ':
            pos = alp.index(letter)
            l = alp[pos - 3]
            s+=l
        if letter == ' ':
            s+=letter
    print(s)


descript('HVWRX HPSROJDGR FRP R FXUVR GH SBWKRQ')



