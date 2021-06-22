#Server.py
from tx_block import TxBlock

TCP_PORT = 5005

def recvObj(ip_addr):
    return None
if __name__ == "__main__":
    newB = recvObj('localhost',  )
    print(newB.data[1])
    print(newB.data[2])
    if (newB.is_valid()):
        print('Success. Tx is valid')
    else:
        print('Error. Tx invalid')
    if newB.data[0].inputs[0][1]  == 2.3:
        print('Success. Input value matches')
    else:
        print('Error. Input value wrong for Block 1, tx')
    if newB.data[0].outputs[1][1]  == 1.1:
        print('Success. output value matches')
    else:
        print('Error. outut value wrong for Block 1, tx')
    if newB.data[1].inputs[0][1]  == 1.1:
        print('Success. Input value matches')
    else:
        print('Error. Input value wrong for Block 1, tx')
    if newB.data[1].inputs[1][1]  == 1.0:
            print('Success. Input value matches')
    else:
        print('Error. Input value wrong for Block 1, tx')
    if newB.data[1].outputs[0][1]  == 3.1:
            print('Success. output value matches')
    else:
        print('Error. output value wrong for Block 1, tx')