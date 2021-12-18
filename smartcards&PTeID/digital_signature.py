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
            
    private_key = session.findObjects([
                    (PyKCS11.CKA_CLASS, PyKCS11.CKO_PRIVATE_KEY), 
                    (PyKCS11.CKA_LABEL, 'CITIZEN AUTHENTICATION KEY')
                    ])[0]

    mechanism = PyKCS11.Mechanism(PyKCS11.CKM_SHA1_RSA_PKCS, None)

    text = b'text to sign'
    signature = bytes(session.sign(private_key, text, mechanism))
   
    with open("signature_result", "wb") as writer:
        writer.write(signature)