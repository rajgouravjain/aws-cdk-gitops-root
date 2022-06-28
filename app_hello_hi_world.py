#!/usr/bin/env python3
import os

import aws_cdk as cdk

from hi_world.hi_world_stack import HiWorldStack
from hello_world.hello_world_stack import HelloWorldStack


app = cdk.App()
HiWorldStack(app, "HiWorldStack")
HelloWorldStack(app,"HelloWorldStack")

app.synth()
