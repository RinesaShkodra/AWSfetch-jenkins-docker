from classes.AWSAccount import AWSAccount
from classes.IAMUsers import IAMUsers
import boto3

usernames = []
def main():
  cdp_account = AWSAccount("825880227928")  

  
  boto3.setup_default_session(profile_name='luani')
  iam_client = boto3.client('iam')
  users = iam_client.list_users()["Users"]
  for user in users:
    try:
      user_name = user["UserName"]
      user_arn = user["Arn"]
     
      #Krijimi i objektit username nga class AWSUSERS
      username = IAMUsers(user_name, user_arn)
      #Shtimi i objekteve ne listen usernames
      usernames.append(username)
      
    except:
      print("no name")
    
  for u in usernames:
    print(u)
main()