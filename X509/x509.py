from cryptography import x509
import datetime


def checkVality(cert):
    today = datetime.datetime.now()

    if cert.not_valid_before <= today <= cert.not_valid_after:
        return True
    else:
        return False
        
dic = {}

with open("certificateServer.pem", 'rb') as file:
    data = file.read().rstrip()

certServer = x509.load_pem_x509_certificate(data)

with open("certificateIntermediario1.pem", 'rb') as file:
    data = file.read().rstrip()

certIntermediario1 = x509.load_pem_x509_certificate(data)   

print(checkVality(certIntermediario1))

#for cert in dic:
#    print("Certificado - " , dic[cert])
#    fromdate = dic[cert].not_valid_before
#    print(fromdate)
#    todate = dic[cert].not_valid_after
#    print(todate)
