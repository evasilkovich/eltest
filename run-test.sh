#!/usr/bin/env bash

#This shell script updates Postman environment file with the API Gateway URL created
# via the api gateway deployment

echo "Running update-postman-env-file.sh"

api_gateway_url=`aws cloudformation describe-stacks \
  --stack-name eltest-dev \
  --query "Stacks[0].Outputs[*].{OutputValueValue:OutputValue}" --output text`

echo "API Gateway URL:" ${api_gateway_url}

api_gateway_url1=`aws cloudformation describe-stacks \
  --stack-name eltest-dev \
  --query "Stacks[0].Outputs[? OutputKey == 'ServiceEndpoint'].OutputValue" --output text`

echo "API Gateway URL 1:" ${api_gateway_url1}
