import boto3
import json
import os

from crhelper import CfnResource

helper = CfnResource(
    json_logging=False,
    log_level='DEBUG',
    boto_level='CRITICAL'
)


def handler(event, context):
    print(event)
    print(context)
    # print(event['ResourceProperties']['Bucket'])
    helper(event, context)


@helper.create
def create(event, context):
    print("Got create")

    put_manifest_to_s3(event['ResourceProperties']['Bucket'])
    create_data_source(event['ResourceProperties']['Bucket'])

    return event['LogicalResourceId']


@helper.update
def update(event, context):
    print("Got Update")
    put_manifest_to_s3(event['ResourceProperties']['Bucket'])
    # create_data_source(event['ResourceProperties']['Bucket'])
    return event['LogicalResourceId']


@helper.delete
def delete(event, context):
    print("Got Delete")


def put_manifest_to_s3(bucket):
    print('put_manifest_to_s3')

    s3 = boto3.client('s3')
    json_object = {'fileLocations': [{"URIPrefixes": [
        "https://s3-eu-central-1.amazonaws.com/"+bucket+"/data/"
    ]}], "globalUploadSettings": {"format": "JSON"}}

    key_name = 'eltest_manifest.json'
    s3.put_object(
        Body=str(json.dumps(json_object)),
        Bucket=bucket,
        Key=key_name
    )
    print('put_manifest_to_s3 - completed')

    return


def create_data_source(bucket):
    print('create_data_source')
    account_id = os.environ.get('ACCOUNT_ID')
    stage = os.environ.get('STAGE')
    print(account_id)
    print(stage)
    print(bucket)

    client = boto3.client('quicksight')
    response = client.create_data_source(
        AwsAccountId=account_id,
        DataSourceId='eltest-'+stage,
        Name='eltest-'+stage,
        Type='S3',
        DataSourceParameters={
            'S3Parameters': {
                'ManifestFileLocation': {
                    'Bucket': bucket,
                    'Key': 'eltest_manifest.json'
                }
            }
        }
    )
    print(response)
    print('after create datasource')
    return


