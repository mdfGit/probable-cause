
#### Install awscli on Master node
sudo apt install awscli

#### Get code to S3
aws s3 cp /Users/MacBookPro_MFerry/Documents/_code/repos/git/github/probable-cause/web_results/pyspark/network_health.py s3://insight-deploy-bucket/pySpark/network_health.py

#### Deploy code from S3 bucket
aws s3 cp s3://insight-deploy-bucket/pySpark/network_health.py /usr/local/spark/network_health.py

#### Run spark application "network_health"

From Master top-level: /usr/local/spark
(Be sure the version of spark 2.3.1 matches the kinesis dependency ...asl_2.11:2.3.1)
```
bin/spark-submit --packages org.apache.spark:spark-streaming-kinesis-asl_2.11:2.3.1 --master spark://ec2-34-198-7-204.compute-1.amazonaws.com:7077 network_health.py myNetworkHealth BotoDemo https://kinesis.us-east-1.amazonaws.com us-east-1
```