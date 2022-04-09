import boto3
from EC2Fetcher import instances_db



dynamodb = boto3.resource('dynamodb',
                           region_name="eu-central-1")
table = dynamodb.Table('EC2_instances')
table.put_item(
   Item={
        'Name': instances_db[1].name ,
        'Ami': instances_db[1].ami,
        'Instance Type': instances_db[1].type,
        'Dns': instances_db[1].dns,
   }

   
)



#for u in instances_list:
   