from assessment.celery import app
from PIL import Image
import io
import base64
import pika


@app.task
def process_and_send_image(image_path):
    print(f'Sending image to RabbitMQ: {image_path}')
    with Image.open(image_path) as img:
        output = io.BytesIO()
        img.save(output, format='JPEG', quality=70)
        compressed_image = output.getvalue()
    base64_image = base64.b64encode(compressed_image).decode('utf-8')
    connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
    channel = connection.channel()
    channel.queue_declare(queue='image_queue')
    channel.basic_publish(exchange='image_queue_exchange',
                          routing_key='image_queue',
                          body=base64_image)
    connection.close()
