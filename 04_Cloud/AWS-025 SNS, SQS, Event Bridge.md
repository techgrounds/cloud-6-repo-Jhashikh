# [Onderwerp]

**Amazon Simple Notification Service (Amazon SNS)** is a fully managed messaging service for both application-to-application (A2A) and application-to-person (A2P) communication.

The A2A pub/sub functionality provides topics for high-throughput, push-based, many-to-many messaging between distributed systems, microservices, and event-driven serverless applications. Using Amazon SNS topics, your publisher systems can fanout messages to a large number of subscriber systems, including Amazon SQS queues, AWS Lambda functions, HTTPS endpoints, and Amazon Kinesis Data Firehose, for parallel processing. The A2P functionality enables you to send messages to users at scale via SMS, mobile push, and email.

**Amazon Simple Queue Service**
Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS eliminates the complexity and overhead associated with managing and operating message-oriented middleware, and empowers developers to focus on differentiating work. Using SQS, you can send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be available. Get started with SQS in minutes using the AWS console, Command Line Interface or SDK of your choice, and three simple commands.

SQS offers two types of message queues. Standard queues offer maximum throughput, best-effort ordering, and at-least-once delivery. SQS FIFO queues are designed to guarantee that messages are processed exactly once, in the exact order that they are sent.

## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

## Opdracht
### Gebruikte bronnen
https://aws.amazon.com/sns
https://aws.amazon.com/sqs/

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat
### Using Amazon SQS with other AWS infrastructure web services
Amazon SQS message queuing can be used with other AWS Services such as Amazon Redshift, Amazon DynamoDB, Amazon Relational Database Service (RDS), Amazon Elastic Compute Cloud (EC2), Amazon Elastic Container Service (ECS), AWS Lambda, and Amazon S3, to make distributed applications more scalable and reliable. Below are some common design patterns:

* Work Queues: Decouple components of a distributed application that may not all process the same amount of work simultaneously.
* Buffer and Batch Operations: Add scalability and reliability to your architecture, and smooth out temporary volume spikes without losing messages or increasing latency.
* Request Offloading: Move slow operations off of interactive request paths by enqueing the request.
* Fanout: Combine SQS with Simple Notification Service (SNS) to send identical copies of a message to multiple queues in parallel.
* Priority: Use separate queues to provide prioritization of work.
* Scalability: Because message queues decouple your processes, it’s easy to scale up the send or receive rate of messages - simply add another process.
* Resiliency: When part of your system fails, it doesn’t need to take the entire system down. Message queues decouple components of your system, so if a process that is reading messages from the queue fails, messages can still be added to the queue to be processed when the system recovers.

### Benefits of Amazon SQS over homegrown or packaged message queuing systems

Amazon SQS provides several advantages over building your own software for managing message queues or using commercial or open-source message queuing systems that require significant up-front time for development and configuration. 
These alternatives require ongoing hardware maintenance and system administration resources. The complexity of configuring and managing these systems is compounded by the need for redundant storage of messages that ensures messages are not lost if hardware fails.

In contrast, Amazon SQS requires no administrative overhead and little configuration. Amazon SQS works on a massive scale, processing billions of messages per day. You can scale the amount of traffic you send to Amazon SQS up or down without any configuration. Amazon SQS also provides extremely high message durability, giving you and your stakeholders added confidence.
