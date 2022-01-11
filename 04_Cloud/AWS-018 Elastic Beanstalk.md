# AWS Elastic Beanstalk 
AWS Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS.

You can simply upload your code and Elastic Beanstalk automatically handles the deployment, from capacity provisioning, load balancing, auto-scaling to application health monitoring. At the same time, you retain full control over the AWS resources powering your application and can access the underlying resources at any time.

There is no additional charge for Elastic Beanstalk - you pay only for the AWS resources needed to store and run your applications.

## Benefits
###  **Fast and simple to begin**

Elastic Beanstalk is the fastest and simplest way to deploy your application on AWS. You simply use the AWS Management Console, a Git repository, or an integrated development environment (IDE) such as Eclipse or Visual Studio to upload your application, and Elastic Beanstalk automatically handles the deployment details of capacity provisioning, load balancing, auto-scaling, and application health monitoring. Within minutes, your application will be ready to use without any infrastructure or resource configuration work on your part.

### **Developer productivity**

Elastic Beanstalk provisions and operates the infrastructure and manages the application stack (platform) for you, so you don't have to spend the time or develop the expertise. It will also keep the underlying platform running your application up-to-date with the latest patches and updates. Instead, you can focus on writing code rather than spending time managing and configuring servers, databases, load balancers, firewalls, and networks.

### **Impossible to outgrow**

Elastic Beanstalk automatically scales your application up and down based on your application's specific need using easily adjustable Auto Scaling settings. For example, you can use CPU utilization metrics to trigger Auto Scaling actions. With Elastic Beanstalk, your application can handle peaks in workload or traffic while minimizing your costs.

### **Complete resource control**

You have the freedom to select the AWS resources, such as Amazon EC2 instance type and processor type to run the workload on, that are optimal for your application. You also retain full control over the AWS resources powering your application. If you decide you want to take over some (or all) of the elements of your infrastructure, you can do so seamlessly by using Elastic Beanstalk's management capabilities.

## Key-terms
* (EB CLI) - Elastic Beanstalk command line interface -The EB CLI is a command line interface for AWS Elastic Beanstalk that provides interactive commands that simplify creating, updating and monitoring environments from a local repository. Use the EB CLI as part of your everyday development and testing cycle as an alternative to the Elastic Beanstalk console.

*  Runtime - The programming language-specific runtime software (framework, libraries, interpreter, vm, etc.) required to run your application code.

* Elastic Beanstalk Components - 
Software components that Elastic Beanstalk adds to a platform to enable Elastic Beanstalk functionality. For example, the enhanced health agent is necessary for gathering and reporting health information.

* Platform - A combination of an operating system (OS), runtime, web server, application server, and Elastic Beanstalk components. Platforms provide components that are available to run your application.

* Platform Version - 
A combination of specific versions of an operating system (OS), runtime, web server, application server, and Elastic Beanstalk components. You create an Elastic Beanstalk environment based on a platform version and deploy your application to it.

   A platform version has a semantic version number of the form X.Y.Z, where X is the major version, Y is the minor version, and Z is the patch version.

* Platform Branch - A line of platform versions sharing specific (typically major) versions of some of their components, such as the operating system (OS), runtime, or Elastic Beanstalk components. For example: Python 3.6 running on 64bit Amazon Linux; IIS 10.0 running on 64bit Windows Server 2016. Each successive platform version in the branch is an update to the previous one.

* Platform Update - A release of new platform versions that contain updates to some components of the platform—OS, runtime, web server, application server, and Elastic Beanstalk components. Platform updates follow semantic version taxonomy, and can have several levels:

  - Major update – An update that has changes that are incompatible with existing platform versions. You might need to modify your application to run correctly on a new major version. A major update has a new major platform version number.

  - Minor update – An update that adds functionality that is backward compatible with an existing platform version. You don't need to modify your application to run correctly on a new minor version. A minor update has a new minor platform version number.

  - Patch update – An update that consists of maintenance releases (bug fixes, security updates, and performance improvements) that are backward compatible with an existing platform version. A patch update has a new patch platform version number.

* Managed Updates - An Elastic Beanstalk feature that automatically applies patch and minor updates to the operating system (OS), runtime, web server, application server, and Elastic Beanstalk components for an Elastic Beanstalk supported platform version. A managed update applies a newer platform version in the same platform branch to your environment. You can  configure managed updates to apply only patch updates, or minor and patch updates. You can also disable managed updates completely


## Opdracht

18.1 What does it mean by AWS Elastic Beanstalk ?

18.2 How does AWS Elastic Beanstalk fit or replace in a classic setting?

18.3 How can I combine AWS Elastic Beanstalk with other services?

18.4 What is the difference between AWS Elastic Beanstalk and other similar services?


### Gebruikte bronnen
[https://aws.amazon.com/elasticbeanstalk/
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/GettingStarted.CreateApp.html
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/platforms-glossary.html]

### Ervaren problemen
No issues experienced

## Resultaat

### 18.1 What does it mean by AWS Elastic Beanstalk ?

Answer provided in introduction already.

### 18.2 How does AWS Elastic Beanstalk fit or replace in a classic setting?

AWS Elastic Beanstalk automates the details of capacity provisioning, load balancing, auto scaling, and application deployment, creating an environment that runs a version of your application. You can simply upload your deployable code (e.g., WAR file), and AWS Elastic Beanstalk does the rest. The AWS Toolkit for Visual Studio and the AWS Toolkit for Eclipse allow you to deploy your application to AWS Elastic Beanstalk and manage it without leaving your IDE. Once your application is running, Elastic Beanstalk automates management tasks–such as monitoring, application version deployment, a basic health check–and facilitates log file access. By using Elastic Beanstalk, developers can focus on developing their application and are freed from deployment-oriented tasks, such as provisioning servers, setting up load balancing, or managing scaling.



### 18.3 How can I combine AWS Elastic Beanstalk with other services?

To run the  application on AWS resources, Elastic Beanstalk takes the following actions. They take about five minutes to complete.

1. Creates an Elastic Beanstalk application named getting-started-app.

2. Launches an environment named GettingStartedApp-env with these AWS resources:

* An Amazon Elastic Compute Cloud (Amazon EC2) instance (virtual machine)

* An Amazon EC2 security group

* An Amazon Simple Storage Service (Amazon S3) bucket

* Amazon CloudWatch alarms

* An AWS CloudFormation stack

* A domain name

### 18.4 What is the difference between AWS Elastic Beanstalk and other similar services?

Most existing application containers or platform-as-a-service solutions, while reducing the amount of programming required, significantly diminish developers’ flexibility and control. Developers are forced to live with all the decisions predetermined by the vendor–with little to no opportunity to take back control over various parts of their application’s infrastructure. However, with AWS Elastic Beanstalk, developers retain full control over the AWS resources powering their application. If developers decide they want to manage some (or all) of the elements of their infrastructure, they can do so seamlessly by using Elastic Beanstalk’s management capabilities.
