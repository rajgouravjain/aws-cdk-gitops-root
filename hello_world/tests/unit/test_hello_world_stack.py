import json
import pytest

from aws_cdk import App, Stack
from constructs import Construct

from aws_cdk import aws_s3 as s3
from aws_cdk import aws_sqs as sqs
from aws_cdk import aws_sns as sns

from hello_world.hello_world_stack  import HelloWorldStack


def get_template():
    app = App()
    HelloWorldStack(app, "helloworldstack")
    return json.dumps(app.synth().get_stack_by_name("helloworldstack").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
