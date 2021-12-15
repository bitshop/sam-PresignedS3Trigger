import json
import boto3
from botocore.exceptions import ClientError
import uuid
import logging

def create_presigned_url(bucket_name, object_name, expiration=3600):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3')
    try:
        response = 'abc'
        response = s3_client.generate_presigned_post(bucket_name, object_name)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response

def lambda_handler(event, context):

    object_name = uuid.uuid4().hex
    url = create_presigned_url("sr-example-get-object-python3", object_name, expiration=300)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "url": url
        }),
    }

