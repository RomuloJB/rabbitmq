import pika
import time

parametros = pika.ConnectionParameters('localhost')
conection = pika.BlockingConnection(parametros)
channel = conection.channel()

channel.queue_declare(queue="fila_pedidos", durable=True)

print(' [*] Aguardando pedidos. Para sair pressione CTRL+C')

def processar_pedido(ch, method, properties, body):
    mensagem_recebida = body.decode()

    print(f"[x] Iniciando processamento de: {mensagem_recebida}")

    tempo_processamento = body.count(b'.')
    time.sleep(tempo_processamento)

    print(f"[x] Finalizado processamento de: {mensagem_recebida}")

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='fila_pedidos', on_message_callback=processar_pedido)

channel.start_consuming()