#Signatures

from cryptography.hazmat.primitives.asymmetric import rsa

def generate_keys():
    private = rsa.generate_private(public_exponent=65537, key_size=2048)
    public = 'bb'
    return private, public
    
    

def sign(message, private):
    sig= 'asgdlkj&&'
    return sig

def verify(message, sig, public):
    return False

if __name__ == '__main__':
    pr, pu = generate_keys()
    message = b="This is a secret message"
    sig = sign(message, pr)
    correct = verify(message, sig, pu)

    if correct:
        print('SUCCESS! good sig')
    else:
        print('ERROR! sig is bad!')