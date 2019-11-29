# dssc-ecr-sec-scan-automation
  Many devops team works in silos and many times these team push image to AWS ECR without CI/CD pipeline. This leads to multiple unscanned image and creates feedback gap between security and devops. This serverless application will help customer to create AWS ECR event based scan.

We are using AWS ECR Push event monitoring using cloudwatch events and the same cloudwatch event triggers lambda function to initiate scan. This security automation provides ability to reduce scheduled scan overhead.

Made with ❤️ by Trend Micro. Available on the AWS Serverless Application Repository

License
Apache License 2.0 (undefined)
