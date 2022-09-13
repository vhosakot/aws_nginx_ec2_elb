## Tool to provision load-balanced Nginx web server in AWS.

#### Install dependencies
This tool assumes that Python3 is installed. If not, install it from https://www.python.org/downloads/.
```
sudo pip3 install -r requirements.txt
```

#### Set AWS access keys and AWS region in `~/.aws/credentials`
```
[default]
aws_access_key_id = AWS_ACCESS_KEY_ID
aws_secret_access_key = AWS_SECRET_ACCESS_KEY
region = AWS_REGION
```

#### Run the tool
```
./deploy.sh
```
VPC ID and Subnet ID can be optionally passed as arguments to `deploy.sh` the following way:
```
./deploy.sh [-vpcID VPC_ID] [-subnetID SUBNET_ID]

$ ./deploy.sh -help

Tool to provision load-balanced Nginx web server in AWS.

Usage: ./deploy.sh [-vpcID VPC_ID] [-subnetID SUBNET_ID]

       VPC_ID     VPC ID used to create Security Group and Target Group
                  used by the Load Balancer. If VPC_ID is not provided,
                  the default VPC ID will be used (default: "").

       SUBNET_ID  Subnet ID used to create EC2 instance. If SUBNET_ID
                  is not provided, the default Subnet ID will be used (default: "").
```
`deploy.sh` is idempotent and can be run multiple times and AWS resources will not be created if they are already created.

#### Design and development iterations
 - Setup environment - install Python3 and pip3 packages (boto3, black Python code formatter)
 - Set AWS access keys in `~/.aws/credentials` and test boto3 AWS APIs
 - Create key pair and download private SSH key as pem file
 - Create security group and allow TCP ports `22` and `80` for SSH and HTTP repectively
 - Create EC2 instance using Ubuntu AMI
 - Wait until EC2 instance reaches `Running` state
 - Get the public IP address of the EC2 instance
 - Iterations to create load balancer:
     - Create target group and register EC2 instance with target group
     - Create application load balancer using EC2 instance's subnet ID
     - Create HTTP listener on TCP port 80 for the load balancer
     - Wait until load balancer reaches `Active` state
     - Get public DNS name of load balancer
 - Iterations to install Nginx web server in EC2 instance using bash and by SSH'ing into the EC2 instance:
     - Update and upgrade Ubuntu apt repos in EC2 instance
     - Install Nginx web server using apt and print its status
     - Add static home page that says "Cisco SPL" for Nginx at `/var/www/html/index.nginx-debian.html` using SCP
     - Restart Nginx web server with updated `/var/www/html/index.nginx-debian.html` in EC2 instance
 - Iterations to test:
     - Test using public IP address of EC2 instance by accessing `http://<public IP address of EC2 instance>` and verify that it shows "Cisco SPL"
     - Test using public DNS name of the load balancer by accessing `http://<DNS name of load balancer>` and verify that it shows "Cisco SPL"
     - Make sure that this tool is idempotent - run `deploy.sh` multiple times and verify that resources in AWS are not created if they are already created
     - Cleanup: This tool does not delete any resource currently so that we can debug if there is an error. To cleanup, delete all the resources manually in the following order in the AWS management web console and rerun `deploy.sh` to provision and test again from scratch:
       - Delete load balancer
       - Delete target group
       - Terminate EC2 instance
       - Wait until EC2 instance reaches `Terminated` state
       - Delete key pair
       - Delete security group

#### Troubleshooting
If the number of requests from clients exceed the capacity of the Nginx web server and overload it, `troubleshoot.sh` can be used to print diagnostic information about the system and to try to recover the overloaded Nginx web server:
```
./troubleshoot.sh <public IP address of EC2 instance>
```
