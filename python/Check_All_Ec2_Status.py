# /usr/bin/python2.7

import boto3
import os

access_key = os.getenv('AWS_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')

client = boto3.client('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,
                                  region_name='ap-south-1')

ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]

for region in ec2_regions:
    print "Region Name : " + region
    print "--------------------------------------------"
    conn = boto3.resource('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key,
                   region_name=region)
    instances = conn.instances.filter()
    for instance in instances:
#        if instance.state["Name"] == "running":
            print (instance.id, instance.instance_type, region,instance.state["Name"])
