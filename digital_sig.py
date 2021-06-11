# Signatures

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization



def generate_keys():
    private = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public = private.public_key()
    pu_ser = public.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return private, pu_ser
    #returning the private and the serizalized version of public 
    # when saving the pri, make a password 


def sign(message, private):
    message = bytes(str(message), 'utf-8')
    sig = private.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()), 
            salt_length=padding.PSS.MAX_LENGTH
            ),
        hashes.SHA256()
    )
    return sig


def verify(message, sig, pu_ser):
    public = serialization.load_pem_public_key(
        pu_ser,
    )
    message = bytes(str(message), 'utf-8')
    try: 
        public.verify(
            sig,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False
    except:
        print('Error executing public key verify')
        return False


if __name__ == '__main__':
    pr, pu = generate_keys()
    print(pr)
    print(pu)
    message = b"This is a secret message"
    sig = sign(message, pr)
    print(sig)
    correct = verify(message, sig, pu)
    print('CORRECT: ' ,correct)
    if correct:
        print('SUCCESS! good sig')
    else:
        print('ERROR! sig is bad!')

    pr2, pu2 = generate_keys() 

    sig2 = sign(message, pr2)

    correct = verify(message, sig2, pu)
    if correct:
        print('ERROR! Bad signature checks out!')
    else:
        print('Success! Bad sig detected!')

    badmessage = message + b'Q'
    correct = verify(badmessage, sig, pu)
    if correct:
        print('ERROR! Tampered message checks out!')
    else:
        print('Success! Tampering detected!')

