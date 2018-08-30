import pika

"""
receive_logs.py

Receives messages from the logs exchange
"""

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

