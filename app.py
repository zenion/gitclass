import sys
from subprocess import check_output

if len(sys.argv) != 2:
    print("Usage: python3 app.py <domain>")
    sys.exit(1)

dns_servers = open("./dns_servers", "r").read().splitlines()
for server in dns_servers:
    a = check_output(["dig", "+short", "@" + server, sys.argv[1]])
    a = a.decode("utf-8").strip()
    print(f"querying {server} --> {a}")
