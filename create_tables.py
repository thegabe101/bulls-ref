import boto3

dynamodb = boto3.resource(
    'dynamodb', region_name='us-west-2', endpoint_url='http://localhost:8000')

try:
    resp = dynamodb.create_table(
        AttributeDefinitions=[
            {
                "AttributeName": "PlayerName",
                "AttributeType": "S"
            },
            {
                "AttributeName": "PlayerNumber",
                "AttributeType": "N"
            },
        ],
        TableName="Player",
        KeySchema=[
            {
                "AttributeName": "PlayerName",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "PlayerNumber",
                "KeyType": "RANGE"
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 1,
            "WriteCapacityUnits": 1
        })
except Exception as e:
    print(e)
