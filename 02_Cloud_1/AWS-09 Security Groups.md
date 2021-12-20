AWS-09 Security Groups
# [Onderwerp]
Introduction:
Security Groups are stateful virtual firewalls that can be assigned to instances. They do not run in the OS, but rather in the VPC.

One Security Group can be assigned to multiple instances. The other way around, one instance can have up to 5 Security Groups.

Security Groups only have allow rules. Everything not explicitly allowed is automatically implicitly denied.

A Network Access Control List (NACL) is a stateless firewall that runs on the subnet level in a VPC.
A NACL has both explicit allow and deny rules. Rules have a number assigned to them. This number indicates the order in which the rules are applied.

By default, a NACL is configured to allow all traffic in and out of the network.
Requirements:


Study:
Security Groups in AWS
Network Access Control Lists in AWS

## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

## Opdracht
### Gebruikte bronnen
[https://aviatrix.com/learn-center/cloud-security/aws-security-groups/
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html
https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html
https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html#VPC_Security_Comparison
https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html]

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat
[What are Security Groups in Amazon Web Services (AWS?)
Introduction to AWS Security Groups
Amazon web services provide a wide range of IT infrastructure, on-demand, and scalable cloud computing services. As such, many clients will tend to trust the platform if it allows for some level of security regarding cloud workloads and projects — and where network traffic can be filtered appropriately.

To maintain and provide this level of security, AWS is built with security groups that support some degree of control of network traffic associated with EC2 instances.

A security group is an AWS firewall solution that performs one primary function: to filter incoming and outgoing traffic from an EC2 instance. It accomplishes this filtering function at the TCP and IP layers, via their respective ports, and source/destination IP addresses.

The Function of Security Groups
Every Security Group works in a similar fashion to a firewall as it carries a set of rules that filter traffic entering and leaving the EC2 instances. As said earlier, security groups are associated with the EC2 instances and offer protection at the ports and protocol access level. Typically, the firewall possesses a ‘Deny rule,’ but the SG has a “Deny All” that allows data packets to be dropped if no rule is assigned to them from the source IP.

Also, when compared to a Network Access Control List (NACL), security groups form the first layer of defense at the instance level in a cloud computing environment whereas NACLs provides a second layer of protection at the subnet level.

When creating a security group, each group will be assigned to a particular virtual private cloud VPC. It’s also an excellent approach to give each group a name and description for easy access from the account menus. It’s also important to note that when creating a security group, you should ensure that it is assigned to the VPC it’s meant to protect to avoid errors.

Rules guiding AWS Security Groups
AWS Security Groups have a set of rules that filter traffic in two ways: inbound and outbound. Since AWS security groups are assigned differently, you won’t be needing the same rules for both inbound and outbound traffic. Thus, any provision that permits traffic into the EC2 instance will ultimately filter outbound traffic.

To further break this down each rule is made up of four principal components: Type, Protocol, Port Range, and Source. There is also a space for a description as well.


The rule allows for selection of the common type of protocols such as HTTP, SSH, etc., and it opens a drop-down menu were all the protocols are listed.

Protocols are automatically selected to be the TCP. However, it can be changed to UDP, ICMP as well as assigns a corresponding association to IPv4 or IPv6.

Port Range is also pre-filled, but you can decide to choose the port range of your choice depending on the protocol. Nonetheless, there will be times when you will have to use the custom port range number. A selection of ICMP will grey out the port selection option as it is not a layer 4 protocol.

Source (custom IP) this can be a particular IP address or a subnet range. However, you can grant access using the anywhere source IP (0.0.0.0/0) value. Allowing access through the anywhere source can turn out to be a mistake every AWS user should avoid. It will be a discussion in the best practices section below.

Some Tips on Configuring Security Groups:
1. Avoid incoming traffic through (0.0.0.0/0).
One common mistake is to allow inbound traffic from (0.0.0.0/0). It could end up exposing sensitive cloud information to outside threats. Though the security group performs its initial layer filtering when all inbound traffic is allowed but ultimately allows for many risks during the process.


Avoid opening the floodgates to the entire internet

The best thing to do is permit only necessary IP ranges and their respective ports to send incoming traffic, and all other connection attempts will be dropped. When working with EC2 instances, all workloads are only exposed based on the implemented rules of the Security Group applied to that instance.


2. Delete unused security groups
There is no need to keep a security group not assigned to an EC2 instance. Ensure that all unused SG’s are deleted to keep the working environment clean and less at risk to link the AWS to the outside world.


3. Enable Tracking and Alerting
AWS comes with some unique set of tools that allows its user to keep track of working information. The AWS Cloudtrail is a cloud tool that enforces the compliance of AWS.

It’s apparent that the right deployment of Security Groups and Network access control lists will go a long way in providing first and second layer form of security for an AWS account.

## Network ACLs
A network access control list (ACL) is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets. You might set up network ACLs with rules similar to your security groups in order to add an additional layer of security to your VPC. 
Network ACL basics
The following are the basic things that you need to know about network ACLs:

Your VPC automatically comes with a modifiable default network ACL. By default, it allows all inbound and outbound IPv4 traffic and, if applicable, IPv6 traffic.

You can create a custom network ACL and associate it with a subnet. By default, each custom network ACL denies all inbound and outbound traffic until you add rules.

Each subnet in your VPC must be associated with a network ACL. If you don't explicitly associate a subnet with a network ACL, the subnet is automatically associated with the default network ACL.

You can associate a network ACL with multiple subnets. However, a subnet can be associated with only one network ACL at a time. When you associate a network ACL with a subnet, the previous association is removed.

A network ACL contains a numbered list of rules. We evaluate the rules in order, starting with the lowest numbered rule, to determine whether traffic is allowed in or out of any subnet associated with the network ACL. The highest number that you can use for a rule is 32766. We recommend that you start by creating rules in increments (for example, increments of 10 or 100) so that you can insert new rules where you need to later on.

A network ACL has separate inbound and outbound rules, and each rule can either allow or deny traffic.

Network ACLs are stateless, which means that responses to allowed inbound traffic are subject to the rules for outbound traffic (and vice versa).

There are quotas (limits) for the number of network ACLs per VPC, and the number of rules per network ACL. For more information, see Amazon VPC quotas.