#TxBlock

from blockchain import CBlock
from digital_sig import generate_keys, sign, verify
import pickle
from transaction import Tx
from cryptography.hazmat.primitives import serialization
reward = 25.0


class TxBlock(CBlock):
    def __init__(self, previousBlock):
        super(TxBlock, self).__init__([], previousBlock)
    def addTx(self, Tx_in):
        self.data.append(Tx_in)
    def __count_totals(self):
        total_in = 0
        total_out = 0
        for tx in self.data:
            for addr, amt in tx.inputs:
                total_in += amt
            for addr, amt in tx.outputs:
                total_out += amt
        return total_in, total_out
    def is_valid(self):
        if not super(TxBlock, self).is_valid():
            return False
        for tx in self.data:
            if not tx.is_valid():
                return False
        total_in, total_out = self.__count_totals()
        if total_out - total_in - reward > 0.0000000001:
            return False 
        return True

if __name__ == "__main__":
    pr1, pu1 = generate_keys()
    pr2, pu2 = generate_keys()
    pr3, pu3 = generate_keys()

    Tx1 = Tx()
    Tx1.add_input(pu1, 1)
    Tx1.add_output(pu2, 1)
    Tx1.sign(pr1)

    if Tx1.is_valid: 
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
    pickle.dump(B1, savefile)
    savefile.close()

    loadFile = open('block.dat', 'rb')
    load_B1 = pickle.load(loadFile)

    # print(bytes(str(load_B1.data), 'utf8'))

    load_B1.is_valid()
    for b in [root, B1, load_B1, load_B1.previousBlock]:
        if b.is_valid():
            print('Success, valid block')
        else:
            print('error, Bad block!')

    B2 = TxBlock(B1)
    Tx5 = Tx()
    Tx5.add_input(pu3, 1)
    Tx5.add_output(pu1, 100)
    Tx5.sign(pr3)
    B2.addTx(Tx5)
    # print(Tx5.is_valid())

    load_B1.previousBlock.addTx(Tx4)
    for b in [B2, load_B1]:
        if b.is_valid():
            print('Error, bad blocks verified!')
        else:
            print('Success, bad blocks detected!')


    #Testing mining reward and tx fees
    pr4, pu4 = generate_keys()

    B3 = TxBlock(B2)
    B3.addTx(Tx2)
    B3.addTx(Tx3)    
    B3.addTx(Tx4)
    Tx6 = Tx()
    Tx6.add_output(pu4, 25)
    B3.addTx(Tx6)
    if B3.is_valid():
        print('Success, block reward succeeds!')
    else:
        print('Error, block reward fail')
    
    B4 = TxBlock(B3)
    B4.addTx(Tx2)
    B4.addTx(Tx3)    
    B4.addTx(Tx4)
    Tx7= Tx()
    Tx7.add_output(pu4, 25.2 )
    B4.addTx(Tx6)
    if B4.is_valid():
        print('Success, tx fees succeeds!')
    else:
        print('Error, tx fees fail')

    #Greedy miner
    B5 = TxBlock(B4)
    B5.addTx(Tx2)
    B5.addTx(Tx3)    
    B5.addTx(Tx4)
    Tx8 = Tx()
    Tx8.add_output(pu4, 26.2)
    B5.addTx(Tx8)
    if not B5.is_valid():
        print('Success, greedy miner detected!')
    else:
        print('Error, greedy miner not detected')

