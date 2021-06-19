import socket
import concurrent.futures

tries = 1
bounds = range(1, 1001)
ip = "localhost"
threads = 20

timeout = 1


def check_port(tup):
    address, port, checker = tup
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((address, port))
        checker.append(port)
    except Exception:
        pass


sets = []

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for i in range(tries):
        sets.append([])
        for k in bounds:
            executor.submit(check_port, (ip, k, sets[i]))

print(sets)
