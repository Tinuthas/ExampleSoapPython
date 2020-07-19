import zeep
from requests import Session



#wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
#wsdl = 'https://homologacao.nfe.fazenda.sp.gov.br/ws/nfeautorizacao4.asmx?wsdl'
#wsdl = 'https://homologacao.nfe.fazenda.sp.gov.br/ws/nfeautorizacao4.asmx'
wsdl = 'https://nfe.fazenda.sp.gov.br/ws/nfeconsultaprotocolo4.asmx?wsdl'

#nota fiscal chave
nfe = '35200643708379010830550050002904511102904515'

session = Session()
session.verify = 'path/to/my/certificate.pem'
transport = zeep.Transport(session=session)


client = zeep.Client(wsdl=wsdl, transport=transport)

print(client.service._operations)
