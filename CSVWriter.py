from UserFetcher import usernames
import csv


# Write users to a CSV file
with open('cdp-users.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'ARN']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)             
    writer.writeheader()
    for user in usernames:
     writer.writerow({'Name': user.name, 'ARN': user.arn})