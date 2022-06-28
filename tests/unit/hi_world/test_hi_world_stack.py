import aws_cdk as core
import aws_cdk.assertions as assertions

from hi_world.hi_world_stack import HiWorldStack

# example tests. To run these tests, uncomment this file along with the example
# resource in hi_world/hi_world_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = HiWorldStack(app, "hi-world")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
         "VisibilityTimeout": 300
     })
