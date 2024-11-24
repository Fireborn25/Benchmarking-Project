from cassandra.cluster import Cluster
import uuid

# Connect to Cassandra cluster
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('test_keyspace')

# Insert data with different consistency levels
write_stmt = session.prepare("INSERT INTO test_table (id, value) VALUES (?, ?)")

def consistency_test():
    id = uuid.uuid4()
    # Insert with consistency level QUORUM
    session.execute(write_stmt.bind((id, 'test_value')), consistency_level='QUORUM')
    print(f"Written with QUORUM consistency.")

    # Read with consistency level ONE
    read_stmt = session.prepare("SELECT value FROM test_table WHERE id = ?")
    result = session.execute(read_stmt.bind((id,)), consistency_level='ONE')
    print(f"Read with ONE consistency: {result.one()}")

consistency_test()
