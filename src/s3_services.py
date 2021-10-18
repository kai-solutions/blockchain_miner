import boto3
import os
from botocore.exceptions import NoCredentialsError

# Project path
src_path = os.getcwd()
data_dir = os.path.join(src_path, 'data')


ACCESS_KEY = os.environ['AWS_ACCESS_KEY_ID']
SECRET_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

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

