# dssc-ecr-sec-scan-automation
  Many devops team works in silos and many times these team push image to AWS ECR without CI/CD pipeline. This leads to multiple unscanned image and creates feedback gap between security and devops. This serverless application will help customer to create AWS ECR event based scan.

We are using AWS ECR Push event monitoring using cloudwatch events and the same cloudwatch event triggers lambda function to initiate scan. This security automation provides ability to reduce scheduled scan overhead.

After application deployed, you can add Deep security smart check and AWS ECR credentials as environment variables.
```
AWS_ECR_ACCESS: <AWS_ACCESS_KEY_FOR_ECR_ACCESS>
AWS_ECR_SECRET: <AWS_SECRET_KEY_FOR_ECR_ACCESS>
DSSC_PSW: <DSSC_USER_PASSWORD>
DSSC_URL: <DSSC_URL>
DSSC_USER: <DSSC_USER_FOR_ECR_AUTOMATION>
```

We strongly recommend you to use AWS KMS to encrypt all environment variables stored in cleartext. remember to use least privilege access for AWS access and secret keys. for more details on how to security AWS lambda secrets. visit `https://docs.aws.amazon.com/lambda/latest/dg/env_variables.html`

We also recommend you to use seprate user in DSSC for this automation. for greater efficiency we encourage you to use our slack notification app for scan notificaiton if any vulnerabilities detected by Trend Micro deep security.



Made with ❤️ by Tejas sheth at Trend Micro. Available on the AWS Serverless Application Repository

License
Apache License 2.0 (undefined)
