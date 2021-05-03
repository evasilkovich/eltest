#!/usr/bin/env bash

echo "Running run-test.sh"


export API_GATEWAY_URL=`aws cloudformation describe-stacks \
  --stack-name eltest-test \
  --query "Stacks[0].Outputs[? OutputKey == 'ServiceEndpoint'].OutputValue" --output text`

echo "API Gateway URL 1:" ${API_GATEWAY_URL}

#ls -l
cd tests
ls -l
python test_integration_hello.py
