In order to have a new account from which to control this whole project,
I chose to create an AWS Organization.

AWS Organizations is an account management service that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage. AWS Organizations includes account management and consolidated billing capabilities that enable you to better meet the budgetary, security, and compliance needs of your business. As an administrator of an organization, you can create accounts in your organization and invite existing accounts to join the organization.

To create multiple AWS accounts, you first need to set up an AWS Organization. To do this, I went to AWS Organizations in the Services window of the AWS Console, and clicked “Create an Organization”.

>> Image

Once I had created the Organization, I created a couple of nested Organizational Units to group the AWS accounts in. This was done by clicking on the checkbox next to the Root Organization, and then selecting Actions > Organizational Unit > Create New. I created this structure:

>> Image

AWS Organizations features
- Centralized management of all of your AWS accounts
- Consolidated billing for all member accounts
- Hierarchical grouping of your accounts to meet your budgetary, security, or compliance needs
- Policies to centralize control over the AWS services and API actions that each account can access
- Policies to standardize tags across the resources in your organization's accounts
- Policies to control how AWS artificial intelligence (AI) and machine learning services can collect and store data.
- Policies that configure automatic backups for the resources in your organization's accounts
- Integration and support for AWS Identity and Access Management (IAM)
- Integration with other AWS services
- Global access
- Data replication that is eventually consistent
- Free to use

Resources:
[Set Up Multi-Account AWS Environment that Uses Best Practices for AWS Organizations](https://www.youtube.com/watch?v=uOrq8ZUuaAQ)
[Docs - What is AWS Organizations?](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
[Sharing Credits between Accounts](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/useconsolidatedbilling-credits.html#credit-sharing)

Source: [LinuxTek article on AWS Orgs](https://www.linuxtek.ca/2023/02/07/aws-cloud-project-boot-camp-week-0-tips-and-tricks/#Creating_an_AWS_Organization)