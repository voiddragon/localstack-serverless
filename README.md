Serverless/LocalStack
===

Dependencies
---

- Docker
- [Localstack](https://localstack.cloud/) - Install via Brew
    > brew install localstack
- [Serverless](https://www.serverless.com/) - Install via NPM
    > npm install -g serverless

What is localstack and why do we use it?
---

- Localstack simulates an AWS-like environment (not everything is fully supported especially in the free version)
- You do not need localstack to run lambdas, they're just functions you can run locally
- Localstack is helpful to simulate the deployment as well as other dependent services such as S3 and SQS
- Localstack Free does not support RDS, it is recommended you install your own Postgres instance to connect to.
- For interacting with localstack, [awscli-local](https://github.com/localstack/awscli-local) can be used to perform most tasks.

What is serverless and why do we use it?
---

- First, what are lambdas? Lambdas are small event driven apps that perform one task and then exit.
- AWS has their own framework for building lambdas which is AWS Serverless Application Model (AWS SAM)
- SAM is more complicated and manual vs the Serverless Framework which helps to abstract and automate a lot of tasks
- Serverless is configured by the main serverless.yml file, additional plugins can help to automate other tasks
- Serverless can also automatically create dependent services like API Gateway or SQS for example.

Helpful Commands
---

- Starting localstack (start after docker is started)
    > localstack start

- Starting a serverless project
    > sls

- Deploying a serverless project to localstack
    > sls deploy --stage local

- Manually invoking a function (after deployment)
    > sls invoke --stage local --function <function name>

- Manually invoking a function with data (after deployment), this can also be used to simulate AWS events
    > sls invoke --stage local --function <function name> --path data.json

