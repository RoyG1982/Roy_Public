#!/bin/bash
machine_name=$1
machine_tag=$2

aws ec2 run-instances \
    --image-id ami-05d38da78ce859165 \
    --instance-type t2.micro \
    --key-name RoyG_key \
    --security-group-ids sg-02b3d29bdcd49a0cc \
    --subnet-id subnet-06d26c27601fa5b42 \
    --count 1 \
    --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=$machine_name},{Key=Purpose,Value=$machine_tag}]" \
--output json > instance-details.json