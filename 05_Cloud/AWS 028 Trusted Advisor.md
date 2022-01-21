# AWS Trusted Advisor
**AWS Trusted Advisors** provides recommendations that help you follow AWS best practices. Trusted Advisor evaluates your account by using checks. These checks identify ways to optimize your AWS infrastructure, improve security and performance, reduce costs, and monitor service quotas. You can then follow the check recommendations to optimize your services and resources.
AWS Basic Support and AWS Developer Support customers can access core security checks and all checks for service quotas. AWS Business Support and AWS Enterprise Support customers can access all checks, including cost optimization, security, fault tolerance, performance, and service quotas.

## Benefits
Checks from Trusted Advisor analyzes your AWS environment and recommends best practices.
* **Cost optimization**
 
   can help you save cost, such as recommending you to delete unused or idle resources, or use reserved capacity.
* **Performance**

  can improve the performance of your services by ensuring you to take advantage of provisioned throughput, and monitoring for overutilized Amazon EC2 instances.
* **Security**

  can improve the security of your application by recommending you to enable AWS security features, and review your permissions.
* **Fault tolerance**

  can increase the availability of your AWS application by recommending you  to take advantage of auto scaling, health checks, multi-AZ Regions, and backup capabilities.
* **Service quotas**

  Service quotas, also referred to as Service limits, are the maximum number of service resources or operations that apply to an account or a Region. Trusted Advisor can notify you if you use more than 80% of a service quota. You can then follow recommendations to delete resources or request a quota increase. Check results are based on a snapshot, so your current usage might vary.
  ![TrustedAdvisor](/00_includes/Cloud/TrustedAdvisorbestpracticechecks.png)

## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

## Opdracht
### Gebruikte bronnen
https://aws.amazon.com/premiumsupport/technology/trusted-advisor/
https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat

![Trustedadvisorwork](/00_includes/Cloud/AWStrustedadvisor.png)




### Using other AWS services to view Trusted Advisor reports

* create an Amazon Simple Storage Service (Amazon S3) bucket to store your report 

   * Upload the report to Amazon S3

  After you download your resources.json report, upload the file to Amazon S3. You must use a bucket in the US East (N. Virginia) Region.

To upload the report to an Amazon S3 bucket

1. Sign in to the AWS Management Console at https://console.aws.amazon.com/.

2. Use the Region selector and choose the US East (N. Virginia) Region.

3. Open the Amazon S3 console at https://console.aws.amazon.com/s3/.

4. From the list of buckets, choose an S3 bucket, and then copy the name. You use the name in the next procedure.

5. On the bucket-name page, choose Create folder, enter the name folder1, and then choose Save.

6. Choose the folder1.

7. In folder1, choose Upload and choose the resources.json file.

8. Choose Next, keep the default options, and then choose Upload.

Note
If you upload a new report to this bucket, rename the .json files each time you upload them so that you don't override the existing reports. For example, you can add the timestamp to each file, such as resources-timestamp.json, resources-timestamp2.json, and so on
* an AWS CloudFormation template to create resources in your account. 

After you upload your report to Amazon S3, upload the following YAML template to AWS CloudFormation. This template tells AWS CloudFormation what resources to create for your account so that other services can use the report data in the S3 bucket. The template creates resources for IAM, AWS Lambda, and AWS Glue.

**To create your resources with AWS CloudFormation**

1. Download the trusted-advisor-reports-template.zip file.

2. Unzip the file.

3. Open the template file in a text editor.

4. For the BucketName and FolderName parameters, replace the values for your-bucket-name-here and folder1 with the bucket name and folder name in your account.

5. Save the file.

6. Open the AWS CloudFormation console at https://console.aws.amazon.com/cloudformation.

If you haven't already, in the Region selector, choose the US East (N. Virginia) Region.

7. In the navigation pane, choose Stacks.

8. Choose Create stack and choose With new resources (standard).

9. On the Create stack page, under Specify template, choose Upload a template file, and then choose Choose file.

10. Choose the YAML file and choose Next.

11. On the Specify stack details page, enter a stack name such as Organizational-view-Trusted-Advisor-reports, and choose Next.

12. On the Configure stack options page, keep the default options, and then choose Next.

13. On the Review Organizational-view-Trusted-Advisor-reports page, review your options. At the bottom of the page, select the check box for I acknowledge that AWS CloudFormation might create IAM resources.

14. Choose Create stack.

The stack takes about 5 minutes to create.

15. After the stack creates successfully, the Resources tab appears
* use Amazon Athena to analyze or run queries for your report 

After you have your resources, you can view the data in Athena. Use Athena to create queries and analyze the results of the report, such as looking up specific check results for accounts in the organization.
To query the data in Athena

1. Open the Athena console at https://console.aws.amazon.com/athena/.

If you haven't already, in the Region selector, choose the US East (N. Virginia) Region.

2. Choose Saved Queries and in search field, enter Show sample.

3. Choose the query that appears, such as Show sample entries of TA report.

4. Choose Run query. Your query results appear.
* Amazon QuickSight to visualize that data in a dashboard.

You can also set up Amazon QuickSight so that you can view your data in a dashboard and visualize your report information.
To create a dashboard in Amazon QuickSight

Navigate to the Amazon QuickSight console and sign in to your account.

Choose New analysis, New dataset, and then choose Athena.

In the New Athena data source dialog box, enter a data source name such as AthenaTA, and then choose Create data source.
In the Choose your table dialog box, choose the athenatacfn table, choose folder1, and then choose Select.
In the Finish data set creation dialog box, choose Directly query your data, and then choose Visualize.
You can now create a dashboard in Amazon QuickSight

**Find duplicate columns**

You can use the AWS Glue console to view the schema and quickly identify if you have duplicate columns in your report.

To find duplicate columns

Open the AWS Glue console at https://console.aws.amazon.com/glue/.

If you haven't already, in the Region selector, choose the US East (N. Virginia) Region.

In the navigation pane, choose Tables.

Choose your folder name, such as folder1, and then under Schema, view the values for Column name.

If you have a duplicate column, you must upload a new report to your Amazon S3 bucket. See the following Upload a new report section

**Viewing AWS Security Hub controls in AWS Trusted Advisor**
After you enable AWS Security Hub for your AWS account, you can view your security controls and their findings in the Trusted Advisor console. You can use Security Hub controls to identify security vulnerabilities in your account in the same way that you can use Trusted Advisor checks. You can view the check's status, the list of affected resources, and then follow Security Hub recommendations to address your security issues. You can use this feature to find security recommendations from Trusted Advisor and Security Hub in one convenient location.