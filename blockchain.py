#Blockchain

#block is the transfer of money or data
#the hash is the code for that block
#each block uses the previous block, so tampering 
#is detected when the "chain" is disrupted or a break in the chain is visible.
from cryptography.hazmat.primitives import hashes
digest = hashes.Hash(hashes.SHA256())
digest.update(b"abc") 
digest.update(b"123")
hash = digest.finalize()
# print(hash)

class someClass:
    string = None
    num = 23987
    def __init__(self, mystring):
        self.string = mystring
    def __repr__(self):
        return self.string + '^^^' + str(self.num)

class CBlock:
    data = None
    previousHash = None
    previousBlock = None
    def __init__(self, data, previousBlock):
        self.data = data
        self.previousBlock = previousBlock
        if previousBlock != None:
            self.previousHash = previousBlock.computeHash()
    def computeHash(self):
        digest = hashes.Hash(hashes.SHA256())
        digest.update(bytes(str(self.data), 'utf8')) 
        digest.update(bytes(str(self.previousHash), 'utf8'))
        return digest.finalize()
    def is_valid(self):
        if self.previousBlock == None:
            return True
        return self.previousBlock.computeHash() == self.previousHash
    
if __name__ == '__main__':
    root = CBlock('I am root', None)
    B1 = CBlock(b'I am a child', root)
    B2 = CBlock('I am a B1\'s brother', root)
    B3 = CBlock(12354, B1)
    B4 = CBlock(someClass('Hi there!'), B3)
    B5 = CBlock("top block", B4)

    for b in [B1, B2, B3, B4]:
        if b.previousBlock.computeHash() == b.previousHash:
            print('success, hash is good')
        else:
            print('error, hash is no good!')

    B3.data = 12345
    # print(B4.previousBlock.data)
    if B4.previousBlock.computeHash() == B4.previousHash:
        print('error, couldn\'t detect tampering')
    else:
        print('success, tampering detected')
    print(B4.data)
    B4.data.num = 99999
    print(B4.data)
    if B5.previousBlock.computeHash() == B5.previousHash:
        print('error, couldn\'t detect tampering')
    else:
        print('success, tampering detected')

