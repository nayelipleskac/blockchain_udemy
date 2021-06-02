#Transaction.py

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes

import digital_sig

class Tx:
    inputs = None
    outputs = None
    sigs = None
    reqd = None
    def __init__(self):
        inputs = []
        outputs = []
        sigs = []
        reqd = []
    def add_input(self, from_addr, amount):
        pass
    def add_output(sef, to_addr, amount):
        pass
    def add_req(self, addr, amount):
        pass
    def sign(self, private):
        pass
    def is_valid(self):
        return False

if __name__ == '__main__':
    pr1, pu1 = digital_sig.generate_keys()  
    pr2, pu2 = digital_sig.generate_keys()  
    pr3, pu3 = digital_sig.generate_keys()  
    pr14, pu4 = digital_sig.generate_keys()

    Tx1 = Tx()
    Tx.add_input(pu1, 1)
    Tx1.add_input(pu2, 1)
    Tx1.sign(pr1)
    if Tx1.is_valid():
        print('success Tx is valid')
    else:
        print('error, Tx is invalid') 
    Tx2 = Tx()
    Tx1.add_input(pu1, 2)
    Tx2.add_output(pu2, 1) 
    Tx2.add_output(pu3, 1)
    Tx2.sign(pr1)

    Tx3 = Tx()
    Tx3.add_input(pu3, 1.2)
    Tx3.add_output(pu1, 1.1)
    Tx3.sign(pr3)


    for t in [Tx1, Tx2, Tx3]:

        if Tx1.is_valid():

            print('success Tx is valid')
        else:
            print('error, Tx is invalid') 


    