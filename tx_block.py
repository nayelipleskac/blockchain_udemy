#TxBlock

from blockchain import CBlock
from digital_sig import generate_keys, sign, verify
import pickle
from transaction import Tx

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

    print(Tx1.is_valid())

    message = b"Some text"
    sig = sign(message, pr1)

    saveFile = open('save.dat', 'wb')
    #Tx1 is being pickles, saveFile is the endpoint
    pickle.dump(Tx1, saveFile)
    saveFile.close()

    loadFile = open('save.dat', 'rb')
    nexTx = pickle.load(loadFile)

    print(nexTx.is_valid())
