

def getKey(uf: str, year: str, month: str, cnpj: str, mod: str):
    print(uf)
    print(year)
    print(month)
    cnpjFormat = str(int(cnpj.replace('.', '').replace('/', '').replace('-', '')))
    print(cnpjFormat)
    print(mod)

    numberSerie = ''
    numberNF = ''
    numberCH = ''
    digitCH = ''

    print('\n Run NF')

    #numberSerie
    for i in range(0, 999):
        if '005' == '%003d' % i:
            numberSerie = '%003d' % i
            break

    # numberNF
    for i in range(0, 999999999):
        if '000290451' == '%000000009d' % i:
            numberNF = '%000000009d' % i
            print('%000000009d' % i)
            break

    # numberCH
    for i in range(0, 999999999):
        if '110290451' == '%000000009d' % i:
            numberCH = '%000000009d' % i
            print('%000000009d' % i)
            break

    # digitCH
    for i in range(0, 9):
        if '5' == str(i):
            digitCH = str(i)
            print(i)
            break

    print('end')

    return uf + year + month + cnpjFormat + mod + numberSerie + numberNF + numberCH + digitCH

