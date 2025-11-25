import clickhouse_connect

_client = None

def get_client():
    global _client
    if _client is None:
        _client = clickhouse_connect.get_client(
            host="localhost",
            port=8123,
            username="default",
            password=""
        )
    return _client
