# Amazon CloudWatch
Amazon CloudWatch is a monitoring and observability service built for DevOps engineers, developers, site reliability engineers (SREs), IT managers, and product owners. CloudWatch provides you with data and actionable insights to monitor your applications, respond to system-wide performance changes, and optimize resource utilization. CloudWatch collects monitoring and operational data in the form of logs, metrics, and events. You get a unified view of operational health and gain complete visibility of your AWS resources, applications, and services running on AWS and on-premises. You can use CloudWatch to detect anomalous behavior in your environments, set alarms, visualize logs and metrics side by side, take automated actions, troubleshoot issues, and discover insights to keep your applications running smoothly.


### Benefits
* **Use a single platform for observability**
Modern applications, such as those running on microservices architectures, generate large volumes of data in the form of metrics, logs, and events. Amazon CloudWatch allows you to collect, access, and correlate this data on a single platform from across all your AWS resources, applications, and services running on AWS and on-premises, helping you break down data silos to gain system-wide visibility and quickly resolve issues.
* **Collect metrics on AWS and on premises**
Monitoring your AWS resources and applications is easy with CloudWatch. It natively integrates with more than 70 AWS services, such as Amazon EC2, Amazon DynamoDB, Amazon S3, Amazon ECS, Amazon EKS, and AWS Lambda. It automatically publishes detailed one-minute metrics and custom metrics with up to one-second granularity so you can dive deep into your logs for additional context. You can also use CloudWatch in hybrid environments by using the CloudWatch Agent or API to monitor your on-premises resources.
* **Improve operational performance and resource optimization**
Set alarms and automate actions based on predefined thresholds or on machine learning (ML) algorithms that identify anomalous behavior in your metrics. For example, you can start Amazon EC2 Auto Scaling automatically or stop an instance to reduce billing overages. You can also use CloudWatch Events for serverless to trigger workflows with services like AWS Lambda, Amazon SNS, and AWS CloudFormation.
* **Get operational visibility and insight**
To optimize performance and resource utilization, you need a unified operational view, real-time granular data, and historical reference. CloudWatch provides automatic dashboards, data with one-second granularity, and up to 15 months of metrics storage and retention. You can also perform metric math on your data to derive operational and utilization insights; for example, you can aggregate usage across an entire fleet of EC2 instances.
* **Derive actionable insights from logs**
Explore, analyze, and visualize your logs so you can troubleshoot operational problems with ease. With CloudWatch Logs Insights, you pay only for the queries you run. It scales with your log volume and query complexity, giving you answers in seconds. In addition, you can publish log-based metrics, create alarms, and correlate logs and metrics together in CloudWatch Dashboards for complete operational visibility.

## Key-terms
* **CloudWatch Log**
Amazon CloudWatch Logs lets you monitor and troubleshoot your systems and applications using your existing system, application and custom log files.

With CloudWatch Logs, you can monitor your logs, in near real time, for specific phrases, values or patterns. For example, you could set an alarm on the number of errors that occur in your system logs or view graphs of latency of web requests from your application logs. You can then view the original log data to see the source of the problem. Log data can be stored and accessed indefinitely in highly durable, low-cost storage so you don’t have to worry about filling up hard drives.

* **Amazon CloudWatch Logs Insights**
Amazon CloudWatch Logs Insights is an interactive, pay-as-you-go, and integrated log analytics capability for CloudWatch Logs. It helps developers, operators, and systems engineers understand, improve, and debug their applications, by allowing them to search and visualize their logs. Logs Insights is fully integrated with CloudWatch, enabling you to manage, explore, and analyze your logs. You can also leverage CloudWatch Metrics, Alarms and Dashboards with Logs to get full operational visibility into your applications. This empowers you to understand your applications, make improvements, and find and fix problems quickly, so that you can continue to innovate rapidly. You can write queries with aggregations, filters, and regular expressions to derive actionable insights from your logs. You can also visualize timeseries data, drill down into individual log events, and export your query results to CloudWatch Dashboards.

* **Amazon CloudWatch Anomaly Detection**
Amazon CloudWatch Anomaly Detection applies machine-learning algorithms to continuously analyze single time series of systems and applications, determine a normal baseline, and surface anomalies with minimal user intervention. It allows you to create alarms that auto-adjust thresholds based on natural metric patterns, such as time of day, day of week, seasonality, or changing trends. You can also visualize metrics with anomaly detection bands on dashboards, monitoring, isolating, and troubleshooting unexpected changes in your metrics.

* **Amazon CloudWatch Contributor Insights**
Amazon CloudWatch now includes Contributor Insights, which analyzes time-series data to provide a view of the top contributors influencing system performance. Once set up, Contributor Insights runs continuously without needing additional user intervention. This helps developers and operators more quickly isolate, diagnose, and remediate issues during an operational event.

* **Amazon CloudWatch ServiceLens**
Amazon CloudWatch ServiceLens is a new feature that enables you to visualize and analyze the health, performance, and availability of your applications in a single place. CloudWatch ServiceLens ties together CloudWatch metrics and logs as well as traces from AWS X-Ray to give you a complete view of your applications and their dependencies. This enables you to quickly pinpoint performance bottlenecks, isolate root causes of application issues, and determine users impacted. CloudWatch ServiceLens enables you to gain visibility into your applications in three main areas: Infrastructure monitoring (using metrics and logs to understand the resources supporting your applications), transaction monitoring (using traces to understand dependencies between your resources), and end user monitoring (using canaries to monitor your endpoints and notify you when your end user experience has degraded).

* ** Custom Metric*

You can use Amazon CloudWatch to monitor data produced by your own applications, scripts, and services. A custom metric is any metric you provide to Amazon CloudWatch. For example, you can use custom metrics as a way to monitor the time to load a web page, request error rates, number of processes or threads on your instance, or amount of work performed by your application. You can get started with custom metrics by using the PutMetricData API, our sample monitoring scripts for Windows and Linux, CloudWatch collectd plugin, as well as a number of applications and tools offered by AWS partners.

## Opdracht
### Gebruikte bronnen
https://aws.amazon.com/cloudwatch/

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat

* CloudWatch gives you actionable insights that help you optimize application performance, manage resource utilization, and understand system-wide operational health. CloudWatch provides up to one-second visibility of metrics and logs data, 15 months of data retention (metrics), and the ability to perform calculations on metrics. This allows you to perform historical analysis for cost optimization and derive real-time insights into optimizing applications and infrastructure resources. You can use CloudWatch Container Insights to monitor, troubleshoot, and alert your containerized applications and microservices. CloudWatch collects, aggregates, and summarizes compute utilization information such as CPU, memory, disk, and network data, as well as diagnostic information such as container restart failures, to help DevOps engineers isolate issues and resolve them quickly. Container Insights gives you insights from container management services such as Amazon ECS for Kubernetes (EKS), Amazon Elastic Container Service (ECS), AWS Fargate, and standalone Kubernetes (k8s)
