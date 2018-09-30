# probable-cause
A framework to classify enterprise cloud system and application health to enable rapid / proactive automated response

## Architecture

![alt text](architecture.png "Probable Cause Architecture")

## Aggregation
*AWSConfig Events to CloutWatch Logs*

*CloudTrail Events to Cloutwatch Logs*

*VPC Flow Logs Events to Cloudwatch Logs*

*Cloudwatch for Apps to Cloudwatch Logs*

## Distribution
*Cloudwatch Subscription to Elastic Search*

*Cloudwatch Subscription to Kinesis*

## Analysis
*Kinesis Stream to Spark*

## Dashboard 
*DynamoDB updates front end display*


## Demo Assets (internal only)

Jenkins
http://ec2-18-234-64-58.compute-1.amazonaws.com/jenkins/

Kibana
http://centralized-logging-aws-elk-1696840377.us-east-1.elb.amazonaws.com/_plugin/kibana/

Spark Dashboard
http://ec2-34-198-7-204.compute-1.amazonaws.com:8080/

Probable Cause
http://insight-probable-cause-web.s3-website-us-east-1.amazonaws.com/

## Code Layout

*Elasticache and Kibana Stack - Cloudformation*
> Probable Cause > Cloudformation > Dev

*CloudWatch Log Subscriptions*
> Probable Cause > lambdas > logstreamer

*Website Results - Static S3 and Lambda*
> Probable Cause > web_results

*Contextual Analysis*
> Probable Cause > pyspark

