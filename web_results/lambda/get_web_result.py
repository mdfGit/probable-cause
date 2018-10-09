# -*- coding: iso-8859-15 -*-
# -------------------------------------------------------------------------
# -
# - tag_amis
# -
# -------------------------------------------------------------------------
# February 2017
# Python 3.5, BOTO 3.0
# Application to encapsulate
# calls with AWS
#

import json
import sys
import argparse
import traceback
import inspect
import boto3


__author__ = 'Mark Ferry'


# --------------------------------------
# Initialize
# --------------------------------------
def initialize():

    print(inspect.stack()[0][3])

    global client
    client = boto3.client('dynamodb')

    if run_mode == 'local':
        print("LOCAL RUN: Setting environment variables locally.")

    else:
        print("AWS RUN: environment variables should exist in the lambda configuration.")

# --------------------------------------
# Grab Command Line
# --------------------------------------
def get_command_line(argv):
    try:
        cmdLineParser = argparse.ArgumentParser(description="AMi Auto Tagging")
        cmdLineParser.add_argument("-d", "--data", help = "JSON Request data", required = True)
        args = cmdLineParser.parse_args(argv)
        return args.data
    except:
        return None

# --------------------------------------
# Update app status
# --------------------------------------
def update_application_status(ec2_status):
    try:

      params = ""

      if ec2_status == 'stopping':
        client.update_item(TableName='ProbableCauseMaster', Key={'ApplicationId':{'S':'1'}}, AttributeUpdates={"ProbableCauseSummary":{"Action":"PUT","Value":{'S': 'RB'}}})

      elif ec2_status == 'pending': 
        client.update_item(TableName='ProbableCauseMaster', Key={'ApplicationId':{'S':'1'}}, AttributeUpdates={"ProbableCauseSummary":{"Action":"PUT","Value":{'S': 'badapp'}}})
      
      else:
        client.update_item(TableName='ProbableCauseMaster', Key={'ApplicationId':{'S':'1'}}, AttributeUpdates={"ProbableCauseSummary":{"Action":"PUT","Value":{'S': 'healthy'}}})

    except Exception as error:
        print ("An error occurred in: {}: {}".format(inspect.stack()[0][3], error))
        raise error


# --------------------------------------
# Get app status
# --------------------------------------
def get_application_status():
    try:

        response = client.get_item(
            TableName='ProbableCauseMaster',
            Key={
                'ApplicationId': {
                    'S': '1'
                }
            }
        )

        print(response)

        my_item=response['Item']
        app=my_item['ApplicationId']['S']
        stat=my_item['Status']['S']
        prob=my_item['ProbableCauseSummary']['S']

        my_response="{ApplicationId: " + app + "}, {Status: " + stat + "}, {ProbableCauseSummary: " + prob + "}"
        print(my_response)

        print("{Status: 200}, body: hello")
        #return my_response
        #{ApplicationId: 1}, {Status: active}, {ProbableCauseSummary: nothing}
        #return "Status: 200, body: hello"
        #return "{statusCode: 200,body: hello}"
        return "OK"

    except Exception as error:
        print ("An error occurred in: {}: {}".format(inspect.stack()[0][3], error))
        raise error


def process(ec2_state):

    try:

        # print name of function
        print(inspect.stack()[0][3])

        #get_application_status()
        update_application_status(ec2_state)    

        print("Execution completed.")

    except Exception as error:
        print("An error occurred in: {}: {}".format(inspect.stack()[0][3], error))
        traceback.print_exc()

# --------------------------------------
# AWS Lambda Handler
# --------------------------------------
def lambda_handler(event, context):

    print(inspect.stack()[0][3])

    global run_mode
    run_mode = 'cloud'

    # Initialize
    initialize()

    print('json.dumps(event): ' + json.dumps(event))
    print("event['detail']: " + json.dumps(event['detail']))
    print("event['detail']['state']: " + json.dumps(event['detail']['state']))
    state = event['detail']['state']

    process(state)

    print('fin')

# --------------------------------------
# Main
# --------------------------------------
if __name__ == "__main__":

    print('### LOCAL ###')

    global run_mode
    run_mode = 'local'

    # Initialize
    initialize()

    # Fulfill Request
    # running, pending, stopping
    process("pending")

    print('fin')

    exit(0)
