#TxBlock

from blockchain import CBlock
from digital_sig import generate_keys, sign, verify
import pickle
from transaction import Tx
from cryptography.hazmat.primitives import serialization


class TxBlock(CBlock):
    def __init__(self, previousBlock):
        pass
    def addTx(self, Tx_in):
        pass
    def is_valid(self):
        return False

if __name__ == "__main__":
    pr1, pu1 = generate_keys()
    pr2, pu2 = generate_keys()
    pr3, pu3 = generate_keys()

    Tx1 = Tx()
    Tx1.add_input(pu1, 1)
    Tx1.add_output(pu2, 1)
    Tx1.sign(pr1)

    if Tx.is_valid: 
        print('Success, Tx is valid!')
    
    #Tx1 is being pickled, saveFile is the endpoint
    saveFile = open('tx.dat', 'wb')
    pickle.dump(Tx1, saveFile)
    saveFile.close()

    
    loadFile = open('tx.dat', 'rb')
    newTx = pickle.load(loadFile)
    if newTx.is_valid():
        print('Success, loaded Tx is valid')    
    loadFile.close()

    root = TxBlock(None)
    root.addTx(Tx1)

    Tx2 = Tx()
    Tx2.add_input(pu2, 1.1)
    Tx2.add_output(pu3, 1)
    Tx2.sign(pr2)
    root.addTx(Tx2)

    B1 = TxBlock(root)
    Tx3 = Tx()
    Tx3.add_input(pu3, 1.1)
    Tx3.add_output(pu1, 1)
    Tx3.sign(pr3)
    B1.addTx(Tx2)

    Tx4 = Tx()
    Tx4.add_input(pu1, 1)
    Tx4.add_output(pu2, 1)
    Tx4.add_reqd(pu3)
    Tx4.sign(pr1)
    Tx4.sign(pr3)
    B1.addTx(Tx4)

    

    savefile = open('block.dat', 'wb')
    pickle.dump(B1)
    savefile.close()

    loadFile = open('block.dat', 'wb')
    load_B1 = pickle.load(loadFile)

    load_B1.is_valid()
    for b in [root, B1, load_B1, load_B1.previousBlock]:
        if b.is_valid():
            print('Success, valid block')
        else:
            print('error, Bad block!')