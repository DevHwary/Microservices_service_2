import pika
from pika import connection
from pika import channel

params = pika.URLParameters('amqps://drtzmlak:mt7OkZ_SML55NTPGgMqJ_tq8KQ3G_wG-@woodpecker.rmq.cloudamqp.com/drtzmlak')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print("Recieve in main")
    print(body)


channel.basic_consume(queue='main', on_message_callback=callback)
print ("Started consuming -----")
channel.start_consuming()
channel.close()