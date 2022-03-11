import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ssm as ssm
)
from constructs import Construct

class TechgroundsprojectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        self.vpc1 = ec2.Vpc(self, 'APP-PROD-VPC',
             cidr = '10.10.10.0/24',
             max_azs = 2,
             subnet_configuration=[
                 ec2.SubnetConfiguration(
                     name = 'Public-Subnet',
                     subnet_type = ec2.SubnetType.PUBLIC,
                     cidr_mask = 26
                 )
             ])

        self.vpc2 = ec2.Vpc(self, 'Management-PROD-VPC',
             cidr = '10.20.20.0/24',
             max_azs = 2,
             subnet_configuration=[
                 ec2.SubnetConfiguration(
                     name = 'Public-Subnet',
                     subnet_type = ec2.SubnetType.PUBLIC,
                     cidr_mask = 26
                 )
             ])            
        self.cfn_VPCPeering_connection = ec2.CfnVPCPeeringConnection(self, "MyCfnVPCPeeringConnection",
        peer_vpc_id = self.vpc1.vpc_id,
        vpc_id = self.vpc2.vpc_id,

             # the properties below are optional
        peer_region='eu-central-1',
        )

        #AMI
        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE 
        )

        windows_server = ec2.MachineImage.latest_windows(
            ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE
           
        )

        # Instance
        Instance = ec2.Instance(self, 'Webserver',
            instance_type=ec2.InstanceType('t2.micro'),
            machine_image=amzn_linux,
            vpc = self.vpc1)

        Instance1 = ec2.Instance(self, 'Management Server',
            instance_type=ec2.InstanceType('t2.micro'),
            machine_image=windows_server,
            vpc = self.vpc2)    
