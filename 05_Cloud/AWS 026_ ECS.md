# Amazon Elastic Container Service (Amazon ECS
Amazon ECS is a fully managed container orchestration service that helps you easily deploy, manage, and scale containerized applications. It deeply integrates with the rest of the AWS platform to provide a secure and easy-to-use solution for running container workloads in the cloud and now on your infrastructure with Amazon ECS Anywhere.

## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

## Opdracht

26.1 What does it mean by Amazon ECS ?

26.2 How does Amazon ECS fit or replace in a classic setting?

26.3 How can I combine Amazon ECS with other services?

26.4 What is the difference between Amazon ECS and other similar services?

### Gebruikte bronnen
https://aws.amazon.com/ecs/faqs/

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat

**26.1 What does it mean by Amazon ECS ?**

![ECSWork](/00_includes/Cloud/AmazonECS.png)

**26.2 How does Amazon ECS fit or replace in a classic setting?**

**26.3 How can I combine Amazon ECS with other services?**

* With Fargate, the concept of server provisioning, cluster management, and orchestration completely goes away. Amazon ECS uses containers provisioned by Fargate to automatically scale, load balance, and manage scheduling of your containers for availability, providing an easier way to build and operate containerized applications.


**26.4 What is the difference between Amazon ECS and other similar services?**

* Difference between Amazon ECS & AWS Lambda

Amazon ECS is a highly scalable Docker container management service that allows you to run and manage distributed applications that run in Docker containers. AWS Lambda is an event-driven task compute service that runs your code in response to “events” such as changes in data, website clicks, or messages from other AWS services without you having to manage any compute infrastructure.

* Difference between Amazon ECS & AWS Elastic Beanstalk

AWS Elastic Beanstalk is an application management platform that helps customers easily deploy and scale web applications and services. It keeps the building block provisioning (e.g., EC2, Amazon RDS, Elastic Load Balancing, AWS Auto Scaling, and Amazon CloudWatch), application deployment, and health monitoring abstracted from the user so they can focus on writing code. You simply specify which container images to  deploy, the CPU and memory requirements, the port mappings, and the container links.
Elastic Beanstalk will automatically handle all the details such as provisioning an Amazon ECS cluster, balancing load, auto-scaling, monitoring, and container placement across your cluster. Elastic Beanstalk is ideal if you want to leverage the benefits of containers withthe simplicity of deploying applications from development to production by uploading a container image. You can work with Amazon ECS directly if you want more fine-grained control for custom application architectures.
