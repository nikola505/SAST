import os

def connect_to_aws():
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

    if not aws_access_key_id or not aws_secret_access_key:
        raise EnvironmentError("AWS credentials not set in environment variables.")

    print("Connecting with", aws_access_key_id[:6] + "...", "(secret hidden)")

connect_to_aws()
