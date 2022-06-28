# Welcome to your CDK Python project!


The `cdk.json` file tells the CDK Toolkit how to execute your app.
Note: Remove setting app: "python3 app.py" from cdk.json file so that multiple apps can be created in single project
ex. app_hello_world.py and app_hi_world.py 

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```


At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth --app "python3 app_hello_world.py" --profile prod
$ cdk synth --app "python3 app_hi_world.py" --profile prod
```
For Diff 
```
$ cdk diff --app "python3 app_hello_world.py" --profile prod
$ cdk diff --app "python3 app_hi_world.py" --profile prod
```

For Diff 
```
$ cdk deploy --app "python3 app_hello_world.py" --profile prod
$ cdk deploy --app "python3 app_hi_world.py" --profile prod
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk diff`        compare deployed stack with current state
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk docs`        open CDK documentation

Enjoy!
