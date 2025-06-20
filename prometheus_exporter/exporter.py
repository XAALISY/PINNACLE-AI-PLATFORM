from prometheus_client import start_http_server, Counter
import random
import time

REQUESTS = Counter('http_requests_total', 'Total HTTP Requests')
ERRORS = Counter('http_errors_total', 'Total HTTP Errors')

def process_request():
    REQUESTS.inc()
    if random.random() < 0.1:
        ERRORS.inc()

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        process_request()
        time.sleep(1)
