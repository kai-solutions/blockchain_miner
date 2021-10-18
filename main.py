import json
import os
import pandas as pd
import numpy as np
from eth_account import account
from web3 import Web3
from src import s3_services
from src import sql_manager
from datetime import datetime

infura_url = 'https://mainnet.infura.io/v3/69765a3368f44f5c8cc3691d2361e496'
web3 = Web3(Web3.HTTPProvider(infura_url))

if web3.isConnected():
    print('The connection with Ethereum network is successfull')
else:
    print('Network connection error')

#latestBlock
block = web3.eth.getBlock('latest', full_transactions=True)
print(f'Searching block {block.number}')

#block Metadata
block_dict = {
    'number': [block.number],
    'timestamp': [block.timestamp],
    'difficulty': [block.difficulty],
    'baseFeePerGas': [block.baseFeePerGas],
    'gasLimit':[block.gasLimit],
    'gasUsed': [block.gasUsed],
    'hash': [web3.toHex(block.hash)],
    'miner': [block.miner],
    'size': [block.size],
    'nonce': [web3.toHex(block.nonce)]
}

# DataFrame conversion
block_data = pd.DataFrame(block_dict)

trx_data = pd.DataFrame.from_dict(block.transactions)

# Convert hash into readable hex format
trx_data.r = trx_data.r.apply(lambda x: web3.toHex(x))

trx_data.s = trx_data.s.apply(lambda x: web3.toHex(x))

trx_data.hash = trx_data.hash.apply(lambda x: web3.toHex(x))

trx_data.blockHash = trx_data.blockHash.apply(lambda x: web3.toHex(x))

# Basic cleansing
def transform(df):
    df.columns = df.columns.str.strip().str.replace(' ', '_').str.upper().str.replace('(','')
    objs = df.select_dtypes(['object'])
    df[objs.columns] = objs.apply(lambda x: x.str.strip())
    
    return df

transform(block_data)
transform(trx_data)



# Define filenames
block_data_filename = f'eth_blockmetadata_{block.number}_{block.timestamp}'
trx_data_filename = f'eth_blocktransactions_{block.number}_{block.timestamp}'

# Local Data dumps
trx_data.to_csv(os.path.join('data',f'{trx_data_filename}.csv'), index=False, sep = ',', encoding='utf-8')
trx_data.to_json(os.path.join('data',f'{trx_data_filename}.json'), orient='records', default_handler=str)
block_data.to_csv(os.path.join('data',f'{block_data_filename}.csv'), index=False, sep = ',', encoding='utf-8')
block_data.to_json(os.path.join('data',f'{block_data_filename}.json'), orient='records', default_handler=str)


# S3 Data dumps
S3_BUCKET = 'blockchainsp'
s3_services.upload(os.path.join('data',f'{trx_data_filename}.csv'), S3_BUCKET, f'{trx_data_filename}.csv')
s3_services.upload(os.path.join('data',f'{trx_data_filename}.csv'), S3_BUCKET, f'{trx_data_filename}.json')
s3_services.upload(os.path.join('data',f'{block_data_filename}.csv'), S3_BUCKET, f'{block_data_filename}.csv')
s3_services.upload(os.path.join('data',f'{block_data_filename}.csv'), S3_BUCKET, f'{block_data_filename}.json')