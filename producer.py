#backend producer lambda in python

import json
import boto3
import random
from datetime import datetime

# Initialize the SQS client
sqs = boto3.client('sqs', region_name='us-east-1')
sqs_url = '<sqs url>'
no_of_consumer = 2
number_of_orders = 100

def lambda_handler(event, context):
    order_id = 1000
    records = []

    for i in range(number_of_orders):
        params = {
            'MessageBody': json.dumps({
                'orderId': order_id,
                'order': f'groceries - {random.randint(0, 9)}',  # Generate a random order
                'timestamp': datetime.now().isoformat()
            }),
            'QueueUrl': sqs_url,
            'MessageDeduplicationId': str(order_id),  # Convert to string
            'MessageGroupId': f'group-{i % no_of_consumer }'  # Grouping by shop
        }
        records.append(params)
        order_id += 1  # Increment order_id

    for record in records:
        try:
            response = sqs.send_message(**record)
            print(json.dumps(response))
        except Exception as error:  # Handle errors
            print(error)
