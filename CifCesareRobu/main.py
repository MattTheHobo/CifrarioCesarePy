"""Fai un menu con:
1) critta
2) decritta
3) esci

Crittare e decrittare con linguaggio cesare"""
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'I', 'M', 'N', 'O', 'P', 'O', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']


def main():
    cont = 0

    while cont != 3:
        print('1 = cripta\n')
        print('2 = decripta\n')
        print('3 = esc\n')
        cont = int(input(">> "))
        if cont == 1:
            critt()
        if cont == 2:
            decritt()


def critt():
    daCif = str(input("Inserisci il messaggio da cifrare: "))
    key = int(input("Inserisci la chiave di cifratura: "))
    testoCritt = ""
    daCif = daCif.upper()

    for charMess in range(len(daCif)):
        index = alpha.index(daCif[charMess])
        for cntK in range(key):
            index = index + 1

            if index is len(alpha):
                index = 0
        carattere = alpha[index]
        testoCritt += carattere

    print('Messaggio crittato: ' + testoCritt)


def decritt():
    daDec = str(input("Inserisci il messaggio da decifrare: "))
    key = int(input("Inserisci la chiave di cifratura: "))
    testoDecritt = ""
    daDec = daDec.upper()

    for charMess in range(len(daDec)):
        index = alpha.index(daDec[charMess])
        for cntK in range(key):
            index = index -1

            if index < 0:
                index = len(alpha) - 1
        carattere = alpha[index]
        testoDecritt += carattere

    print("Messaggio decrittato: " + testoDecritt)


main()

