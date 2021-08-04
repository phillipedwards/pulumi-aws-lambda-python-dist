"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import lambda_
from pulumi_aws import iam

lambda_role = iam.Role('lambdaRole',
    assume_role_policy="""{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": "sts:AssumeRole",
                "Principal": {
                    "Service": "lambda.amazonaws.com"
                },
                "Effect": "Allow",
                "Sid": ""
            }
        ]
    }"""
)

lambda_role_policy = iam.RolePolicy('lambdaRolePolicy',
    role=lambda_role.id,
    policy="""{
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        }]
    }"""
)

lambda_func = lambda_.Function("mylambda",
    role=lambda_role.arn,
    runtime="python3.7",
    handler="hello_pulumi.lambda_handler",
    code=pulumi.AssetArchive({
        '.': pulumi.FileArchive('./src/dist/'),
    })
)

pulumi.export("function-arn", lambda_func.arn)
pulumi.export("function-name", lambda_func.name)