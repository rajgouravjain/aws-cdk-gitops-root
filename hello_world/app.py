#!/usr/bin/env python3
import os

import aws_cdk as cdk

from hello_world.hello_world_stack import HelloWorldStack

env_IN = cdk.Environment(account="600290073582", region="ap-south-1")

app = cdk.App()
HelloWorldStack(app, "HelloWorldStack",env=env_IN)

app.synth()
