#!/usr/bin/env bash

#This shell script updates Postman environment file with the API Gateway URL created
# via the api gateway deployment

echo "Running run-test.sh"

#api_gateway_url=`aws cloudformation describe-stacks \
#  --stack-name eltest-dev \
#  --query "Stacks[0].Outputs[*].{OutputValueValue:OutputValue}" --output text`
#
#echo "API Gateway URL:" ${api_gateway_url}


api_gateway_url=`aws cloudformation describe-stacks \
  --stack-name eltest-dev \
  --query "Stacks[0].Outputs[? OutputKey == 'ServiceEndpoint'].OutputValue" --output text`

echo "API Gateway URL 1:" ${api_gateway_url}
export API_GATEWAY_URL=api_gateway_url
python ./test/hello.py
