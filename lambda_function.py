import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

def lambda_handler(event, context):
    for record in event['Records']:
        try:
            message = json.loads(record['body'])
            if 'Message' in message:
                message = json.loads(message['Message'])

            item = {
                'orderId': message['orderId'],         
                'userId': message['userId'],
                'itemName': message['itemName'],
                'quantity': int(message['quantity']),
                'status': message['status'],
                'timestamp': message['timestamp']
            }

            table.put_item(Item=item)
            print(f" Order stored: {item['orderId']}")

        except Exception as e:
            print(f" Failed to process msg: {record['body']}")
            print(f"Error: {str(e)}")
            raise e 

    return {
        'statusCode': 200,
        'body': 'Processed all incoming SQS msgs.'
    }
