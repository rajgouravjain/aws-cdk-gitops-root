import json
import pytest
import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_cdk import App, Stack
from constructs import Construct
from aws_cdk.assertions import Match, Template

from aws_cdk import aws_s3 as s3
from aws_cdk import aws_sqs as sqs
from aws_cdk import aws_sns as sns

from composed_world.composed_world_construct  import ComposedWorld


def get_template():
    stack = Stack()
    cc = ComposedWorld(stack,"composedconstruct",prefix="images")
    return json.dumps(Template.from_stack(stack).to_json())


def test_sqs_queue_created():
    assert("AWS::S3::Bucket" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())

