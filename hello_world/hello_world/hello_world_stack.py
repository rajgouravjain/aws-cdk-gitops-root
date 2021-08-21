
from aws_cdk import Stack
from constructs import Construct

from aws_cdk import aws_sqs as sqs
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_sns as sns


class HelloWorldStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        jobs_queue = sqs.Queue(self, "jobs")
        bucket = s3.Bucket(self, "MyFirstBucket", versioned=True)
        topic = sns.Topic(self, "topic")
