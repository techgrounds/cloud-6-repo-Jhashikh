AWS-02 Pricing
# [AWS Pricing]
[Introduction:
One of the main reasons for moving to the cloud is cost. If done well, public cloud infrastructures can reduce costs significantly compared to traditional data centers. This is done by adopting a pay-as-you-go pricing model and economy of scale.

You pay only for the compute capacity, storage, and outbound data transfer that you use. You never pay for inbound data transfer and data transfer between services within the same region.

AWS lists four advantages of their pricing model:
Pay-as-you-go
Save when you reserve
Pay less when using more
Pay less as AWS grows

When creating a new AWS account, you automatically get a free-tier account for the first 12 months. Some services are free up to a certain limit with a free-tier account.
Other services are always free. However, those services might be integrated with other services for which you have to pay.

The Total Cost of Ownership (TCO) is used to measure how much an infrastructure would cost if it were hosted the traditional way. This is done by measuring capital expenditures (capex). The cloud pricing model allows you to trade capex for variable expenditure. This can reduce cost by not spending money on capacity you don’t need.
]

## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

## Study
- The four advantages of the AWS pricing model.
- AWS free tier for:
-   S3
-   EC2
-   Always free services
-Understand the differences between capex and opex

### Gebruikte bronnen
[https://rnd-solutions.net/2020/01/17/aws-pricing-in-2020-overview-principles-and-examples/.
https://dzone.com/articles/the-cost-of-the-cloud-the-ultimate-aws-pricing-gui
https://aws.amazon.com/pricing/
https://www.exelanz.com/blogs/aws-pricing-performance-security/
https://www.10thmagnitude.com/opex-vs-capex-the-real-cloud-computing-cost-advantage/
https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/how-aws-pricing-works.pdf]

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat
[The four advantages of the AWS pricing model
Principle #1: Pay as You Go  (On-demand)
The Principle: This is the main idea behind AWS - instead of buying or building costly infrastructure, rent it. AWS is dedicated to turning your CapEx expenses into OpEx. It also provides extreme flexibility - you can order 1,000 machines for an hour and then stop them and pay only for those 1,000 machine hours.Pay-as-you-go allows you to easily adapt to changing business needs without overcommitting budgets and improving your responsiveness to changes. With a pay-as-you-go model, you can adapt your business depending on need and not on forecasts, reducing the risk of overprovisioning or missing capacity.

Principle #2: Save When You Reserve
For AWS Compute and AWS Machine Learning, Savings Plans offer savings over On-Demand in exchange for a commitment to use a specific amount (measured in $/hour) of an AWS service or a category of services, for a one- or three-year period.At the core of AWS is its compute service, Amazon EC2. EC2 machine instances are substantially discounted (on the order of 30-50%) if you reserve an instance for 1-3 years in advance. Another option is to use “spot instances” - machine instances that happen to be available at a given time, and will be taken away from you when another user demands them. Switching loads dynamically between spot instances, and helping Amazon manage their demand, can give you even bigger discounts.Amazon provides a lot of price flexibility. You can significantly cut costs by committing to 1 years or more - it’s possible to do this selectively for some workloads, while using others on demand. The spot instances option is a creative one, which lets anyone with expertise, and the time to architect a spot instances solution, shave 60% off costs.You can pay nothing upfront (most expensive), partially upfront (less expensive), or all upfront (least expensive) for your reservatio

Principle #3: Pay Less by Using More
With AWS, you can get volume based discounts and realize important savings as your usage increases. For services such as S3, pricing is tiered, meaning the more you use, the less you pay per GB. AWS also gives you options to acquire services that help you address your business needs.Amazon EC2 offers volume discounts for users who spend more than $500,000 in upfront costs. Amazon also provides a plethora of services and options for most use cases, allowing you to switch to a service that meets your need at a lower cost. For example, there are several AWS backup options including the AWS Backup service and storage services like S3, Glacier, EBS, EFS, etc. Organizations can move data between these storage services to gain efficiencies.Sophisticated users of AWS can save a lot by dynamically moving workloads between services and creating economies of scale.

Principle #4: Pay even less as AWS grows
  As AWS grows,they focus more on reducing data centre hardware costs, improving operational efficiencies, lowering power consumption and the cost of doing business. These optimizations and AWS’s substantial growth, results in savings that is passed on to customers in form of low pricing]

 AWS free tier for:
-   S3 
As part of the AWS Free Tier, you can get started with Amazon S3 for free. Upon sign-up, new AWS customers receive 5GB of Amazon S3 storage in the S3 Standard storage class for 12 months; 20,000 GET Requests; 2,000 PUT, COPY, POST, or LIST Requests; and 100 GB of Data Transfer Out each month.

Your usage for the free tier is calculated each month across all AWS Regions except the AWS GovCloud Region and automatically applied to your bill; unused monthly usage will not roll over. Restrictions apply;.
-   EC2
750 hours per month of Linux, RHEL, or SLES t2.micro or t3.micro instance dependent on region
750 hours per month of Windows t2.micro or t3.micro instance dependent on region
-   Always free services 
These free tier offers do not automatically expire at the end of your 12 month AWS Free Tier term, but are available to both existing and new AWS customers indefinitely.
E.G of Always Free Services are 
- Amazon DynamoDB [ DATABASE ]- Fast and flexible NoSQL database with seamless scalability. 25 GB of Storage ,25 provisioned Write Capacity Units (WCU) ,25 provisioned Read Capacity Units (RCU),Enough to handle up to 200M requests per month
- AWS Lambda [ COMPUTE ] -Compute service that runs your code in response to events and automatically manages the compute resources. 1,000,000 (1 Miliion )free requests per month,Up to 3.2 million seconds of compute time per mont
- Amazon Simple Notification Service (Amazon SNS)[ Mobile] -Fast, flexible, fully managed push messaging service.1,000,000 Publishes,100,000 HTTP/S Deliveries ,1,000 Email Deliveries
- Amazon CloudWatch [ DEVELOPER TOOLS ] -Monitoring for AWS cloud resources and applications - 10 Custom Metrics and 10 Alarm, 1,000,000 API Requests ,5GB of Log Data Ingestion and 5GB of Log Data Archive, 3 Dashboards with up to 50 Metrics Each per Month
- Amazon Chime [BUSINESS PRODUCTIVITY] - Amazon Chime is a modern unified communications service that offers frustration-free meetings with exceptional audio and video -Amazon Chime Basic subscription is free to use for as long you'd like
- Amazon CloudFront [ CONTENT DELIVERY ] - Web service to distribute content to end users with low latency and high transfer speeds.1 TB of Data Transfer Out , 10,000,000 HTTP or HTTPS Requests , 2,000,000 CloudFront Function Invocations
- Amazon Cognito [ SECURITY, IDENTITY, & COMPLIANCE] -Simple and Secure User Sign-Up, Sign-In, and Access Control. - The Your User Pool feature has a Free Tier of 50,000 MAUs each month** , 10 GB of cloud sync storage. Expires 12 months after sign-up.,1,000,000 sync operations per month. Expires 12 months after sign-up

Differences between capex and opex
CapEx is defined as business expenses incurred in order to create long-term benefits in the future, such as purchasing fixed assets like a building or equipment. Some examples of IT items that fall under this category would be whole systems and servers, printers and scanners, or air conditioners and generators. You buy these items once and they benefit your business for many, many years. Maintenance of such items is also considered CapEx, as it extends their lifetime and usefulness. 
OpEx is your operating costs, the expenses to run day-to-day business, like services and consumable items that get used up and are paid for according to use. This includes printer cartridges and paper, electricity, and even yearly services like website hosting or domain registrations. These things are necessary for your business’s success but are not considered major long-term investments like CapEx items
![OpExvsCapEx](../00_includes/Cloud/OpEx-vs-CapEx.jpg)

What is AWS Pricing Calculator?
PDF
RSS
AWS Pricing Calculator lets you explore AWS services and create an estimate for the cost of your use cases on AWS. You can model your solutions before building them, explore the price points and calculations behind your estimate, and find the available instance types and contract terms that meet your needs. This enables you to make informed decisions about using AWS. You can plan your AWS costs and usage or price out setting up a new set of instances and services.

AWS Pricing Calculator is useful both for people who have never used AWS and for users who want to reorganize or expand their AWS usage. You don't need any experience with the cloud or AWS to use AWS Pricing Calculator.

Accessing AWS Pricing Calculator
AWS Pricing Calculator provides only a console interface at https://calculator.aws/#/. It doesn't provide an API.

Prerequisites for using AWS Pricing Calculator
You don't need an AWS account or in-depth knowledge of AWS to use AWS Pricing Calculator.

For best results, we suggest that you have a plan for how you want to use AWS before starting your estimate. For example, decide whether you want to break out your estimate by cost center, by product that you run on AWS, or by regional stacks.

AWS Pricing Calculator Regions
You can use AWS Pricing Calculator to generate monthly cost estimates for all Regions supported by your preferred service. For information about each service's available Regions, see the corresponding service user guide documentation.

Pricing for AWS Pricing Calculator
AWS Pricing Calculator is free for use. It provides an estimate of your AWS fees and charges, but the estimate doesn't include any taxes that might apply to the fees and charges. AWS Pricing Calculator provides pricing details for your information only. If the prices on the marketing page are different from the prices that AWS Pricing Calculator uses, AWS honors the prices from the marketing pages. For more information about AWS service pricing, see Cloud Services Pricing.

The prices that AWS Pricing Calculator uses for the estimates come from the AWS Price List API. For more information about the AWS Price List API, see Using the AWS Price List API in the AWS Billing and Cost Management User Guide.