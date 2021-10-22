import os
import snowflake.connector
import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv

load_dotenv('/home/kraftman/Documents/Projects/Blockchain_Analytics/.env')

# Project path
src_path = os.getcwd()
data_dir = os.path.join(src_path, 'data')


ACCESS_KEY = os.environ['AWS_ACCESS_KEY_ID']
SECRET_KEY = os.environ['AWS_SECRET_ACCESS_KEY']


# Gets the version
def get_version():
    ctx = snowflake.connector.connect(
        user=os.environ['USER'],
        password=os.environ['SNOWFLAKE_PASS'],
        account='KB33487.us-east-2.aws'
        )
    cs = ctx.cursor()
    try:
        cs.execute("SELECT current_version()")
        one_row = cs.fetchone()
        print(one_row[0])
    finally:
        cs.close()
    ctx.close()

def upload(local_file, bucket, s3_file):

    s3 = boto3.client('s3', aws_access_key_id= ACCESS_KEY, aws_secret_access_key = SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print('Upload successfull')
        return True
    except FileNotFoundError:
        print('The file was not found')
        return False
    except NoCredentialsError:
        print('Credentials not available')
        return False

