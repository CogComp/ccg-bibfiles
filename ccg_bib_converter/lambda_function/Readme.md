This directory contains the code for the Lambda function that converts a bib entry into the CCG format.

A [Lambda Function](https://aws.amazon.com/lambda/) is a very cheap and fast way to have a machine run a fast piece of code on AWS servers.
The AWS free tier includes a very large amount of compute time, and this job is really fast, so there shouldn't be a problem in terms of cost.
See [this tutorial](https://docs.aws.amazon.com/lambda/latest/dg/python-package-create.html) for how to create a Lambda function in Python.
I've included some extra scripts to help with the development: 
    - `scripts/create-function.sh`: Creates the Lambda function.
    You only need to run this the first time.
    - `scripts/delete-function.sh`: Deletes it
    - `scripts/invoke-function.sh`: An example invocation of the Lambda function using the AWS commandline tools
    - `scripts/make-zip.sh`: Creates the zip file which contains the Lambda function and is eventually uploaded to AWS
    - `scripts/update-function.sh`: Updates the code of the function after it has been created.
You need to have the AWS commandline configured in order to run any of these scripts.
Currently you need access to my (Dan Deutsch) AWS account (see below for more) for these commands to work correctly.

The general workflow: Use `scripts/make-zip.sh` every time you update the code locally and want to deploy it.
If the function doesn't exist, run `scripts/create-function.sh`.
Otherwise, `scripts/update-function.sh` will deploy the zip file to the AWS servers.

New python packages can be added like:
```
pip install --target ./package <package-name>
```
Required packages are only `bibtexparser`, so you need to run the following line once before making the zip.
```
pip install --target ./package bibtexparser
```

The Lambda function is exposed through an AWS API Gateway.
See [here](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-api-as-simple-proxy-for-lambda.html) for a tutorial about how to integrate the API with the Lambda function.

If you ever receive a Javascript error about CORS issues, what I did to fix it was follow [this](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors-console.html).
That enables CORS for the API.
Then I also had to return `{"headers": {"Access-Control-Allow-Origin": "*"}}` in the Lambda function headers.

Right now, all of this is hosted on my (Dan Deutsch) AWS account, but the AWS free tier includes a ton of free requests which we should never exceed.
If you want to switch it to a CogComp owned AWS account, the above tutorials will explain how to set up the Lambda function and API Gateway with the corresponding IAM Roles and permissions.
After, each of the `script` bash scripts will need to be updated with a different IAM role.

The `index.html` file has an example of how to send a request to the Lambda function.
Now the Python flask server does not need to be running locally.