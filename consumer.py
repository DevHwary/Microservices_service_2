import pika, json
from pika import connection
from pika import channel
from main import Product, db

params = pika.URLParameters('amqps://drtzmlak:mt7OkZ_SML55NTPGgMqJ_tq8KQ3G_wG-@woodpecker.rmq.cloudamqp.com/drtzmlak')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print("Recieve in main")
    data = json.loads(body)
    print(data)


    if properties.content_type == 'product-created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()

    elif properties.content_type == 'product-updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
    
    elif properties.content_type == 'product-deleted':
        product = Product.query.get(data['id'])
        db.session.delete(product)
        db.session.commit()


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)
print ("Started consuming -----")
channel.start_consuming()
channel.close()