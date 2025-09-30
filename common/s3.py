import uuid
import boto3
import os

s3 =  boto3.client(
        's3',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION", "us-east-1")
    )


def create_s3_folder_and_upload_file(bucket, project_id, out_dir, local_file_path):
    
    rel_path = os.path.relpath(local_file_path, out_dir)
    s3_key = f"{project_id}/{rel_path}"

    with open(local_file_path, "rb") as f:
        s3.upload_fileobj(f, bucket, s3_key)
    print(f"Uploaded {local_file_path} to s3://{bucket}/{s3_key}")