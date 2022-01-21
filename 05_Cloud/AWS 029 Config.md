# AWS Config
AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. Config continuously monitors and records your AWS resource configurations and allows you to automate the evaluation of recorded configurations against desired configurations. With Config, you can review changes in configurations and relationships between AWS resources, dive into detailed resource configuration histories, and determine your overall compliance against the configurations specified in your internal guidelines. This enables you to simplify compliance auditing, security analysis, change management, and operational troubleshooting.]

### Benefits
* **Continuous monitoring**
With AWS Config, you are able to continuously monitor and record configuration changes of your AWS resources. Config also enables you to inventory your AWS resources, the configurations of your AWS resources, as well as software configurations within EC2 instances at any point in time. Once change from a previous state is detected, an Amazon Simple Notification Service (SNS) notification can be delivered for you to review and take action.
* **Continuous assessment**
AWS Config allows you to continuously audit and assess the overall compliance of your AWS resource configurations with your organization’s policies and guidelines. AWS Config provides you with the ability to define rules for provisioning and configuring AWS resources. These rules can be provisioned independently or packaged together with compliance remediation actions inside a pack (known as a conformance pack) that can be deployed across your entire organization with a single click. Resource configurations or configuration changes that deviate from your rules automatically trigger Amazon Simple Notification Service (SNS) notifications and Amazon CloudWatch events so that you can be alerted on a continuous basis. You can also take advantage of the visual dashboard to check your overall compliance status and quickly spot non-compliant resources.
* **Change management**
With AWS Config, you are able to track the relationships among resources and review resource dependencies prior to making changes. Once a change occurs, you are able to quickly review the history of the resource's configuration and determine what the resource’s configuration looked like at any point in the past. Config provides you with information to assess how a change to a resource configuration would affect your other resources, which minimizes the impact of change-related incidents.
* **Operational troubleshooting**
With AWS Config, you can capture a comprehensive history of your AWS resource configuration changes to simplify troubleshooting of your operational issues. Config helps you identify the root cause of operational issues through its integration with AWS CloudTrail, a service that records events related to API calls for your account. Config leverages CloudTrail records to correlate configuration changes to particular events in your account. You can obtain the details of the event API call that invoked the change (e.g., who made the request, at what time, and from which IP address) from the CloudTrail logs.
* **Enterprise-wide compliance monitoring**
With multi-account, multi-region data aggregation in AWS Config, you can view compliance status across your enterprise and identify non-compliant accounts. You can dive deeper to view status for a specific region or a specific account across regions. You can view this data from the Config console in a central account, removing the need to retrieve this information individually from each account, and each region.
* **Support for third-party resources**
AWS Config is designed to be your primary tool to perform configuration audit and compliance verification of both your AWS and third-party resources. You can publish the configuration of third-party resources such as GitHub repositories, Microsoft Active Directory resources, or any on-premises server into AWS. You can then view and monitor the resource inventory and configuration history using the AWS Config console and APIs, just like you do for AWS resources. You can also create AWS Config rules or conformance packs to evaluate these third-party resources against best practices, internal policies, and regulatory policies.

## Key-terms
* Config Rule :-A Config Rule represents desired configurations for a resource and is evaluated against configuration changes on the relevant resources, as recorded by AWS Config. The results of evaluating a rule against the configuration of a resource are available on a dashboard. Using Config Rules, you can assess your overall compliance and risk status from a configuration perspective, view compliance trends over time and pinpoint which configuration change caused a resource to drift out of compliance with a rule.


* conformance pack :-
A conformance pack is a collection of Config rules and remediation actions that is built using a common framework and packaging model in AWS Config. By packaging the above Config artifacts, you can simplify the deployment and reporting aspects of governance policies and configuration compliance across multiple accounts and regions and reduce the time that a resource is left in a non-compliant state.

* resource’s configuration :-Configuration of a resource is defined by the data included in the Configuration Item (CI) of AWS Config. The initial release of Config rules makes the CI for a resource available to relevant rules. Config rules can use this information along with any other relevant information such as other attached resource, business hours, etc. to evaluate compliance of a resource’s configuration.

* evaluation :- Evaluation of a rule determines whether a rule is compliant with a resource at a particular point in time. It is the result of evaluating a rule against the configuration of a resource. Config rules will capture and store the result of each evaluation. This result will include the resource, rule, time of evaluation and a link to Configuration Item (CI) that caused non-compliance.

## Opdracht
### Gebruikte bronnen
https://aws.amazon.com/config/

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat

![Config](/00_includes/Cloud/Config.png)

### Integrations
* **AWS Organizations**

You can use AWS Organizations to define the accounts to use for AWS Config’s multi-account, multi-region data aggregation capability. AWS Organizations is an account management service that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage. By providing your AWS Organizations details, you can monitor the compliance status across your organization.
* **AWS CloudTrail**

AWS Config integrates with AWS CloudTrail to correlate configuration changes to particular events in your account. You can use the CloudTrail logs to obtain the details of the event that invoked the change, including who made the request, at what time, and from which IP address. You can navigate to the Config timeline from the AWS CloudTrail console to view the configuration changes related to your AWS API activities. To learn more about this feature, read our documentation here.
* **Connect with ITSM / ITOM Software**
IT Service Management (ITSM) tools, such as Jira Service Desk, can connect with AWS Config to make it easier for ITSM platform users to request and manage AWS services and resources. The AWS Service Management Connector for Jira Service Desk provides Jira Service Desk administrators governance and oversight over their AWS products.
* **AWS Security Hub**

AWS Security Hub centralizes security checks from other AWS services, including AWS Config rules. Security Hub enables and controls Config rules to ensure your resource configurations are aligned to best practices. Enable Config on all accounts in all Regions where Security Hub is in order to run security checks on your environment’s resources.
* **AWS Audit Manager**

AWS Audit Manager helps you continuously audit your AWS usage to simplify how you assess risk and compliance with regulations and industry standards. Audit Manager automates evidence collection, so you can configure a control data source, such as AWS Config, to collect automated evidence.
* **AWS Systems Manager**

AWS Config integrates with AWS Systems Manager to record configuration changes to software on your Amazon EC2 instances and servers in your on-premises environment. With this integration, you can gain visibility into operating system (OS) configurations, system-level updates, installed applications, network configuration, and more. Config also provides a history of OS and system-level configuration changes alongside infrastructure configuration changes recorded for EC2 instances. You can navigate to the Config timeline from the Systems Manager console to view the configuration changes of your managed EC2 instances. You can use Config to view AWS Systems Manager Inventory history and track changes for all your managed instances.
* **Amazon Firewall Manager**

To use AWS Firewall Manager, you must enable AWS Config for each of your AWS Organizations member accounts. When new applications are created, Firewall Manager is the single service to build firewall rules, create security policies, and enforce them consistently.
* **Amazon EC2 Dedicated Host**
AWS Config integrates with Amazon EC2 Dedicated Hosts to assess license compliance. Config records when instances are launched, stopped, or terminated on a Dedicated Host, and pairs this information with host and instance level information relevant to software licensing, such as Host ID, Amazon Machine Image (AMI) IDs, number of sockets and physical cores. This enables you to use Config as a data source for your license reporting. You can navigate to the Config timeline from the Amazon EC2 Dedicated Hosts console to view the configuration changes of your Amazon EC2 Dedicated Hosts.
* **Application Load Balancers**

AWS Config integrates with Elastic Load Balancing (ELB) service to record configuration changes to Application Load Balancers. Config also includes relationships with associated EC2 security groups, VPCs, and subnets. You can use this information for security analysis and troubleshooting. For example, you can check which security groups are associated with your application load balancer at any point in time. You can navigate to the Config timeline from the ELB console to view the configuration changes of your Application Load Balancers.