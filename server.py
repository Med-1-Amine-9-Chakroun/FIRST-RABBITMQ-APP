import pika
from pika.exchange_type import ExchangeType

def on_request_message_received(ch, method, propreties, body):    
    print('Request received : ', propreties.correlation_id)
    ch.basic_publish('', routing_key = propreties.reply_to,
                     body=f'hey its your reply to{propreties.correlation_id}')
    

connection_parameters = pika.ConnectionParameters("localhost")

connection = pika.BlockingConnection(connection_parameters) 

channel = connection.channel()

channel.queue_declare(queue="request-queue")

channel.basic_consume(queue="request-queue", auto_ack=True, on_message_callback=on_request_message_received)

print("Starting Server")

channel.start_consuming()   