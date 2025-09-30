import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def get_aws_client(service_name):

    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION = os.getenv("AWS_REGION", "us-east-2")

    # Create client params
    client_params = {"service_name": service_name, "region_name": AWS_REGION}

    # If credentials are found (local), use them
    if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY:
        client_params["aws_access_key_id"] = AWS_ACCESS_KEY_ID
        client_params["aws_secret_access_key"] = AWS_SECRET_ACCESS_KEY

    # Return the boto3 client using either local or IAM-based credentials
    return boto3.client(**client_params)