class Nfe:
    numberSerie = ''
    numberNF = ''
    numberCH = ''
    digitCH = ''

    def __init__(self, uf: str, year: str, month: str, cnpj: str, mod: str):
        self.uf = uf
        self.year = year
        self.month = month
        self.cnpj = cnpj
        self.mod = mod

    def getCompleteNfe(self):
        return self.uf + self.year + self.month + self.cnpj + self.mod + self.numberSerie + self.numberNF + self.numberCH + self.digitCH


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

    # numberSerie
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


def getCertificate(uf: str, year: str, month: str, cnpj: str, mod: str):
    cnpjFormat = str(int(cnpj.replace('.', '').replace('/', '').replace('-', '')))

    numberNfe = Nfe(uf, year, month, cnpjFormat, mod)

    getNumberSerie(numberNfe)

    print('end')

    return numberNfe


def getNumberSerie(numberNfe: Nfe):
    for i in range(0, 999):
        numberNfe.numberSerie = '%003d' % i
        print('%003d' % i)
        getNumberNF(numberNfe)


def getNumberNF(numberNfe: Nfe):
    for i in range(0, 999999999):
        numberNfe.numberNF = '%000000009d' % i
        print('%000000009d' % i)
        getNumberCH(numberNfe)


def getNumberCH(numberNfe: Nfe):
    for i in range(0, 999999999):
        numberNfe.numberCH = '%000000009d' % i
        print('%000000009d' % i)
        getDigitCH(numberNfe)


def getDigitCH(numberNfe: Nfe):
    for i in range(0, 9):
        numberNfe.digitCH = str(i)
        print(i)
        getClientSoap(numberNfe)


def getClientSoap(numberNfe: Nfe):
    # uf + year + month + cnpjFormat + mod + numberSerie + numberNF + numberCH + digitCH
    print(numberNfe.getCompleteNfe())