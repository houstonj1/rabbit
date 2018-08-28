import pika
import time

"""
worker.py

Worker to simulate a task given different sized messages
"""

def callback(ch, method, properties, body):
    """
    Callback function - receives messages and performs a task
    """
    print("  [x] Received {0}".format(body))
    time.sleep(body.count(b'.'))
    print("  [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_hello', durable=True)

channel.basic_consume(callback, queue='hello')
print("  [*] Waiting for messages. To exit press CTRL-C")
channel.start_consuming()
