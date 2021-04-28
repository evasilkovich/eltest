import boto3
import json
import os
import time


def put_object():
    s3 = boto3.client('s3')
    bucket_name = os.environ.get('MY_BUCKET')
    json_object = {'datetime': time.strftime("%Y-%m-%d %H:%M:%S")}
    key_name = 'data/'+ time.strftime("%Y-%m-%d-%H:%M:%S")+'.json'
    s3.put_object(
        Body=str(json.dumps(json_object)),
        Bucket=bucket_name,
        Key=key_name
    )
    return


def handler(event, context):

    put_object()
    response = {
        "statusCode": 200,
        "body": "helloworld"
    }

    return response
