#!/usr/bin/env python3

import argparse
import boto3
import os
import time
import traceback
from validate import *


ec2 = boto3.client("ec2")
prefix = "nginx"
key_pair_name = prefix + "-key-pair"
security_group_name = prefix + "-security-group"
ec2_instance_name = prefix + "-ec2"
target_group_name = prefix + "-target-grp"
lb_name = prefix + "-lb"
parser = argparse.ArgumentParser(
    description="Tool to provision load-balanced Nginx web server in AWS."
)
parser.add_argument(
    "--vpc-id",
    type=str,
    default="",
    help="VPC ID used to create Security Group and Target Group used by the Load Balancer. "
    'If --vpc-id is not provided, the default VPC ID will be used (default: "").',
)
parser.add_argument(
    "--subnet-id",
    type=str,
    default="",
    help="Subnet ID used to create EC2 instance. "
    'If --subnet-id is not provided, the default Subnet ID will be used (default: "").',
)
args = parser.parse_args()
vpc_id = args.vpc_id
subnet_id = args.subnet_id
ami_image_name = "ubuntu-jammy-22.04-amd64-server-20220609"
timeout_interval = 600  # Timeout interval in seconds used for polling


# Create key pair
def create_key_pair():
    response = ec2.create_key_pair(
        KeyName=key_pair_name, KeyType="ed25519", KeyFormat="pem"
    )
    if os.path.exists(prefix + "-priv-key.pem"):
        os.chmod("./" + prefix + "-priv-key.pem", 0o777)
        os.remove("./" + prefix + "-priv-key.pem")
    # Save SSH private key pem file
    with open(prefix + "-priv-key.pem", "w") as f:
        f.write(response["KeyMaterial"])
    os.chmod("./" + prefix + "-priv-key.pem", 0o400)
    print(
        "Keypair",
        key_pair_name,
        "created and SSH private key",
        prefix + "-priv-key.pem",
        "pem file saved.",
    )


# Create security group
def create_security_group():
    vpcId = ""
    if vpc_id == "":
        for vpc in ec2.describe_vpcs()["Vpcs"]:
            if vpc["IsDefault"]:
                vpcId = vpc["VpcId"]
                print(
                    f"VPC ID not provided by user, using default VPC ID {vpcId} to create Security Group."
                )
    else:
        vpcId = vpc_id
        print(
            f"Using non-default VPC ID {vpcId} provided by user to create Security Group."
        )
    ec2.create_security_group(
        GroupName=security_group_name,
        Description="Security Group for " + prefix,
        VpcId=vpcId,
    )
    # Allow TCP port 22 for SSH access
    ec2.authorize_security_group_ingress(
        GroupName=security_group_name,
        CidrIp="0.0.0.0/0",
        IpProtocol="tcp",
        FromPort=22,
        ToPort=22,
    )
    # Allow TCP port 80 for HTTP
    ec2.authorize_security_group_ingress(
        GroupName=security_group_name,
        CidrIp="0.0.0.0/0",
        IpProtocol="tcp",
        FromPort=80,
        ToPort=80,
    )
    print(f"Security Group {security_group_name} created using VPC ID {vpcId}.")


# Get image ID of Ubuntu AMI image
def get_ami_image_id(image_name):
    ec2 = boto3.resource("ec2")
    filters = [{"Name": "name", "Values": ["*" + image_name + "*"]}]
    images = ec2.images.filter(Filters=filters).all()
    for image in images:
        return image.id
    raise Exception("Error: AMI image " + image_name + " not found.")


# Create EC2 instance
def create_ec2_instance():
    ec2 = boto3.resource("ec2")
    if subnet_id == "":
        instance = ec2.create_instances(
            ImageId=get_ami_image_id(ami_image_name),
            InstanceType="t2.micro",
            KeyName=key_pair_name,
            SecurityGroups=[security_group_name],
            TagSpecifications=[
                {
                    "ResourceType": "instance",
                    "Tags": [{"Key": "Name", "Value": ec2_instance_name}],
                }
            ],
            MinCount=1,
            MaxCount=1,
        )
        print(
            "EC2 instance",
            ec2_instance_name,
            "created using default subnet and default VPC ID.",
        )
    else:
        instance = ec2.create_instances(
            ImageId=get_ami_image_id(ami_image_name),
            InstanceType="t2.micro",
            KeyName=key_pair_name,
            SecurityGroups=[security_group_name],
            TagSpecifications=[
                {
                    "ResourceType": "instance",
                    "Tags": [{"Key": "Name", "Value": ec2_instance_name}],
                }
            ],
            MinCount=1,
            MaxCount=1,
            SubnetId=subnet_id,
        )
        print(
            "EC2 instance",
            ec2_instance_name,
            "created using non-default subnet ID",
            subnet_id,
            "and default VPC ID.",
        )


# Check if EC2 instance reached Running state
def check_ec2_instance_state():
    for x in range(timeout_interval // 10):
        for i in ec2.describe_instances()["Reservations"]:
            for tag in i["Instances"][0]["Tags"]:
                if tag["Key"] == "Name" and tag["Value"] == ec2_instance_name:
                    if i["Instances"][0]["State"]["Name"].lower() == "running":
                        print(
                            "EC2 instance", ec2_instance_name, "reached Running state."
                        )
                        return
                    else:
                        print(
                            "Waiting for EC2 instance",
                            ec2_instance_name,
                            "in",
                            i["Instances"][0]["State"]["Name"],
                            "state to reach Running state ...",
                        )
                        # Retry after 10 seconds
                        time.sleep(10)
        # EC2 instance did not reach Running state
        if x == (timeout_interval // 10) - 1:
            raise Exception(
                "Error: EC2 instance "
                + ec2_instance_name
                + " did not reach Running state after waiting for "
                + str(timeout_interval)
                + " seconds."
            )


# Get public IP address of EC2 instance
def get_ec2_instance_public_ip():
    for i in ec2.describe_instances()["Reservations"]:
        for tag in i["Instances"][0]["Tags"]:
            if tag["Key"] == "Name" and tag["Value"] == ec2_instance_name:
                return i["Instances"][0]["PublicIpAddress"]
    return ""


# Get EC2 instance's VPC ID
def get_ec2_instance_vpc_id():
    for i in ec2.describe_instances()["Reservations"]:
        for tag in i["Instances"][0]["Tags"]:
            if tag["Key"] == "Name" and tag["Value"] == ec2_instance_name:
                return i["Instances"][0]["VpcId"]
    return ""


# Get instance ID of EC2 instance
def get_ec2_instance_id():
    for i in ec2.describe_instances()["Reservations"]:
        for tag in i["Instances"][0]["Tags"]:
            if tag["Key"] == "Name" and tag["Value"] == ec2_instance_name:
                return i["Instances"][0]["InstanceId"]
    return ""


# Get security group ID
def get_security_group_id():
    for sg in ec2.describe_security_groups()["SecurityGroups"]:
        if sg["GroupName"] == security_group_name:
            return sg["GroupId"]
    return ""


# Create target group
def create_target_group():
    client = boto3.client("elbv2")
    target_grp = None

    if vpc_id == "":
        target_grp = client.create_target_group(
            Name=target_group_name,
            Protocol="HTTP",
            ProtocolVersion="HTTP1",
            Port=80,
            VpcId=get_ec2_instance_vpc_id(),
            HealthCheckProtocol="HTTP",
            HealthCheckPort="traffic-port",
            HealthCheckEnabled=True,
            HealthCheckPath="/",
            HealthCheckIntervalSeconds=30,
            HealthCheckTimeoutSeconds=5,
            HealthyThresholdCount=5,
            UnhealthyThresholdCount=2,
            Matcher={"HttpCode": "200"},
            TargetType="instance",
            IpAddressType="ipv4",
        )
    else:
        target_grp = client.create_target_group(
            Name=target_group_name,
            Protocol="HTTP",
            ProtocolVersion="HTTP1",
            Port=80,
            # Use VPC ID provided by user
            VpcId=vpc_id,
            HealthCheckProtocol="HTTP",
            HealthCheckPort="traffic-port",
            HealthCheckEnabled=True,
            HealthCheckPath="/",
            HealthCheckIntervalSeconds=30,
            HealthCheckTimeoutSeconds=5,
            HealthyThresholdCount=5,
            UnhealthyThresholdCount=2,
            Matcher={"HttpCode": "200"},
            TargetType="instance",
            IpAddressType="ipv4",
        )
    print("Target Group", target_group_name, "created.")
    target_grp_arn = target_grp["TargetGroups"][0]["TargetGroupArn"]
    # Register EC2 instance with target group
    client.register_targets(
        TargetGroupArn=target_grp_arn,
        Targets=[
            {
                "Id": get_ec2_instance_id(),
                "Port": 80,
            },
        ],
    )
    print(
        f"Registered EC2 instance {ec2_instance_name} with target group {target_group_name}."
    )


# Get two subnet IDs needed to create load balancer
def get_subnet_ids_for_lb():
    az1 = ""
    for i in ec2.describe_instances()["Reservations"]:
        for tag in i["Instances"][0]["Tags"]:
            if tag["Key"] == "Name" and tag["Value"] == ec2_instance_name:
                az1 = i["Instances"][0]["Placement"]["AvailabilityZone"]
    us_east_zones = [
        "us-east-1a",
        "us-east-1b",
        "us-east-1c",
        "us-east-1d",
        "us-east-1e",
    ]
    us_east_zones.remove(az1)
    az2 = us_east_zones[0]
    lb_az = [az1, az2]
    subnet_ids_for_lb = []
    for az in lb_az:
        for subnet in ec2.describe_subnets()["Subnets"]:
            if subnet["AvailabilityZone"] == az:
                subnet_ids_for_lb.append(subnet["SubnetId"])
    return subnet_ids_for_lb


# Create load balancer
def create_lb():
    client = boto3.client("elbv2")
    lb = client.create_load_balancer(
        Name=lb_name,
        Subnets=get_subnet_ids_for_lb(),
        Scheme="internet-facing",
        Type="application",
        SecurityGroups=[get_security_group_id()],
        IpAddressType="ipv4",
    )
    print("Load balancer", lb_name, "created.")
    lb_arn = lb["LoadBalancers"][0]["LoadBalancerArn"]
    tg_arn = ""
    for tg in client.describe_target_groups()["TargetGroups"]:
        if tg["TargetGroupName"] == target_group_name:
            tg_arn = tg["TargetGroupArn"]
    # Create HTTP listener for load balancer
    client.create_listener(
        DefaultActions=[
            {
                "TargetGroupArn": tg_arn,
                "Type": "forward",
            },
        ],
        LoadBalancerArn=lb_arn,
        Port=80,
        Protocol="HTTP",
    )
    print("Created HTTP listener for", lb_name, "load balancer.")


# Check if load balancer reached Active state
def check_lb_state():
    client = boto3.client("elbv2")
    for x in range(timeout_interval // 10):
        for lb in client.describe_load_balancers()["LoadBalancers"]:
            if lb["LoadBalancerName"] == lb_name:
                if lb["State"]["Code"].lower() == "active":
                    print("Load balancer", lb_name, "reached Active state.")
                    return
                else:
                    print(
                        "Waiting for load balancer",
                        lb_name,
                        "in",
                        lb["State"]["Code"],
                        "state to reach Active state ...",
                    )
                    # Retry after 10 seconds
                    time.sleep(10)
        # Load balancer did not reach Active state
        if x == (timeout_interval // 10) - 1:
            raise Exception(
                "Error: Load balancer "
                + lb_name
                + " did not reach Active state after waiting for "
                + str(timeout_interval)
                + " seconds."
            )


# Get DNS name of load balancer
def get_lb_dns_name():
    client = boto3.client("elbv2")
    for lb in client.describe_load_balancers()["LoadBalancers"]:
        if lb["LoadBalancerName"] == lb_name:
            return lb["DNSName"]
    return ""


try:
    # Create key pair if it does not exist
    if key_pair_exists(key_pair_name=key_pair_name):
        print("Keypair", key_pair_name, "already exists, no need to create.")
    else:
        create_key_pair()

    # Create security group if it does not exist
    if security_groups_exists(security_group_name=security_group_name):
        print(
            "Security Group", security_group_name, "already exists, no need to create."
        )
    else:
        create_security_group()

    # Create EC2 instance if it does not exist
    if ec2_instance_exists(instance_name=ec2_instance_name):
        print(
            "EC2 instance with name",
            ec2_instance_name,
            "already exists, no need to create.",
        )
    else:
        create_ec2_instance()
        check_ec2_instance_state()
        print("Waiting 30 seconds before SSH'ing into EC2 instance ...")
        time.sleep(30)
        print(
            "Run the following command to SSH into the",
            ec2_instance_name,
            "EC2 instance:",
        )
        print(
            "\n  ssh -i nginx-priv-key.pem ubuntu@"
            + get_ec2_instance_public_ip()
            + "\n"
        )

    # Create target group it does not exist
    if target_group_exists(target_group_name=target_group_name):
        print("Target Group", target_group_name, "already exists, no need to create.")
    else:
        create_target_group()

    # Create ELB load balancer it does not exist
    if lb_exists(lb_name=lb_name):
        print("Load balancer", lb_name, "already exists, no need to create.")
    else:
        create_lb()
        check_lb_state()
    print(
        "Access nginx web server at public DNS:\n\n    http://"
        + get_lb_dns_name()
        + "\n"
    )
except Exception as inst:
    print("Error:", inst, ",", type(inst))
    print("Error:", inst.args)
    print(traceback.format_exc())
    # Cleanup after error:
    #  - delete all the resources created if they are not needed after error
    #  - do not delete anything if the resources created are needed to debug error
