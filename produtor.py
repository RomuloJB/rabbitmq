import pika
import sys

parametros = pika.ConnectionParameters('localhost')
conection = pika.BlockingConnection(parametros)
channel = conection.channel()

channel.queue_declare(queue="fila_pedidos", durable=True)

mensagem = ' '.join(sys.argv[1:]) or "Pedido Padrão"

channel.basic_publish(exchange='', routing_key='fila_pedidos', body=mensagem, properties=pika.BasicProperties(delivery_mode=2))

print(f" [x] Enviado para a fila:: '{mensagem}'")

conection.close()
