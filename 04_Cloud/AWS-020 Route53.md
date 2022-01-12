# [Amazon Route 53]
Amazon Route 53 is a highly available and scalable cloud Domain Name System (DNS) web service. It is designed to give developers and businesses an extremely reliable and cost effective way to route end users to Internet applications by translating names like www.example.com into the numeric IP addresses like 192.0.2.1 that computers use to connect to each other. Amazon Route 53 is fully compliant with IPv6 as well.

Amazon Route 53 effectively connects user requests to infrastructure running in AWS – such as Amazon EC2 instances, Elastic Load Balancing load balancers, or Amazon S3 buckets – and can also be used to route users to infrastructure outside of AWS. You can use Amazon Route 53 to configure DNS health checks, then continuously monitor your applications’ ability to recover from failures and control application recovery with Route 53 Application Recovery Controller.

Amazon Route 53 Traffic Flow makes it easy for you to manage traffic globally through a variety of routing types, including Latency Based Routing, Geo DNS, Geoproximity, and Weighted Round Robin—all of which can be combined with DNS Failover in order to enable a variety of low-latency, fault-tolerant architectures. Using Amazon Route 53 Traffic Flow’s simple visual editor, you can easily manage how your end-users are routed to your application’s endpoints—whether in a single AWS region or distributed around the globe. Amazon Route 53 also offers Domain Name Registration – you can purchase and manage domain names such as example.com and Amazon Route 53 will automatically configure DNS settings for your domains

## Key-terms
* **Amazon Route 53 Resolve** :- Route 53 Resolver is a regional DNS service that provides recursive DNS lookups for names hosted in EC2 as well as public names on the internet. This functionality is available by default in every Amazon Virtual Private Cloud (VPC). For hybrid cloud scenarios you can configure conditional forwarding rules and DNS endpoints to enable DNS resolution across AWS Direct Connect and AWS Managed VPN.

* **Recursive DNS** :- Amazon Route 53 is both an Authoritative DNS service and Recursive DNS service. Authoritative DNS contains the final answer to a DNS query, generally an IP address. Clients (such as mobile devices, applications running in the cloud, or servers in your datacenter) don’t actually talk directly to authoritative DNS services, except in very rare cases. Instead, clients talk to recursive DNS services (also known as DNS resolvers) which find the correct authoritative answer for any DNS query. Route 53 Resolver is a recursive DNS service.

When receiving a query, a recursive DNS service like Route 53 Resolver may either be configured to automatically forward the query directly to a specific recursive DNS server, or it may recursively search beginning with the root of the domain and continuing until it finds the final answer. In either case, once an answer is found, the recursive DNS server may cache the answer for a period of time so it can answer subsequent queries for the same name more quickly in the future.

* **Conditional forwarding rules**

Conditional forwarding rules allow Resolver to forward queries for specified domains to the target IP address of your choice, typically an on-premises DNS resolver. Rules are applied at the VPC level and can be managed from one account and shared across multiple accounts

* **DNS endpoints**

A DNS endpoint includes one or more elastic network interfaces (ENI) that attach to your Amazon Virtual Private Cloud (VPC). Each ENI is assigned an IP address from the subnet space of the VPC where it is located. This IP address can then serve as a forwarding target for on-premises DNS servers to forward queries. Endpoints are required both for DNS query traffic that you're forwarding from VPCs to your network and from your network to your VPCs over AWS Direct Connect and Managed VPN.

* **Amazon Route 53 Resolver DNS Firewall**
Amazon Route 53 Resolver DNS Firewall is a feature that allows you to quickly deploy DNS protections across all of your Amazon Virtual Private Clouds (VPCs). The Route 53 Resolver DNS Firewall allows you to block queries made for known malicious domains (i.e. create “denylists”) and to allow queries for trusted domains (create “allowlists”) when using the Route 53 Resolver for recursive DNS Resolution. You can also quickly get started with protections against common DNS threats by using AWS Managed Domain Lists. Amazon Route 53 Resolver DNS Firewall works together with AWS Firewall Manager so you can build policies based on DNS Firewall rules, and then centrally apply those policies across your VPCs and accounts.


## Opdracht
20.1 What is Route 53?

20.2 How does Route 53 fit or replace in a classic setting?

20.3 How can I combine Route 53t with other services?

20.4 What is the difference between Route 53 and other similar services?

### Gebruikte bronnen
https://aws.amazon.com/route53/
https://rakeshjain-devops.medium.com/elb-vs-route-53-routing-a84e91183697

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat
**20.1 What is Route 53?**
Information shared in introduction.

**20.2 How does Route 53 fit or replace in a classic setting?**


**20.3 How can I combine Route 53 with other services?**
* Amazon Route 53 is designed to work well with other AWS features and offerings. You can use Amazon Route 53 to map domain names to your Amazon EC2 instances, Amazon S3 buckets, Amazon CloudFront distributions, and other AWS resources. By using the AWS Identity and Access Management (IAM) service with Amazon Route 53, you get fine grained control over who can update your DNS data. You can use Amazon Route 53 to map your zone apex (example.com versus www.example.com) to your Elastic Load Balancing instance, Amazon CloudFront distribution, AWS Elastic Beanstalk environment, API Gateway, VPC endpoint, or Amazon S3 website bucket using a feature called Alias record.

* By integrating Amazon Route 53 with AWS Identity and Access Management (IAM), you can grant unique credentials and manage permissions for every user within your AWS account and specify who has access to which parts of the Amazon Route 53 service. When you enable Amazon Route 53 Resolver DNS firewall, you can configure it to inspect outbound DNS requests against a list of known malicious domains.

* Queries for qualifying alias records are provided at no additional cost to Route 53 customers. You can create alias records for AWS resources, such as:

  * Elastic Load Balancers
  * Amazon CloudFront distributions
  * AWS Elastic Beanstalk environments
  * Amazon S3 buckets that are configured as website endpoints

* Using the Amazon Route 53 console can generate API calls to Amazon Simple Storage Service (Amazon S3). Actions such as identifying Alias record targets sends API calls to S3, such as LIST_ALL_MY_BUCKETS. 

**20.4 What is the difference between Route 53 and other similar services?**

* ELB vs Route 53 routing

ELBs are intended to load balance across EC2 instances in a ‘single’ region among Multiple Availability Zone. Whereas DNS load-balancing (Route 53) is intended to help balance traffic ‘across’ regions. Route53 policies like geolocation may help direct traffic to preferred regions, then ELBs route between instances within one region.
Functionally, another difference is that DNS-based routing (e.g. Route 53) only changes the address that your clients’ requests resolve to. On the other hand, an ELB actually reroutes traffic.
One analogy is: if you ask for the closest WalMart, you may get an address based on your location, but you could choose to go to another Walmart if you know one. That’s Route 53; it just switches the address resolved based on some context. On the other hand, a policeman redirecting traffic because of construction, is more like an ELB, he/she is actually changing the traffic flow, not just suggesting.
There are additional considerations about whether DNS-based routing versus Load Balancing is best for your use case, and why (or if) Route53 and ELB continue to co-exist, but hopefully this helps at a high-level.
Another difference is with ELB you can use autoscaling to automatically register new instances added to the group with the ELB, you do not have to do anything yourself. With Route53 you have to either manually replace the old failed instance with the new one in the route or add some script to your launch configuration to automatically register the new instance with Route53 and remove the failed one.