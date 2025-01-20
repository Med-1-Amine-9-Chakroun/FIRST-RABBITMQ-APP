import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, method, propreties, body):    
    print('received new message : ', body)
    

connection_parameters = pika.ConnectionParameters("localhost")

connection = pika.BlockingConnection(connection_parameters) 

channel = connection.channel()

channel.queue_declare(queue="letterbox")

queue = channel.queue_declare(queue="", exclusive=True)

channel.basic_consume(queue="letterbox", auto_ack=True, on_message_callback=on_message_received)

print("Start  consuming")

channel.start_consuming()   