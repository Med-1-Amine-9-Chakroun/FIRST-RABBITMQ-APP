import pika
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters("localhost")

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='mytopicexchange', exchange_type=ExchangeType.topic)

message = "this message needs to be routed"

channel.basic_publish(exchange='mytopicexchange', routing_key='user.europe.payments', body=message)

print("sent message: ",message)    

connection.close()