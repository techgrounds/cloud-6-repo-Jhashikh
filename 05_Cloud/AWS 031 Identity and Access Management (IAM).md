# AWS Identity and Access Management (IAM)
AWS Identity and Access Management (IAM) provides fine-grained access control across all of AWS. With IAM, you can specify who can access which services and resources, and under which conditions. With IAM policies, you manage permissions to your workforce and systems to ensure least-privilege permissions.

IAM is a feature of your AWS account and is offered at no additional charge.

### Use cases
With IAM, you can manage AWS permissions for workforce users and workloads. For workforce users, we recommend that you use AWS Single Sign-On (AWS SSO) to manage access to AWS accounts and permissions within those accounts. AWS SSO makes it easier to provision and manage IAM roles and policies across your AWS organization. For workload permissions, use IAM roles and policies, and grant only the required access for your workloads.

* **Apply fine-grained access control**
Grant access to specific AWS service APIs and resources by using IAM policies. You also can define specific conditions in which access is granted, such as granting access to identities from a specific AWS organization or access through a specific AWS service. 
* **Establish permissions guardrails and data perimeters across your AWS organization**
With AWS Organizations, you can use service control policies (SCPs) to establish permissions guardrails that all IAM users and roles in an organization’s accounts adhere to. Whether you’re just getting started with SCPs or have existing SCPs, you can use IAM access advisor to help you restrict permissions confidently.
* **Achieve least-privilege permissions with IAM Access Analyzer**
Achieving least privilege is a continuous cycle to grant the right fine-grained permissions as your requirements evolve. IAM Access Analyzer helps you streamline permissions management as you set, verify, and refine permissions.
* **Automatically scale fine-grained permissions with ABAC**
Attribute-based access control (ABAC) is an authorization strategy for creating fine-grained permissions based on user attributes, such as department, job role, and team name. With ABAC, you can reduce the number of distinct permissions you need for creating fine-grained controls in your AWS account.

## Key-terms
 * **IAM role**
 An IAM role is an IAM entity that defines a set of permissions for making AWS service requests. IAM roles are not associated with a specific user or group. Instead, trusted entities assume roles, such as IAM users, applications, or AWS services such as EC2.

* **user**
A user is a unique identity recognized by AWS services and applications. Similar to a login user in an operating system like Windows or UNIX, a user has a unique name and can identify itself using familiar security credentials such as a password or access key. A user can be an individual, system, or application requiring access to AWS services. IAM supports users (referred to as "IAM users") managed in AWS's identity management system, and it also enables you to grant access to AWS resources for users managed outside of AWS in your corporate directory (referred to as "federated users").


## Opdracht
### Gebruikte bronnen
https://aws.amazon.com/iam/

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat
How it works
With IAM, you define who can access what by specifying fine-grained permissions. IAM then enforces those permissions for every request. Access is denied by default and access is granted only when permissions specify an "Allow."
![IAM](/00_includes/Cloud/IAM.jpg)
