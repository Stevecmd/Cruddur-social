#!/usr/bin/env python3

import socket

def check_xray_connectivity():
    sock = None
    try:
        xray_host = "xray-daemon"
        xray_port = 2000
        sock = socket.create_connection((xray_host, xray_port), timeout=5)
        print("Connection to xray-daemon on port 2000 succeeded")
    except socket.error as err:
        print(f"Connection to xray-daemon on port 2000 failed: {err}")
    finally:
        if sock:
            sock.close()

check_xray_connectivity()
