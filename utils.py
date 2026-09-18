import boto3
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_session(access_key, secret_key, region):
    return boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )

def list_buckets(session):
    s3 = session.client('s3')
    response = s3.list_buckets()
    return response.get('Buckets', [])

def list_ec2_instances(session):
    ec2 = session.client('ec2')
    response = ec2.describe_instances()
    return response.get('Reservations', [])
