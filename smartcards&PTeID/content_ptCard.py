import PyKCS11
import binascii
from cryptography import x509
from cryptography.hazmat.backends import default_backend

def load_certificate(cert_data):
    cert = x509.load_der_x509_certificate(cert_data, default_backend())
    return cert

lib = '/usr/local/lib/libpteidpkcs11.so'
pkcs11 = PyKCS11.PyKCS11Lib()
pkcs11.load(lib)
slots = pkcs11.getSlotList()

for slot in slots:
    #print(pkcs11.getTokenInfo(slot))

    all_attr = list(PyKCS11.CKA.keys())
    #Filter attributes
    all_attr = [e for e in all_attr if isinstance(e, int)]

    session = pkcs11.openSession(slot)
    for obj in session.findObjects():
        # Get object attributes
        attr = session.getAttributeValue(obj, all_attr)
        # Create dictionary with attributes
        attr = dict(zip(map(PyKCS11.CKA.get, all_attr), attr))

        if attr["CKA_CLASS"] != None:
            print('Label: ', attr['CKA_LABEL'])
            cert = load_certificate(bytes(attr["CKA_VALUE"]))
            print("   Issuer: ",cert.issuer.rfc4514_string())
            print("   Subject: ",cert.subject.rfc4514_string(),"\n")