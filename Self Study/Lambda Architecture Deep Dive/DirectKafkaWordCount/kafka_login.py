import io, random, threading, logging, time, sys

import avro.io
import avro.schema

from kafka.client   import KafkaClient
from kafka.consumer import KafkaConsumer
from kafka.producer import SimpleProducer

KAFKA_TOPIC = 'login-topic'

LOGIN_USERS = ['alice','bob','chas','dee','eve']
LOGIN_OPS   = ['login','logout']

def get_login_event():
    return {
        'date'    : time.strftime('%F'),
        'time'    : time.strftime('%T'),
        'user'    : random.choice(LOGIN_USERS),
        'op'      : random.choice(LOGIN_OPS),
        'success' : bool(random.randint(0,1)) }

AVRO_SCHEMA_STRING = '''{
  "namespace" : "login.avro",
  "type"      : "record",
  "name"      : "Event",
  "fields"    : [
    { "name" : "date"    , "type" : "string"  },
    { "name" : "time"    , "type" : "string"  },
    { "name" : "user"    , "type" : "string"  },
    { "name" : "op"      , "type" : "string"  },
    { "name" : "success" , "type" : "boolean" }
  ]
}
'''

class AvroSerDe:
    '''Serializes and deserializes data structures using Avro.'''
    def __init__(self, avro_schema_string):
        self.schema = avro.schema.parse(avro_schema_string)
        self.datum_writer = avro.io.DatumWriter(self.schema)
        self.datum_reader = avro.io.DatumReader(self.schema)

    def obj_to_bytes(self, obj):
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        self.datum_writer.write(obj, encoder)
        raw_bytes = bytes_writer.getvalue()
        return raw_bytes

    def bytes_to_obj(self, raw_bytes):
        bytes_reader = io.BytesIO(raw_bytes)
        decoder = avro.io.BinaryDecoder(bytes_reader)
        obj = self.datum_reader.read(decoder)
        return obj

class Producer(threading.Thread):
    '''Produces login events and publishes them to Kafka topic.'''
    daemon = True
    def run(self):
        avro_serde = AvroSerDe(AVRO_SCHEMA_STRING)
        client = KafkaClient('localhost:9092')
        producer = SimpleProducer(client)
        while True:
            raw_bytes = avro_serde.obj_to_bytes(get_login_event())
            producer.send_messages(KAFKA_TOPIC, raw_bytes)
            time.sleep(1)

class Consumer(threading.Thread):
    '''Consumes users from Kafka topic.'''
    daemon = True
    def run(self):
        avro_serde = AvroSerDe(AVRO_SCHEMA_STRING)
        client = KafkaClient('localhost:9092')
        consumer = KafkaConsumer(KAFKA_TOPIC,
                                 group_id='my_group',
                                 bootstrap_servers=['localhost:9092'])

        # Keep track of and print statistics.
        attempts  = 0
        failures  = 0
        failure_rate = 0.0
        for message in consumer:
            event = avro_serde.bytes_to_obj(message.value)
            print '--> ' + str(event)
            if event['op'] == 'login':
                attempts += 1
                if not event['success']: failures  += 1
                failure_rate = float(failures)/attempts
            print '--> Event: '        + str(event)
            print '--> Failure Rate: ' + str(failure_rate)


def main():
    '''Starts producer and consumer threads.'''
    threads = [ Producer(), Consumer() ]
    for t in threads: t.start()
    time.sleep(5)

if __name__ == '__main__':
    if len(sys.argv) == 0:
        print "To watch Kafka messages run app with --debug"
    elif sys.argv.count('--debug') > 0:
        logging.basicConfig(
            format='%(asctime)s.%(name)s:%(message)s',
            level=logging.DEBUG)
    main()
