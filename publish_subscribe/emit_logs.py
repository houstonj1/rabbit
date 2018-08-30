import pika
import sys

"""
emit_logs.py

Program to broadcast log messages to an exchange
"""

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or 'info: Hello World'
channel.basic_publish(exchange='logs', routing_key='', body=message)
print("  [x] Sent {0}".format(message))

connection.close()
