import sys, time, socket

def wait_for_port(address, port):
    start = time.perf_counter()
    timeout = 20
    while True:
        try:
            with socket.create_connection((address, port), timeout):
                return
        except OSError:
            time.sleep(0.1)
            if time.perf_counter() - start > timeout:
                raise

if __name__ == "__main__":
    wait_for_port(sys.argv[1], sys.argv[2])