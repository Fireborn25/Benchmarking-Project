from cassandra.cluster import Cluster
import uuid
import time

# Connect to Cassandra cluster
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('test_keyspace')

# Insert and simulate node failure
write_stmt = session.prepare("INSERT INTO test_table (id, value) VALUES (?, ?)")

def fault_tolerance_test():
    try:
        id = uuid.uuid4()
        # Write before failure
        session.execute(write_stmt, (id, 'test_value'))
        print("Write successful before node failure.")

        # Simulate node failure: manually stop a Cassandra node.

        # Write during failure
        session.execute(write_stmt, (uuid.uuid4(), 'test_during_failure'))
        print("Write successful during node failure.")

        # Restart node, wait for recovery, then read
        time.sleep(10)  # Simulate recovery time
        print("Node recovery simulated. Checking data integrity...")

        read_stmt = session.prepare("SELECT value FROM test_table WHERE id = ?")
        result = session.execute(read_stmt.bind((id,)))
        print(f"Recovered value: {result.one()}")
    except Exception as e:
        print(f"Error during fault tolerance test: {e}")

fault_tolerance_test()
