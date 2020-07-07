import zeep

wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
client = zeep.Client(wsdl=wsdl)
print(client.service._operations)
print(client.service.Method1('Zeep', 'is cool'))