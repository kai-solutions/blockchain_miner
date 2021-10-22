from web3 import Web3

ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

print(web3.isConnected())

print(web3.eth.blockNumber)

account_1 = '0xD8dE02Ea5CbCf0D700BD3548ab39EA4507bbA2CA'
account_2 = '0x1C79282Dc3aaaaf3BA1467d0CB486376EFc1a992'

private_key = '9e905601850849d2ec954d1883ea395f497de38a406f1bc9600067467ce7fc04'

#get the nonce
nonce = web3.eth.getTransactionCount(account_1)
#1 build a transaction
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')

}
#sign a transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)
#send the transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
#get transaction hash
print(web3.toHex(tx_hash))
