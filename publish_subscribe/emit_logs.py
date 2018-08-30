import pika
import sys

"""
emit_logs.py

Program to broadcast log messages to an exchange
"""

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')