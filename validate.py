#!/usr/bin/env python3

import boto3

ec2 = boto3.client("ec2")


# Returns true if EC2 instance exists in AWS
def ec2_instance_exists(instance_name):
    for reservation in ec2.describe_instances()["Reservations"]:
        instances = reservation["Instances"]
        for instance in instances:
            for tag in instance["Tags"]:
                if tag["Key"] == "Name" and tag["Value"] == instance_name:
                    return True
    return False


# Returns true if key pair exists
def key_pair_exists(key_pair_name):
    for key_pair in ec2.describe_key_pairs()["KeyPairs"]:
        if key_pair["KeyName"] == key_pair_name:
            return True
    return False


# Returns true if security group exists
def security_groups_exists(security_group_name):
    for security_group in ec2.describe_security_groups()["SecurityGroups"]:
        if security_group["GroupName"] == security_group_name:
            return True
    return False


# Returns true if target group exists
def target_group_exists(target_group_name):
    client = boto3.client("elbv2")
    for tg in client.describe_target_groups()["TargetGroups"]:
        if tg["TargetGroupName"] == target_group_name:
            return True
    return False


# Returns true if load balancer exists
def lb_exists(lb_name):
    client = boto3.client("elbv2")
    for lb in client.describe_load_balancers()["LoadBalancers"]:
        if lb["LoadBalancerName"] == lb_name:
            return True
    return False
