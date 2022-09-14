### Greenfield
```
$ ./deploy.sh 
Keypair nginx-key-pair created and SSH private key nginx-priv-key.pem pem file saved.
VPC ID not provided by user, using default VPC ID vpc-0edbd187d65482beb to create Security Group.
Security Group nginx-security-group created using VPC ID vpc-0edbd187d65482beb.
EC2 instance nginx-ec2 created using default subnet and default VPC ID.
Waiting for EC2 instance nginx-ec2 in pending state to reach Running state ...
Waiting for EC2 instance nginx-ec2 in pending state to reach Running state ...
EC2 instance nginx-ec2 reached Running state.
Waiting 30 seconds before SSH'ing into EC2 instance ...
Run the following command to SSH into the nginx-ec2 EC2 instance:

  ssh -i nginx-priv-key.pem ubuntu@54.157.253.185

Target Group nginx-target-grp created.
Registered EC2 instance nginx-ec2 with target group nginx-target-grp.
Load balancer nginx-lb created.
Created HTTP listener for nginx-lb load balancer.
Waiting for load balancer nginx-lb in provisioning state to reach Active state ...
Waiting for load balancer nginx-lb in provisioning state to reach Active state ...
Waiting for load balancer nginx-lb in provisioning state to reach Active state ...
Waiting for load balancer nginx-lb in provisioning state to reach Active state ...
Waiting for load balancer nginx-lb in provisioning state to reach Active state ...
Waiting for load balancer nginx-lb in provisioning state to reach Active state ...
Waiting for load balancer nginx-lb in provisioning state to reach Active state ...
Waiting for load balancer nginx-lb in provisioning state to reach Active state ...
Waiting for load balancer nginx-lb in provisioning state to reach Active state ...
Waiting for load balancer nginx-lb in provisioning state to reach Active state ...
Waiting for load balancer nginx-lb in provisioning state to reach Active state ...
Waiting for load balancer nginx-lb in provisioning state to reach Active state ...
Waiting for load balancer nginx-lb in provisioning state to reach Active state ...
Load balancer nginx-lb reached Active state.
Access nginx web server at public DNS:

    http://nginx-lb-1432264784.us-east-1.elb.amazonaws.com

Warning: Permanently added '54.157.253.185' (ED25519) to the list of known hosts.
Hit:1 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy InRelease
Get:2 http://us-east-1.ec2.archive.ubuntu.com/ubuntu jammy-updates InRelease [114 kB]
...
The following additional packages will be installed:
  fontconfig-config fonts-dejavu-core libdeflate0 libfontconfig1 libgd3
  libjbig0 libjpeg-turbo8 libjpeg8 libnginx-mod-http-geoip2
  libnginx-mod-http-image-filter libnginx-mod-http-xslt-filter
  libnginx-mod-mail libnginx-mod-stream libnginx-mod-stream-geoip2 libtiff5
  libwebp7 libxpm4 nginx-common nginx-core
Suggested packages:
  libgd-tools fcgiwrap nginx-doc ssl-cert
The following NEW packages will be installed:
  fontconfig-config fonts-dejavu-core libdeflate0 libfontconfig1 libgd3
  libjbig0 libjpeg-turbo8 libjpeg8 libnginx-mod-http-geoip2
  libnginx-mod-http-image-filter libnginx-mod-http-xslt-filter
  libnginx-mod-mail libnginx-mod-stream libnginx-mod-stream-geoip2 libtiff5
  libwebp7 libxpm4 nginx nginx-common nginx-core
...
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Wed 2022-09-14 00:47:15 UTC; 4s ago
       Docs: man:nginx(8)
    Process: 14800 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
    Process: 14801 ExecStart=/usr/sbin/nginx -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
   Main PID: 14887 (nginx)
      Tasks: 2 (limit: 1146)
     Memory: 5.5M
        CPU: 23ms
     CGroup: /system.slice/nginx.service
             ├─14887 "nginx: master process /usr/sbin/nginx -g daemon on; master_process on;"
             └─14890 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""

Sep 14 00:47:15 ip-172-31-82-9 systemd[1]: Starting A high performance web server and a reverse proxy server...
Sep 14 00:47:15 ip-172-31-82-9 systemd[1]: Started A high performance web server and a reverse proxy server.
index.nginx-debian.html                                                                                    100%   65     1.4KB/s   00:00    
Waiting 10 seconds before testing nginx web server ...
<!DOCTYPE html>
<html>
<body>
<h1>Cisco SPL</h1>
</body>
</html>
```

### Brownfield (when `deploy.sh` is rerun)
```
$ ./deploy.sh
Keypair nginx-key-pair already exists, no need to create.
Security Group nginx-security-group already exists, no need to create.
EC2 instance with name nginx-ec2 already exists, no need to create.
Target Group nginx-target-grp already exists, no need to create.
Load balancer nginx-lb already exists, no need to create.
Access nginx web server at public DNS:

    http://nginx-lb-1432264784.us-east-1.elb.amazonaws.com

Nginx web server already installed in EC2 instance.
<!DOCTYPE html>
<html>
<body>
<h1>Cisco SPL</h1>
</body>
</html>
```

### Curl public DNS name of EC2 instance running Nginx web server
```
$ curl http://nginx-lb-1432264784.us-east-1.elb.amazonaws.com
<!DOCTYPE html>
<html>
<body>
<h1>Cisco SPL</h1>
</body>
</html>
```
