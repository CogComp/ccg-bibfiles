aws lambda create-function \
  --function-name ccg-bib-convert \
  --zip-file fileb://function.zip \
  --handler lambda_function.main \
  --runtime python3.8 \
  --role arn:aws:iam::386895259649:role/lambda-ex \
  --timeout 60