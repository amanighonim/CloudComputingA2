# CloudComputingA2
This project implements a simplified backend system for an e-commerce platform using AWS serverless services. The system accepts orders, stores them in a database, sends notifications, and handles failures using an event-driven architecture.

Amazon SNS -> Event broadcast (OrderTopic)

Amazon SQS -> Message queuing (OrderQueue)

AWS Lambda -> Serverless processing (orderProcessing)

Amazon DynamoDB -> NoSQL database (Orders table)

Dead-Letter Queue (DLQ) -> Reliable error handling (OrderDLQ)

Setup Instructions: 

1- Create DynamoDB Table

Table name: Orders

Partition Key: orderId (String)

2- Create SNS Topic

Name: OrderTopic

3- Create SQS Queues

Main queue: OrderQueue

Dead-Letter Queue: OrderDLQ

Set maxReceiveCount = 3 on OrderQueue and attach OrderDLQ

4- Create Lambda Function

Language: Python

Add trigger: SQS -> OrderQueue

Permissions: Grant AmazonDynamoDBFullAccess

5- Test the System

Publish a test message to SNS

Verify flow: SNS -> SQS -> Lambda -> DynamoDB -> Logs

The flow of data is:

1- An ordering user submits a new order.

2- The order is published to an Amazon SNS Topic.

3- The SNS topic delivers the message to an Amazon SQS Queue.

4- The AWS Lambda function is triggered by the SQS queue.

5- The Lambda function processes the message and stores the order in Amazon DynamoDB.

6- If the Lambda fails to process the message after 3 attempts, it is moved to a Dead-Letter Queue (DLQ).

![Architecture Diagram](Architecture-Diagram.png)
