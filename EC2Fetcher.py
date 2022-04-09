from classes.AWSAccount import AWSAccount
from classes.AWSEc2  import EC2instances
import boto3
import os
import csv
instances_list = []
instances_db = []
def main():
  #cdp_account = AWSAccount("825880227928")  # pass access & secret keys
  # print(cdp_account.account_id)

  
  
  ec2_client = boto3.client('ec2',
                            aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
                            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                            region_name="eu-central-1")
  instances = ec2_client.describe_instances()["Reservations"]
  for instance in instances:
    try:
      instance_name = instance["Instances"][0]["KeyName"]
      ami_id = instance["Instances"][0]["ImageId"]
      model = instance["Instances"][0]["InstanceType"]
      dns_name = instance["Instances"][0]["PrivateDnsName"]
      instance1 = EC2instances(instance_name,ami_id,model,dns_name)
      instances_list.append(instance1)
      instances_db.append(instance1)
    except:
        instance1 = EC2instances("",ami_id,model,dns_name)
   
  for u in instances_list:
    print(u)
  
  
main()