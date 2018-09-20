#! /bin/bash

echo #########
echo `date`
echo #########

ACTION=$1
LAMBDA_NAME=$2

# zip the virtualenv folder
zip -r ./deployment/probablecauseweb.zip * -x "hcdo/*" -x "probablecauseweb/*"

if [ "$ACTION" = "update" ]
then
    echo "update function..."

    aws lambda update-function-code \
    --region us-east-1 \
    --function-name $LAMBDA_NAME \
    --zip-file fileb://deployment/probablecauseweb.zip

elif [ "$ACTION" = "create" ]
then
    echo "create function..."

    aws lambda create-function \
    --region us-east-1 \
    --function-name $LAMBDA_NAME \
    --description "This AMT Lambda function will determine if an ami is not CPM managed and is in-use" \
    --zip-file fileb://deployment/probablecauseweb.zip \
    --role arn:aws:iam::120270496361:role/GetWebResultsRole \
    --handler get_web_result.lambda_handler \
    --runtime python3.6 \
    #--vpc-config $VPC_CONFIG \
    #--memory-size 256 \
    --timeout 30 \
    --environment Variables="{ENVVAR1=value,ENVVAR2=value}" \
    --tags Name=lambda-function,tag2=tag2value
fi

