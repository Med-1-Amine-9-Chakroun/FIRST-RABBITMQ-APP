import pika

connection_parameters = pika.ConnectionParameters("localhost")

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue="letterbox")

message = "hello, this is my first message"

channel.basic_publish(exchange='', routing_key='letterbox', body=message)

print("sent message: ",message)

connection.close()