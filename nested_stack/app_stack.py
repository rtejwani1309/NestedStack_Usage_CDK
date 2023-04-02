from aws_cdk import (
    NestedStack as NestedStack,
    aws_ec2 as ec2,
)

from constructs import Construct

class AppStack (NestedStack):
    def __init__(self, scope: Construct, id: str, vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        ec2.Instance(
            self,
            f'{id}Ec2Instance',
            instance_type=ec2.InstanceType('t2.micro'),
            machine_image=ec2.MachineImage.generic_linux(
                ami_map={
                    'us-west-2': 'ami-0efa651876de2a5ce'
                }
            ),
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(subnet_group_name='public')
        )