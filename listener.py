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
binding_key = 'image_queue'  # Adjusted binding key to match the routing key used in the publisher
channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=binding_key)


def callback(ch, method, properties, body):
    # Decode the base64 data
    base64_data = body.decode('utf-8')
    image_data = base64.b64decode(base64_data)

    # Convert to a PIL image
    image = Image.open(io.BytesIO(image_data))

    # Convert the image to grayscale
    grayscale_image = image.convert('L')

    # Save the image to disk
    file_name = f'grayscale_image_{datetime.now().strftime("%Y%m%d_%H%M%S")}.jpeg'
    file_path = os.path.join('images', file_name)

    # with open(file_path, 'wb') as image_file:
    #     image_file.write(grayscale_image)

    grayscale_image.save(file_path)
    print(f"Image saved to {file_path}")


# Set up consumption of the queue
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
