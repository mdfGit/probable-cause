#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
  Consumes messages from a Amazon Kinesis streams and does wordcount.
  This example spins up 1 Kinesis Receiver per shard for the given stream.
  It then starts pulling from the last checkpointed sequence number of the given stream.
  Usage: kinesis_wordcount_asl.py <app-name> <stream-name> <endpoint-url> <region-name>
    <app-name> is the name of the consumer app, used to track the read data in DynamoDB
    <stream-name> name of the Kinesis stream (ie. mySparkStream)
    <endpoint-url> endpoint of the Kinesis service
      (e.g. https://kinesis.us-east-1.amazonaws.com)
  Example:
      # export AWS keys if necessary
      $ export AWS_ACCESS_KEY_ID=<your-access-key>
      $ export AWS_SECRET_KEY=<your-secret-key>
      # run the example
      $ bin/spark-submit -jars external/kinesis-asl/target/scala-*/\
        spark-streaming-kinesis-asl-assembly_*.jar \
        external/kinesis-asl/src/main/python/examples/streaming/network_health.py \
        myAppName mySparkStream https://kinesis.us-east-1.amazonaws.com
  There is a companion helper class called KinesisWordProducerASL which puts dummy data
  onto the Kinesis stream.
  This code uses the DefaultAWSCredentialsProviderChain to find credentials
  in the following order:
      Environment Variables - AWS_ACCESS_KEY_ID and AWS_SECRET_KEY
      Java System Properties - aws.accessKeyId and aws.secretKey
      Credential profiles file - default location (~/.aws/credentials) shared by all AWS SDKs
      Instance profile credentials - delivered through the Amazon EC2 metadata service
  For more information, see
      http://docs.aws.amazon.com/AWSSdkDocsJava/latest/DeveloperGuide/credentials.html
  See http://spark.apache.org/docs/latest/streaming-kinesis-integration.html for more details on
  the Kinesis Spark Streaming integration.
"""

"""
Cloudtrail json schema
root
 |-- awsRegion: string (nullable = true)
 |-- eventID: string (nullable = true)
 |-- eventName: string (nullable = true)
 |-- eventSource: string (nullable = true)
 |-- eventTime: string (nullable = true)
 |-- eventType: string (nullable = true)
 |-- eventVersion: string (nullable = true)
 |-- recipientAccountId: string (nullable = true)
 |-- requestID: string (nullable = true)
 |-- requestParameters: struct (nullable = true)
 |    |-- roleArn: string (nullable = true)
 |    |-- roleSessionName: string (nullable = true)
 |-- resources: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- ARN: string (nullable = true)
 |    |    |-- accountId: string (nullable = true)
 |    |    |-- type: string (nullable = true)
 |-- responseElements: struct (nullable = true)
 |    |-- assumedRoleUser: struct (nullable = true)
 |    |    |-- arn: string (nullable = true)
 |    |    |-- assumedRoleId: string (nullable = true)
 |    |-- credentials: struct (nullable = true)
 |    |    |-- accessKeyId: string (nullable = true)
 |    |    |-- expiration: string (nullable = true)
 |    |    |-- sessionToken: string (nullable = true)
 |-- sourceIPAddress: string (nullable = true)
 |-- userAgent: string (nullable = true)
 |-- userIdentity: struct (nullable = true)
 |    |-- accessKeyId: string (nullable = true)
 |    |-- accountId: string (nullable = true)
 |    |-- arn: string (nullable = true)
 |    |-- principalId: string (nullable = true)
 |    |-- sessionContext: struct (nullable = true)
 |    |    |-- attributes: struct (nullable = true)
 |    |    |    |-- creationDate: string (nullable = true)
 |    |    |    |-- mfaAuthenticated: string (nullable = true)
 |    |    |-- sessionIssuer: struct (nullable = true)
 |    |    |    |-- accountId: string (nullable = true)
 |    |    |    |-- arn: string (nullable = true)
 |    |    |    |-- principalId: string (nullable = true)
 |    |    |    |-- type: string (nullable = true)
 |    |    |    |-- userName: string (nullable = true)
 |    |-- type: string (nullable = true)

"""

from __future__ import print_function

import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kinesis import KinesisUtils, InitialPositionInStream

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            "Usage: network_health.py <app-name> <stream-name> <endpoint-url> <region-name>",
            file=sys.stderr)
        sys.exit(-1)

    sc = SparkContext(appName="PythonStreamingKinesisNetworkHealthAsl")
    ssc = StreamingContext(sc, 1)
    appName, streamName, endpointUrl, regionName = sys.argv[1:]

    print("appName: " + appName)
    print("streamName: " + streamName)
    print("endpointUrl: " + endpointUrl)
    print("regionName: " + regionName)

    lines = KinesisUtils.createStream(
        ssc, appName, streamName, endpointUrl, regionName, InitialPositionInStream.LATEST, 2)
    
    #print(lines)
    print("hello1")

    #lines.collect().foreach(print)

    #new
    parsed = lines.flatMap(lambda line: line.split(" "))
    parsed.count().map(lambda x:'data in this batch: %s' % x).pprint()
    #new stop

    #counts = lines.flatMap(lambda line: line.split(" ")) \
    #    .map(lambda word: (word, 1)) \
    #    .reduceByKey(lambda a, b: a+b)

    print("lines.count().pprint()")
    lines.count().pprint()    

    print("lines.count()")    
    print(lines.count())    

    #print("dir(counts)")
    #print(dir(counts))

    #print("counts.pprint()")
    #counts.pprint()

    #print("counts: " + counts.pprint())
    print("hello2")

    ssc.start()
    ssc.awaitTermination()