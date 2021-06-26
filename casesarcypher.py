# Caesar Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

message = 'BRX IRXQG D FRGH? EXW LW ORRNV OLNH VRPHWKLQJV PLVVLQJ ILQG SLHFHV DQG EULQJ LW WR PH: A122PAFTSKWPQ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
    print('Key #%s: %s' % (key, translated))