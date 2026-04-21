import json
import uuid
from datetime import datetime
from src.db.dynamodb import table
import boto3

sns = boto3.client('sns')

def handler(event, context):
    body = json.loads(event['body'])

    item = {
        "id": str(uuid.uuid4()),
        "amount": body['amount'],
        "category": body['category'],
        "createdAt": datetime.utcnow().isoformat()
    }

    # ✅ SNS ALERT (correct place)
    if body['amount'] > 5000:
        sns.publish(
            TopicArn='arn:aws:sns:ap-south-1:811623296418:expense-alert',
            Message=f"High expense alert: ₹{body['amount']}"
        )

    table.put_item(Item=item)

    return {
        "statusCode": 200,
        "body": json.dumps(item)
    }