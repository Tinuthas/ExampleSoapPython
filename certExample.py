from requests import Session
from zeep import Client
from zeep.transports import Transport

session = Session()
#file path
session.verify = 'path/to/my/certificate.pem'
transport = Transport(session=session)
client = Client(
    'http://my.own.sslhost.local/service?WSDL',
    transport=transport)

#verify
client.service