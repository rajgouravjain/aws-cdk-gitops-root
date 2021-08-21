

https://aws.amazon.com/blogs/developer/announcing-aws-cloud-development-kit-v2-developer-preview/



#App:
class MyApp(App):
     def __init__(self):
         MyFirstStack(self, "hello-cdk")

MyApp().synth()

#Stack:
from aws_cdk.core import App, Construct, Stack

# imagine these stacks declare a bunch of related resources
class ControlPlane(Stack): pass
class DataPlane(Stack): pass
class Monitoring(Stack): pass

class MyService(Construct):

  def __init__(self, scope: Construct, id: str, *, prod=False):
  
    super().__init__(scope, id)
  
    # we might use the prod argument to change how the service is configured
    ControlPlane(self, "cp")
    DataPlane(self, "data")
    Monitoring(self, "mon")
    
app = App();
MyService(app, "beta")
MyService(app, "prod", prod=True)

app.synth()  

#Environment:
env_EU = core.Environment(account="8373873873", region="eu-west-1")
env_USA = core.Environment(account="2383838383", region="us-west-2")

MyFirstStack(app, "first-stack-us", env=env_USA)
MyFirstStack(app, "first-stack-eu", env=env_EU)

#Resources:
```
cluster = ecs.Cluster(self, "Cluster")
service = ecs.Ec2Service(self, "Service", cluster=cluster)
```

```
#Construct a resource (bucket) just by its name (must be same account)
s3.Bucket.from_bucket_name(self, "MyBucket", "my-bucket-name")

#Construct a resource (bucket) by its full ARN (can be cross account)
s3.Bucket.from_bucket_arn(self, "MyBucket", "arn:aws:s3:::my-bucket-name")

#Construct a resource by giving attribute(s) (complex resources)
ec2.Vpc.from_vpc_attributes(self, "MyVpc", vpc_id="vpc-1234567890abcdef")
```

```
ec2.Vpc.from_lookup(self, "PublicVpc", 
    tags={"aws-cdk:subnet-type": "Public"})
```

#Tags:
```
Tags.of(my_construct).add("tagname", "value",
    apply_to_launched_instances=False,
    include_resource_types=["AWS::Xxx::Yyy"],
    exclude_resource_types=["AWS::Xxx::Zzz"],
    priority=100)
```

#Parameters:

```
cdk deploy MyStack YourStack --no-previous-parameters --parameters MyStack:uploadBucketName=UploadBucket --parameters YourStack:uploadBucketName=UpBucket
cdk deploy MyStack YourStack --no-previous-parameters --parameters MyStack:uploadBucketName=UploadBucket --parameters YourStack:uploadBucketName=UpBucket
```

#Assets:
https://docs.aws.amazon.com/cdk/latest/guide/assets.html

#Permissions:
https://docs.aws.amazon.com/cdk/latest/guide/permissions.html

#Construct context
Context values can be provided to your AWS CDK app in six different ways:
* Automatically from the current AWS account.
* Through the --context option to the cdk command. (These values are always strings.)
* In the project's cdk.context.json file.
* In the context key of the project's cdk.json file.
* In the context key of your ~/.cdk.json file.
* In your AWS CDK app using the construct.node.setContext() method.

*Use the cdk context command to view and manage the information in your cdk.context.json file. 
```
cdk context --reset 2
```
```
cdk synth --context Stack1:key=value --context Stack2:key=value Stack1 Stack2
```
```
import aws_cdk.core as cdk
import aws_cdk.aws_ec2 as ec2

class ExistsVpcStack(cdk.Stack):

    def __init__(scope: cdk.Construct, id: str, **kwargs):
  
        super().__init__(scope, id, **kwargs)
    
        vpcid = self.node.try_get_context("vpcid")
        vpc = ec2.Vpc.from_lookup(self, "VPC", vpc_id=vpcid)
    
        pubsubnets = vpc.select_subnets(subnetType=ec2.SubnetType.PUBLIC)
    
        cdk.CfnOutput(self, "publicsubnets",
            value=pubsubnets.subnet_ids.to_string())
```
* https://docs.aws.amazon.com/cdk/latest/guide/context.html

#Bootstrap::
```
cdk bootstrap aws://ACCOUNT-NUMBER-1/REGION-1 aws://ACCOUNT-NUMBER-2/REGION-2 ...
cdk bootstrap --profile prod
```
```
cdk bootstrap --show-template > bootstrap-template.yaml
aws cloudformation create-stack \
  --stack-name CDKToolkit \
  --template-body file://bootstrap-template.yaml
```

* https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html


