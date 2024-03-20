import os
from datetime import datetime

import pika
import base64
from PIL import Image
import io

connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()


exchange_name = 'image_queue_exchange'

channel.exchange_declare(exchange=exchange_name, exchange_type='topic')

queue_name = 'image_queue'
channel.queue_declare(queue=queue_name)
binding_key = 'image_queue'
channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=binding_key)


def callback(ch, method, properties, body):

    base64_data = body.decode('utf-8')
    image_data = base64.b64decode(base64_data)

    image = Image.open(io.BytesIO(image_data))

    grayscale_image = image.convert('L')

    file_name = f'grayscale_image_{datetime.now().strftime("%Y%m%d_%H%M%S")}.jpeg'
    file_path = os.path.join('images', file_name)

    grayscale_image.save(file_path)
    print(f"Image saved to {file_path}")


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
