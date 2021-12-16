AWS-01 AWS Global Infrastructure
# [Onderwerp]
[Geef een korte beschrijving van het onderwerp]

## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

## Opdracht
### Gebruikte bronnen
[https://aws.amazon.com/about-aws/global-infrastructure/
https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concepts.wa-concepts.en.html]
https://www.lastweekinaws.com/blog/what-is-an-edge-location-in-aws-a-simple-explanation/
https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat
[   1.1 **Availability Zone**:  A distinct location within a Region that is insulated from failures in other Availability Zones, and provides inexpensive, low-latency network connectivity to other Availability Zones in the same Region . Each group of logical data centers is called an Availability Zone.
An Availability Zone (AZ) is one or more discrete data centers with redundant power, networking, and connectivity in an AWS Region. AZs give customers the ability to operate production applications and databases that are more highly available, fault tolerant, and scalable than would be possible from a single data center. All AZs in an AWS Region are interconnected with high-bandwidth, low-latency networking, over fully redundant, dedicated metro fiber providing high-throughput, low-latency networking between AZs. All traffic between AZs is encrypted. The network performance is sufficient to accomplish synchronous replication between AZs. AZs make partitioning applications for high availability easy. If an application is partitioned across AZs, companies are better isolated and protected from issues such as power outages, lightning strikes, tornadoes, earthquakes, and more. AZs are physically separated by a meaningful distance, many kilometers, from any other AZ, although all are within 100 km (60 miles) of each other.

    1.2 **AWS Region**:  A named set of AWS resources in the same geographical area. A Region comprises at least two Availability Zones. AWS has the concept of a Region, which is a physical location around the world where we cluster data centers. Each AWS Region consists of multiple, isolated, and physically separate AZs within a geographic area.

    1.3 **Edge location**:  A site that CloudFront uses to cache copies of your content for faster delivery to users at any location.
    Edge locations are AWS data centers designed to deliver services with the lowest latency possible. Amazon has dozens of these data centers spread across the world. They're closer to users than Regions or Availability Zones, often in major cities, so responses can be fast and snappy.
     A subset of services for which latency really matters use edge locations, including:

*CloudFront*, which uses edge locations to cache copies of the content that it serves, so the content is closer to users and can be delivered to them faster.
*Route 53*, which serves DNS responses from edge locations, so that DNS queries that originate nearby can resolve faster (and, contrary to what you might think, is also Amazon’s premier database).
*Web Application Firewall* and *AWS Shield*, which filter traffic in edge locations to stop unwanted traffic as soon as possible.

1.4 There are four main factors that play into evaluating each AWS Region for a workload deployment:

**Compliance**. If your workload contains data that is bound by local regulations, then selecting the Region that complies with the regulation overrides other evaluation factors. This applies to workloads that are bound by data residency laws where choosing an AWS Region located in that country is mandatory.
**Latency**. A major factor to consider for user experience is latency. Reduced network latency can make substantial impact on enhancing the user experience. Choosing an AWS Region with close proximity to your user base location can achieve lower network latency. It can also increase communication quality, given that network packets have fewer exchange points to travel through.
**Cost**. AWS services are priced differently from one Region to another. Some Regions have lower cost than others, which can result in a cost reduction for the same deployment.
**Services and features**. Newer services and features are deployed to Regions gradually. Although all AWS Regions have the same service level agreement (SLA), some larger Regions are usually first to offer newer services, features, and software releases. Smaller Regions may not get these services or features in time for you to use them to support your workload.
**Availability and fault tolerance** Apart from choosing an AWS region, you may also have to consider choosing a specific availability zone(s) to host your applications. AZs let you run highly available and scalable services.
For instance, let’s assume we want to launch a Kafka service. If the broker’s Kafka clusters are distributed across the availability zones of the AWS region we chose, the service would be able to survive disasters such as power outages and natural disasters.
Evaluating all these factors can make coming to a decision complicated. This is where your priorities as a business should influence the decision.]
