
from aws_cdk import Stack
from constructs import Construct

from aws_cdk import aws_sqs as sqs
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_sns as sns

from aws_cdk import aws_s3_notifications as s3notify

class ComposedWorld(Construct):
    def __init__(self, scope: Construct, construct_id: str, prefix=None, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        bucket = s3.Bucket(self, "my_first_bucket", versioned=True)
        self.topic = sns.Topic(self, "topic")
        bucket.add_object_created_notification(s3notify.SnsDestination(self.topic),
        s3.NotificationKeyFilter(prefix=prefix))
