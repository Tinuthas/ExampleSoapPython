from cUF import UF
from mod import MOD
from tpEmis import TPEmis
from runNF import getKey

# cnpj fashshop 43708379010830
# mod 55 nota fiscal eletronica
# serie 005
# numero nota fiscal 000290451
# codigoNumericoChave 110290451
# digito Verificador 5

#3520 0643 7083 7901 0830 5500 5000 2904 5111 0290 4515
#35200643708379010830550050002904511102904515
for uf in UF:
    print(uf.value, uf.name)

for mod in MOD:
    print(mod.value, mod.name)

for tp in TPEmis:
    print(tp.value, tp.name)



print(int('43708379010830'))
x = '%000000009d' % 5
print(x)

nfe = getKey(str(UF.SP.value), '20', '06', '43.708.379/0108-30', '55')

print('\nNFE: ' + nfe)




