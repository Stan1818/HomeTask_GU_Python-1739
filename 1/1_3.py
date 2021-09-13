procent = 0
while procent != '100':
    procent = int(procent) + 1
    slovo = 'процент'
    procent = str(procent)

    if procent == '11' or procent == '12' or procent == '13' or procent == '14' or procent == '15' or procent == '16' or \
            procent == '17' or procent == '18' or procent == '19':
        slovo = slovo + 'ов'
        print(procent, slovo)
    elif procent[-1] == '0' or procent[-1] == '5' or procent[-1] == '6' or procent[-1] == '7' or procent[-1] == '8' or \
            procent[-1] == '9':
        slovo = slovo + 'ов'
        print(procent, slovo)
    elif procent[-1] == '1':
        print(procent, slovo)
    elif procent[-1] == '2' or procent[-1] == '3' or procent[-1] == '4':
        slovo = slovo + 'а'
        print(procent, slovo)
