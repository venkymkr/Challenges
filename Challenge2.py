#!/usr/bin/env bash
#
# Get the value of a tag for a running EC2 instance.
#
# This can be useful within bootstrapping scripts ("user-data").
#
# Note the EC3 instance needs to have an IAM role that lets it read tags. The policy
# JSON for this looks like:
#
#    {
#      "Version": "2012-10-17",
#      "Statement": [
#        {
#          "Effect": "Allow",
#          "Action": "ec2:DescribeTags",
#          "Resource": "*"
#        }
#      ]
#    }

# Define the tag you want to get the value for
KEY=bucket

# Install AWS CLI (you could just do 'apt-get install awscli' although you'll
# get an older version).
apt-get update
apt-get install -y python-pip
pip install -U pip
pip install awscli

# Grab instance ID and region as the 'describe-tags' action below requires them. Getting the region 
# is a pain (see http://stackoverflow.com/questions/4249488/find-region-from-within-ec2-instance)
INSTANCE_ID=$(ec2metadata --instance-id)
REGION=$(curl -s http://169.254.169.254/latest/dynamic/instance-identity/document | grep region | awk -F\" '{print $4}')

# Grab tag value
TAG_VALUE=$(aws ec2 describe-tags --filters "Name=resource-id,Values=$INSTANCE_ID" "Name=key,Values=$KEY" --region=$REGION --output=text | cut -f5)