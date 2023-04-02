#!/usr/bin/env python3
import os

import aws_cdk as cdk

# from aws_cdk import core as core


# from nested_stack.nested_stack_stack import NestedStackStack
from nested_stack.skeleton_stack import SkeletonStack
from nested_stack.app_stack import AppStack

app = cdk.App()

main_stack = cdk.Stack(app, 'MainStack', env={'account': '860278712199','region': 'us-west-2'})

skeleton = SkeletonStack(main_stack, 'skeleton')

ec2_app = AppStack(main_stack, 'App', vpc=skeleton.vpc)

# NestedStackStack(app, "NestedStackStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=cdk.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    # )

app.synth()
