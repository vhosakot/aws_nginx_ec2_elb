#!/usr/bin/env bash

# set -euxo pipefail

# Read VPC ID and Subnet ID in optional command line arguments
while getopts 'v:s:h' OPTION; do
    case "$OPTION" in
        h | help)
            echo -e "\nTool to provision load-balanced Nginx web server in AWS."
            echo -e "\nUsage: $0 [-vpcID VPC_ID] [-subnetID SUBNET_ID]"
            echo -e "\n       VPC_ID     VPC ID used to create Security Group and Target Group"
            echo "                  used by the Load Balancer. If VPC_ID is not provided,"
            echo "                  the default VPC ID will be used (default: \"\")."
            echo -e "\n       SUBNET_ID  Subnet ID used to create EC2 instance. If SUBNET_ID"
            echo -e "                  is not provided, the default Subnet ID will be used (default: \"\").\n"
            exit 1
    esac
done

shift "$(($OPTIND -1))"
# Provision load-balanced EC2 instance in AWS
if [ -z $1 ]; then
    ./deploy.py --vpc-id "" --subnet-id ""
else
    ./deploy.py --vpc-id $1 --subnet-id $3
fi

ec2_instance_public_ip=`python3 -c "import deploy ; print(deploy.get_ec2_instance_public_ip())" | tail -1`
if ssh -i nginx-priv-key.pem ubuntu@$ec2_instance_public_ip "sudo systemctl status nginx &> /dev/null"; then
    echo "Nginx web server already installed in EC2 instance."
else
    # Install Nginx web server in EC2 instance
    ssh -i nginx-priv-key.pem ubuntu@$ec2_instance_public_ip "sudo apt-get -y update"
    ssh -i nginx-priv-key.pem ubuntu@$ec2_instance_public_ip "sudo apt-get -y upgrade"
    ssh -i nginx-priv-key.pem ubuntu@$ec2_instance_public_ip "sudo apt-get -y install nginx"
    ssh -i nginx-priv-key.pem ubuntu@$ec2_instance_public_ip "sudo systemctl status nginx"
    rm -rf index.nginx-debian.html

    # Static home page for Nginx web server
    cat > index.nginx-debian.html <<-EOF
	<!DOCTYPE html>
	<html>
	<body>
	<h1>Cisco SPL</h1>
	</body>
	</html>
	EOF

    # SCP static home page for Nginx onto EC2 instance and restart Nginx
    scp -i nginx-priv-key.pem ./index.nginx-debian.html ubuntu@$ec2_instance_public_ip:~/index.nginx-debian.html
    ssh -i nginx-priv-key.pem ubuntu@$ec2_instance_public_ip "sudo mv ~/index.nginx-debian.html /var/www/html/index.nginx-debian.html"
    ssh -i nginx-priv-key.pem ubuntu@$ec2_instance_public_ip "sudo systemctl restart nginx"
    rm -rf index.nginx-debian.html
    echo "Waiting 10 seconds before testing nginx web server ..."
    sleep 10
fi
# Test Nginx web server
curl http://$ec2_instance_public_ip
