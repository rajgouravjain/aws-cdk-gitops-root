#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk import Stack
from constructs import Construct

import aws_cdk.aws_sqs as sqs
from aws_cdk import aws_sns_subscriptions as sns_sub

from composed_world.composed_world_construct import ComposedWorld

class ComposedWorldStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cw = ComposedWorld(self,"ComposedWorld",prefix="images")
        queue = sqs.Queue(self, "NewImagesQueue")
        cw.topic.add_subscription(sns_sub.SqsSubscription(queue))


env_IN = cdk.Environment(account="486391667947", region="ap-south-1")

app = cdk.App()
ComposedWorldStack(app, "ComposedWorldStack",env=env_IN)

app.synth()
