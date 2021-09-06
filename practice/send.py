import pika
import json

test_data = {
    "name": 'jinwoo-test-json',
    "parts": ['52910G6000', '52910G6050', '52910G6100', '52910G6200', '52910G6300', '52910G6350', '52910G6400', '52910G6450', '52910G6500', '52910G6600', '52910G6650', '52910G6700', '52910G6750', '5296006251', '5296007901', '529604X200', '52970G6200', '58110G6000', '58110G6300', '58130G6000', '58130G6300', '58210G6000', '58230G6000', '5841107500']
}
test_data_json = json.dumps(test_data)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


channel.queue_declare(queue='jw')
channel.basic_publish(exchange='', routing_key='jw', body=test_data_json)
print(" [x] Sent JSON!")


connection.close()
