from cassandra.cluster import Cluster
import uuid
import time

# Connect to Cassandra cluster
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('test_keyspace')

# Prepare test data
write_stmt = session.prepare("INSERT INTO test_table (id, value) VALUES (?, ?)")

# Measure throughput
def measure_throughput(operations):
    start_time = time.time()
    for _ in range(operations):
        id = uuid.uuid4()
        session.execute(write_stmt, (id, 'test_value'))
    end_time = time.time()
    throughput = operations / (end_time - start_time)
    print(f"Throughput: {throughput:.2f} ops/sec")

measure_throughput(operations=5000)
