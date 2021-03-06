import boto3
import json
ec2_prices = []  
  
  


pricing_client = boto3.client('pricing', region_name='us-east-1')

def get_products(region):
    paginator = pricing_client.get_paginator('get_products')

    response_iterator = paginator.paginate(
        ServiceCode="AmazonEC2",
        Filters=[
            {
                'Type': 'TERM_MATCH',
                'Field': 'location',
                'Value': region
            },
            {
                'Type': 'TERM_MATCH',
                'Field': 'instanceType',
                'Value': 't2.micro'
            }
        ],
        PaginationConfig={
            'PageSize': 100
        }
    )

    products = []
    for response in response_iterator:
        for priceItem in response["PriceList"]:
            priceItemJson = json.loads(priceItem)["terms"]["OnDemand"]
            products.append(priceItemJson)
            id1 = list(priceItemJson)[0]
            id2 = list(priceItemJson[id1]['priceDimensions'])[0]           
            ec2_prices.append("Qmimi: " + priceItemJson[id1]['priceDimensions'][id2]['description'])
 
    for price in ec2_prices:
        print(price)     
   

if __name__ == '__main__':
    get_products('EU (Frankfurt)')