from pprint import pprint
import boto3
boto3.setup_default_session(profile_name='luani')

dynamodb = boto3.resource('dynamodb')
table = dynamodb.create_table(
    TableName='EC2_instances',
    KeySchema=[
        {
            'AttributeName': 'Name',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'Ami',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Name',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Ami',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)    