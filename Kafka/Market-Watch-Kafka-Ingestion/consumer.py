'''
initial consumer 
'''

from kafka import KafkaConsumer
from json import loads

#consumer object
consumer = KafkaConsumer(
    'StockValues',
    bootstrap_servers = ['localhost:9092'],
    auto_offset_reset = 'earliest',
    enable_auto_commit = True,
    group_id = 'my-group',
    value_deserializer = lambda x: loads(x.decode('utf-8'))
)

#print consumer message
for message in consumer:
    print(message)


