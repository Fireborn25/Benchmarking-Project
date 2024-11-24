from cassandra.cluster import Cluster
import uuid
import time

# Connect to Cassandra cluster
cluster = Cluster(['127.0.0.1'])  # Replace with your Cassandra node IPs
session = cluster.connect('test_keyspace')

# Prepare test data
write_stmt = session.prepare("INSERT INTO test_table (id, value) VALUES (?, ?)")
read_stmt = session.prepare("SELECT value FROM test_table WHERE id = ?")

# Measure latency for writes and reads
def measure_latency(concurrent_users, operations):
    start_time = time.time()
    for _ in range(operations):
        id = uuid.uuid4()
        # Write operation
        session.execute(write_stmt, (id, 'test_value'))
        # Read operation
        session.execute(read_stmt, (id,))
    end_time = time.time()
    avg_latency = (end_time - start_time) / operations
    print(f"Avg Latency with {concurrent_users} users: {avg_latency:.3f} seconds")

measure_latency(concurrent_users=10, operations=1000)
