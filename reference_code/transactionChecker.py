from web3 import Web3
from datetime import datetime

infura_url = 'https://mainnet.infura.io/v3/69765a3368f44f5c8cc3691d2361e496'
web3 = Web3(Web3.HTTPProvider(infura_url))

account = '0x8Cf170b22402E7E066eEA53B2A73241814BB4625'

#latestBlock
block = web3.eth.getBlock('latest')
number = block.number
print(f'Searching block {number}')
#latest-n-Blocks
for i in range(0,10):
    print(web3.eth.getBlock(number - i))


flag = False
if flag:
    for txHash in block.transactions:
        tx = web3.eth.getTransaction(txHash)
        if account == tx.to:
            print('Transaction from address book found on blockchain')
            txinfo = {

                'value': web3.utils.fromWei(tx.value, 'ether')
                ,'timestamp': datetime.now()
            }

hash = '0x40fc0466a165da205972def37b373c2f3823a16dfc2bf7cc09adf73925d94d83'

print(web3.eth.getTransactionByBlock(hash, 0))