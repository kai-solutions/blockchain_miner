import pandas as pd
import os, time
from web3 import Web3
from datetime import datetime



class Web3Connection:
    projectid: str
    provider: str
    web3: Web3

    def __init__(self, provider,projectid):

        self.projectid = projectid
        self.provider = provider
        


class InfuraConnection(Web3Connection):

    def __init__(self):
        projectid = self.projectid
        provider = self.provider

        

#connection = #InfuraConnection('https://mainnet.infura.io/v3/', '69765a3368f44f5c8cc3691d2361e496')

connection = InfuraConnection('1','1')
print(connection.projectid)




""" 
class EtherBlockMiner():

    def __init__(self,projectID):

        self.NAME = 'eth'
        self.S3_BUCKET = 'blockchainsp'
        self.projectId = projectID
        self.web3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{projectID}'))
        if self.web3.isConnected():
            print('The connection with Ethereum network is successfull')

    def get_latestBlock(self):
        self.block = self.web3.eth.getBlock('latest', full_transactions=True)
        self.currentblock = self.block.number
        print(f'Current block is {self.currentblock}')

    
    def transform(self, df):
        df.columns = df.columns.str.strip().str.replace(' ', '_').str.upper().str.replace('(','',regex=True)
        objs = df.select_dtypes(['object'])
        for i in objs.columns:
            try:
                df[i] = i.apply(lambda x: x.str.strip())
            except:
                pass
        
        return df

    
    def process_block_metadata(self):
        self.blocktype = 'blockmetadata'
        self.blockname = f'{self.NAME}_{self.blocktype}_{self.block.number}_{self.block.timestamp}'
        print(f'Processing block {self.blockname}')
        block_dict = {
            'number': [self.block.number],
            'timestamp': [self.block.timestamp],
            'difficulty': [self.block.difficulty],
            'baseFeePerGas': [self.block.baseFeePerGas],
            'gasLimit':[self.block.gasLimit],
            'gasUsed': [self.block.gasUsed],
            'hash': [self.web3.toHex(self.block.hash)],
            'miner': [self.block.miner],
            'size': [self.block.size],
            'nonce': [self.web3.toHex(self.block.nonce)]
            }
        # Create dataframe objects
        self.df = pd.DataFrame.from_dict(block_dict)
        # Clean object
        self.transform(self.df)


    def process_block_transactions(self):
        print(f'Processing block {self.currentblock} transactions')
        # Create dataframe objects
        self.trx_data = pd.DataFrame.from_dict(self.block.transactions)
        # Clean trx data fields
        self.trx_data.r = self.trx_data.r.apply(lambda x: self.web3.toHex(x))
        self.trx_data.s = self.trx_data.s.apply(lambda x: self.web3.toHex(x))
        self.trx_data.hash = self.trx_data.hash.apply(lambda x: self.web3.toHex(x))
        self.trx_data.blockHash = self.trx_data.blockHash.apply(lambda x: self.web3.toHex(x))

        self.transform(self.trx_data)


    def export_block(self, *args):

        YEAR = str(datetime.fromtimestamp(self.block.timestamp).year)
        MONTH = str(datetime.fromtimestamp(self.block.timestamp).month)
        DAY = str(datetime.fromtimestamp(self.block.timestamp).day)

        filepath = os.path.join('data',self.NAME, self.blocktype, YEAR, MONTH, DAY)
        create_path(filepath, delete_first=False)

        if 'csv' in args:
            self.df.to_csv(os.path.join(filepath, f'{self.blockname}.csv'), index=False, sep = ',', encoding='utf-8')
        if 'json' in args:
            self.df.to_json(os.path.join(filepath, f'{self.blockname}.json'), orient='records', default_handler=str)
        if 's3' in args and 'csv' in args:
            s3_services.upload(os.path.join(filepath,f'{self.blockname}.csv'), self.S3_BUCKET, os.path.join(filepath,f'{self.blockname}.csv'))
        if 's3' in args and 'json' in args:
            s3_services.upload(os.path.join(filepath,f'{self.blockname}.csv'), self.S3_BUCKET, os.path.join(filepath,f'{self.blockname}.json'))

 """