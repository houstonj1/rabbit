import pika
import sys

"""
new_task.py

Scheduler for tasks being sent to work queues
"""

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_hello', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='', routing_key='hello', body=message, properties=pika.BasicProperties(delivery_mode=2,))
print("  [x] Sent {0}".format(message))
