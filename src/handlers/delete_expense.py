import json
from src.db.dynamodb import table

def handler(event, context):
    id = event['pathParameters']['id']

    table.delete_item(Key={"id": id})

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Deleted"})
    }