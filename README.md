# probable-cause
A framework to classify enterprise cloud system and application health to enable rapid / proactive automated response

## Architecture

![alt text](architecture.png "Probable Cause Architecture")

## Demo Assets (internal only)

Jenkins
http://ec2-18-234-64-58.compute-1.amazonaws.com/jenkins/

Kibana
http://centralized-logging-aws-elk-1696840377.us-east-1.elb.amazonaws.com/_plugin/kibana/

Spark Dashboard
http://ec2-34-198-7-204.compute-1.amazonaws.com:8080/

Probable Cause
http://insight-probable-cause-web.s3-website-us-east-1.amazonaws.com/

## Demo Steps

*Reboot Jenkins*

*Change Security Group on Jenkins*

*Check Probable Cause*

## Code Layout

*Elasticache and Kibana Stack - Cloudformation*
> Probable Cause > Cloudformation > Dev

*CloudWatch Log Subscriptions*
> Probable Cause > lambdas 

*Website Results - Static S3 and Lambda*
> Probable Cause > web_results


