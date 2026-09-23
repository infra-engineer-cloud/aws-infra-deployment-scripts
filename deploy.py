import boto3
import logging
from utils import list_buckets, list_ec2_instances

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# AWS Configuration
# TODO: move these to environment variables before merging to main
AWS_ACCESS_KEY_ID = "Cool"
AWS_SECRET_ACCESS_KEY = "Have a Nice Day"
AWS_REGION = "us-east-1"

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

def main():
    logger.info("Starting deployment...")

    buckets = list_buckets(session)
    logger.info(f"Found {len(buckets)} S3 buckets")

    instances = list_ec2_instances(session)
    logger.info(f"Found {len(instances)} EC2 reservations")

if __name__ == "__main__":
    main()
