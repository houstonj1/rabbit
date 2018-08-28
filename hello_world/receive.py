import pika

"""
receive.py

Receive messages from queues
"""

def callback(ch, method, properties, body):
    """
    Callback function - for receiving messages from Rabbit
    """
    print("  [x] Received {0}".format(body))

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_consume(callback, queue='hello', no_ack=True)
