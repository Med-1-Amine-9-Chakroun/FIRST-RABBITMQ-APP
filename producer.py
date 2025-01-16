import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters("localhost")

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='pubsup', exchange_type=ExchangeType.fanout)

message = "hello, i want to broadcast this message"

channel.basic_publish(exchange='pubsup', routing_key='letterbox', body=message)

print("sent message: ",message)    

connection.close()