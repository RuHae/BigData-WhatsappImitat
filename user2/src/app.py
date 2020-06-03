import threading
import logging
import time
import json

from kafka import KafkaConsumer, KafkaProducer
global_counter = '2'

class Producer(threading.Thread):
    daemon = True

    def run(self):
        producer = KafkaProducer(bootstrap_servers='my-cluster-kafka-bootstrap:9092')
        global global_counter
        #time.sleep(5)
        while True:
            i = global_counter + '2'
            s = str(i)
            print('User 2 sending')
            producer.send('my-topic2', s.encode())
            time.sleep(5)


class Consumer(threading.Thread):
    daemon = True
    
    def run(self):
        global global_counter
        consumer = KafkaConsumer('my-topic1', bootstrap_servers='my-cluster-kafka-bootstrap:9092')#,
                           
        print('User 2 Messages:')
        d = []
        for message in consumer:
            global_counter = message.value.decode('utf-8')
            d.append(message.value.decode('utf-8'))
            #time.sleep(5)
            
            print('User2: ', global_counter)#, d)


def main():
    threads = [
        Producer(),
        Consumer()
    ]

    for t in threads:
        t.start()

    time.sleep(10)

while __name__ == "__main__":
    main()
