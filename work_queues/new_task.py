import pika
import sys

"""
new_task.py

Scheduler for tasks being sent to work queues
"""

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')



