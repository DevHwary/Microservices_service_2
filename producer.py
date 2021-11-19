import pika, json
from pika import connection
from pika import channel


params = pika.URLParameters('amqps://drtzmlak:mt7OkZ_SML55NTPGgMqJ_tq8KQ3G_wG-@woodpecker.rmq.cloudamqp.com/drtzmlak')

connection = pika.BlockingConnection(params)
channel = connection.channel()

def publish(method, body):
    """
    Send message to admin (Django) app
    """
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)