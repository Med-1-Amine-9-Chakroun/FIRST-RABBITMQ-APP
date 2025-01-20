import pika
from pika.exchange_type import ExchangeType
import uuid
def on_reply_message_received(ch, method, propreties, body):    
    print('reply received : ', body)
    

connection_parameters = pika.ConnectionParameters("localhost")

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

reply_queue = channel.queue_declare(queue='', exclusive=True)

channel.basic_consume(queue=reply_queue.method.queue, auto_ack=True, on_message_callback=on_reply_message_received)

channel.queue_declare(queue='request-queue')

message = "Can i resquest a reply?"

cor_id = str(uuid.uuid4())

print("Sending Request: ",cor_id)

channel.basic_publish(
    exchange='', 
    routing_key='request-queue', 
    properties=pika.BasicProperties(
        reply_to= reply_queue.method.queue,
        correlation_id=cor_id), 
    body=message
)

print("Starting client")    
channel.start_consuming()