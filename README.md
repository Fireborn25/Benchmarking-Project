
# Benchmarking-Project

Benchmarking Bayou vs. Cassandra

## Set up of Cassandra

1. Install Cassandra

    Ensure Apache Cassandra is installed and running on your system.
    If not installed, follow the official installation guide.
2. Python Environment Setup

    Install Python 3.x and set up a virtual environment:

``` bash
python3 -m venv cassandra-benchmark
source cassandra-benchmark/bin/activate
```

3. Install the Cassandra Python Driver:

``` bash
pip install cassandra-driver
Set Up the Keyspace and Table
```

4. Open the Cassandra CQL shell (cqlsh) and execute the following:

```sql
CREATE KEYSPACE test_keyspace 
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3};

CREATE TABLE test_keyspace.test_table (
    id UUID PRIMARY KEY,
    value TEXT
);
```

5. Multi-Node Setup for Fault Tolerance Tests

    If you're testing fault tolerance, set up a multi-node Cassandra cluster.
    Ensure nodes are properly connected and visible in the cluster using:

```bash
nodetool status
```


## Setting up Bayou

``` bash
pip install -e '.'

make test_storage        # Test Storage's implementation
make test_client         # End-to-End testing from client to server
```