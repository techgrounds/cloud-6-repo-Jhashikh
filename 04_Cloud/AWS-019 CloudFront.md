# Amazon CloudFront
Amazon CloudFront is a content delivery network (CDN) service built for high performance, security, and developer convenience.

Amazon CloudFront is a web service that speeds up distribution of your static and dynamic web content, such as .html, .css, .js, and image files, to your users. CloudFront delivers your content through a worldwide network of data centers called edge locations. When a user requests content that you're serving with CloudFront, the request is routed to the edge location that provides the lowest latency (time delay), so that content is delivered with the best possible performance.

  * If the content is already in the edge location with the lowest latency, CloudFront delivers it immediately.

  * If the content is not in that edge location, CloudFront retrieves it from an origin that you've defined—such as an Amazon S3 bucket, a MediaPackage channel, or an HTTP server (for example, a web server) that you have identified as the source for the definitive version of your content.

## Use cases
**Deliver fast, secure websites**

Reach viewers across the globe in milliseconds with built-in data compression, edge compute capabilities, and field-level encryption.

**Accelerate dynamic content delivery and APIs**

Optimize dynamic web content delivery with the purpose-built and feature-rich AWS global network infrastructure supporting edge termination and WebSockets.

**Stream live and on-demand video**

Start streams quickly, play them with consistency, and deliver high-quality video to any device with AWS Media Service and AWS Elemental integration.
 
**Distribute patches and updates**

Scale automatically to deliver software, game patches, and IoT over-the-air (OTA) updates at scale with high transfer rates.

## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

## Opdracht

19.1 What is cloudfront?

19.2 How does cloudfront fit or replace in a classic setting?

19.3 How can I combine Cloudfront with other services?

19.4 What is the difference between Cloudfront and other similar services?

### Gebruikte bronnen
https://aws.amazon.com/cloudfront/
https://app.mindmup.com/
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html
https://aws.amazon.com/cloudfront/faqs/
https://www.cloudzero.com/blog/amazon-elasticache




### Ervaren problemen
No issues faced.

### Resultaat

### 19.1 What is cloudfront?
Explained in introduction

![Cloudfront](/00_includes/Cloud/Cloudfront.png)

### 19.2 How does cloudfront fit or replace in a classic setting?

As an example, suppose that you're serving an image from a traditional web server, not from CloudFront. For example, you might serve an image, sunsetphoto.png, using the URL http://example.com/sunsetphoto.png.

Your users can easily navigate to this URL and see the image. But they probably don't know that their request is routed from one network to another—through the complex collection of interconnected networks that comprise the internet—until the image is found.

CloudFront speeds up the distribution of your content by routing each user request through the AWS backbone network to the edge location that can best serve your content. Typically, this is a CloudFront edge server that provides the fastest delivery to the viewer. Using the AWS network dramatically reduces the number of networks that your users' requests must pass through, which improves performance. Users get lower latency—the time it takes to load the first byte of the file—and higher data transfer rates.

You also get increased reliability and availability because copies of your files (also known as objects) are now held (or cached) in multiple edge locations around the world.

Amazon CloudFront lets you quickly obtain the benefits of high performance content delivery without negotiated contracts or high prices. Amazon CloudFront gives all developers access to inexpensive, pay-as-you-go pricing – with a self-service model. Developers also benefit from tight integration with other Amazon Web Services. The solution is simple to use with Amazon S3, Amazon EC2, and Elastic Load Balancing as origin servers, giving developers a powerful combination of durable storage and high performance delivery. Amazon CloudFront also integrates with Amazon Route 53 and AWS CloudFormation for further performance benefits and ease of configuration.

### 19.3 How can I combine Cloudfront with other services?

**Protection against Network and Application Layer Attacks**

Amazon CloudFront, AWS Shield, AWS Web Application Firewall (WAF), and Amazon Route 53 work seamlessly together to create a flexible, layered security perimeter against multiple types of attacks including network and application layer DDoS attacks. All of these services co-reside at the AWS edge and provide a scalable, reliable, and high-performance security perimeter for applications and content. With CloudFront as the “front door” to an application and infrastructure, the primary attack surface is moved away from critical content, data, code and infrastructure

**SSL/TLS Encryptions and HTTPS**

With Amazon CloudFront, content, APIs or applications can be delivered over HTTPS using the latest version Transport Layer Security (TLSv1.3) to encrypt and secure communication between viewer clients and CloudFront. AWS Certificate Manager (ACM) can be used to easily create a custom SSL certificate and deploy to an CloudFront distribution for free. ACM automatically handles certificate renewal, eliminating the overhead and costs of a manual renewal process. Additionally, CloudFront provides a number of TLS optimizations and advanced capabilities such as full/half bridge HTTPS connections, OCSP stapling, Session Tickets, Perfect Forward Secrecy, TLS Protocol Enforcements and Field-Level Encryption.

**Cloudfront setup to deliver our content**

When we configure Cloudfront to deliver our content, we specify origin servers, like an Amazon S3 bucket or your own HTTP server, from which CloudFront gets your files which will then be distributed from CloudFront edge locations all over the world.

**Enabling redundancy for origins**

CloudFront supports multiple origins for backend architecture redundancy. CloudFront’s native origin failover capability automatically serves content from a backup origin when the primary origin is unavailable. The origins set up with origin failover can be any combination of AWS origins like EC2 instances, Amazon S3 buckets, or Media Services, or non-AWS origins like an on-premises HTTP server. Additionally, you can implement advanced origin failover capabilities with CloudFront and Lambda@Edge.

**Edge Computing**

Amazon CloudFront offers programmable and secure edge CDN computing capabilities through CloudFront Functions and AWS Lambda@Edge.

**Real-time Metrics**

Amazon CloudFront is integrated with Amazon CloudWatch, and automatically publishes six operational metrics per distribution, which are displayed in a set of graphs in the CloudFront console. Additional, granular metrics are available with simple click on the console or via API.

**Standard and Real-time Logging**

CloudFront provides two ways to log the requests delivered from your distributions: Standard logs and Real-time logs. 

Standard logs are delivered to the Amazon S3 bucket of your choice (log records are delivered within minutes of a viewer request). 

 CloudFront real-time logs are delivered to the data stream of your choice in Amazon Kinesis Data Streams (log records are delivered within seconds of a viewer request). You can choose the sampling rate for your real-time logs—that is, the percentage of requests for which you want to receive real-time log records. 

 ### 19.4 What is the difference between Cloudfront and other similar services?

 **Difference between CloudFront & Amazon S3**

Amazon S3 is a Simple Storage Service, this can be used large amount of information i.e. Videos, Images, PDF etc. CloudFront is a Content Delivery Network, which is closer to the end user and is used to make the information available on Amazon S3 in the least possible time

**difference between ElastiCache and CloudFront**

While AWS ElastiCache and AWS CloudFront are both caching solutions, their individual approaches and overall framework differ greatly. 

ElastiCache, for starters, enhances the performance of web applications by quickly retrieving information from fully-managed in-memory data stores. It utilizes Memcached and Redis, and manages to considerably reduce the time your applications would, otherwise, take to read data from disk-based databases. 

Amazon CloudFront seeks to boost the performance of web applications too. But, unlike ElastiCache, it acts as a Content Delivery Network (CDN) — which speeds up the delivery of web-based assets through endpoint caches that are positioned close to the traffic source. In other words, your web visitors load content from the closest caching server, instead of relying entirely on the original hosting server. 


