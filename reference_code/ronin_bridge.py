import json
import pandas as pd
from eth_account import account
from web3 import Web3

infura_url = 'https://mainnet.infura.io/v3/69765a3368f44f5c8cc3691d2361e496'
web3 = Web3(Web3.HTTPProvider(infura_url))

if web3.isConnected():
    print('The connection with Ethereum network is successfull')
else:
    print('Network connection error')

# Ronin Bridge Smart Contract
address = '0x1A2a1c938CE3eC39b6D47113c7955bAa9DD454F2'
abi = json.loads('[{"inputs":[{"internalType":"address","name":"_proxyTo","type":"address"},{"internalType":"address","name":"_registry","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_oldAdmin","type":"address"},{"indexed":true,"internalType":"address","name":"_newAdmin","type":"address"}],"name":"AdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_oldAdmin","type":"address"}],"name":"AdminRemoved","type":"event"},{"anonymous":false,"inputs":[],"name":"Paused","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_new","type":"address"},{"indexed":true,"internalType":"address","name":"_old","type":"address"}],"name":"ProxyUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"_depositId","type":"uint256"},{"indexed":true,"internalType":"address","name":"_owner","type":"address"},{"indexed":true,"internalType":"address","name":"_tokenAddress","type":"address"},{"indexed":false,"internalType":"address","name":"_sidechainAddress","type":"address"},{"indexed":false,"internalType":"uint32","name":"_standard","type":"uint32"},{"indexed":false,"internalType":"uint256","name":"_tokenNumber","type":"uint256"}],"name":"TokenDeposited","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"_withdrawId","type":"uint256"},{"indexed":true,"internalType":"address","name":"_owner","type":"address"},{"indexed":true,"internalType":"address","name":"_tokenAddress","type":"address"},{"indexed":false,"internalType":"uint256","name":"_tokenNumber","type":"uint256"}],"name":"TokenWithdrew","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpaused","type":"event"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"constant":true,"inputs":[],"name":"admin","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_newAdmin","type":"address"}],"name":"changeAdmin","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"depositCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"deposits","outputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"address","name":"sidechainAddress","type":"address"},{"internalType":"uint32","name":"standard","type":"uint32"},{"internalType":"uint256","name":"tokenNumber","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"implementation","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"proxyType","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[],"name":"registry","outputs":[{"internalType":"contract Registry","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"removeAdmin","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_newProxyTo","type":"address"}],"name":"updateProxyTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_registry","type":"address"}],"name":"updateRegistry","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"withdrawals","outputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"tokenAddress","type":"address"},{"internalType":"uint256","name":"tokenNumber","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]')
contract = web3.eth.contract(address=address, abi = abi)

# Balance
balance = web3.eth.getBalance(address)
print(f'The current balance is {web3.fromWei(balance, "ether")} ether')


#latestBlock
block = web3.eth.getBlock('latest', full_transactions=True)
number = block.number
print(f'Searching block {number}')

list_of_block_transactions = block.transactions

df = pd.DataFrame()
for transaction in list_of_block_transactions:

    print(transaction)

    to_address = transaction['to']
    from_address= transaction['from']

    if to_address == address:
        print(f'To account {to_address}')
        to_match = True
    else:
        to_match = False

    if from_address == address:
        print(f'To account {from_address}')
        from_address = True
    else:
        from_address = False

    if to_match or from_address:
        print(f'Found transaction with HASH: {transaction["hash"]}')




nblocks = 10

filter = web3.eth.filter({
    'fromBlock': number - nblocks,
    'toBlock': number,
    'address': address,
})

