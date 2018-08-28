import pika
import time

"""
worker.py

Worker to simulate a task given different sized messages
"""


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_consume(callback, queue='hello', no_ack=True)
print("  [*] Waiting for messages. To exit press CTRL-C")
channel.start_consuming()
