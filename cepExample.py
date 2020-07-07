import zeep

wsdl = 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl'
client = zeep.Client(wsdl=wsdl)

print(client.service._operations)

print(client.service.consultaCEP('06787520'))


#client.service.cancelarPedidoScol('teste', 13,34, 'admin', 'admin')